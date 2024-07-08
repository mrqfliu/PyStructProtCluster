import os



# 获取 pdbs 文件夹中的所有 pdb 文件
pdb_files = os.listdir('pdbs')
pdb_files = sorted([f for f in pdb_files if f.endswith('.pdb')])

# 遍历文件进行处理
for i in range(1, len(pdb_files)):
    target_files = pdb_files[i:]
    file_path = os.path.join('pdbs', f'list_pdb{i + 1}{len(pdb_files)}.txt')
    with open(file_path, 'w') as f:  # 存在则覆盖更新
        for file in target_files:
            f.write(file + '\n')

