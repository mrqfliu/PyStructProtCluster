#!/bin/bash
#DSUB -n alignment
#DSUB -A root.project.P18Z19700N0076
#DSUB -R cpu=2;mem=10240
#DSUB -N 1

# 获取当前工作目录
current_path=$(pwd)

#DSUB -oo $current_path/test/af_output/%J.out
#DSUB -eo $current_path/test/af_output/%J.er

source /path/to/anaconda3/bin/activate
conda activate saturn

#任务1 获取pdb文件子列表
python ./PdbFileListGenerator.py

#任务2 并行实现结构两两比对
# 获取 pdbs 文件夹中的所有 pdb 文件
pdb_files=($(ls "$current_path/pdbs/" | grep '\.pdb$'))

# 创建一个进程组
set -m

# 可调节的并行数量
parallel_count=2  # 您可以根据需要修改这个值

# 已运行的进程数量
running_count=0

for ((i=0; i<${#pdb_files[@]}-1; i++)); do
    pro=${pdb_files[$i]}
    dir2="$current_path/pdbs/"
    list_file="$current_path/pdbs/list_pdb$((i + 2))${#pdb_files[@]}.txt"
    output_file="$current_path/test/af_output/align$((i + 1)).txt"
    if [ -s "$output_file" ]; then
        : > "$output_file"
    fi
    command="./USalign/USalign $current_path/pdbs/$pro -dir2 $dir2 $list_file -outfmt 2"

    # 如果运行的进程数量小于并行数量，启动新进程
    if [ $running_count -lt $parallel_count ]; then
        (
            # 在子进程中执行命令
            $command >> "$output_file"
        ) &
        running_count=$((running_count + 1))
    else
        # 持续等待，直到有进程结束
        while [ $running_count -ge $parallel_count ]; do
            wait -n
            running_count=$((running_count - 1))
        done
        # 等待结束后再启动新进程
        (
            # 在子进程中执行命令
            $command >> "$output_file"
        ) &
        running_count=$((running_count + 1))
    fi
done

# 等待所有剩余的子进程结束
wait

#任务3 蛋白质结构对比堆叠后的txt文件
python ./get_align.py

#任务4 生成4x4的相似性矩阵，并将结果保存为.csv格式
python ./similarity_matrix.py

#任务5  输出.nwk文件，用于生成树状图
python ./generate_tree.py

