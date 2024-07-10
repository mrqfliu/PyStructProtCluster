#!/bin/bash
#DSUB -n alignment
#DSUB -A root.project.P18Z19700N0076
#DSUB -R cpu=2;mem=10240
#DSUB -N 1
# Get the current working directory
current_path=$(pwd)

#DSUB -oo $current_path/test/af_output/%J.out
#DSUB -eo $current_path/test/af_output/%J.er

#Task 2: Parallel implementation structure pairwise comparison
# Get all PDB files in the pdbs folder
pdb_files=($(ls "$current_path/pdbs/" | grep '\.pdb$'))
# Create a process group
set -m

# Adjustable number of parallels
parallel_count=2   # You can modify this value as needed

# Number of running processes
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
    # If the number of running processes is less than the number of parallel processes, start a new process
    if [ $running_count -lt $parallel_count ]; then
        (
            # Execute commands in child processes
            $command >> "$output_file"
        ) &
        running_count=$((running_count + 1))
    else
        # Continuously wait until a process ends
        while [ $running_count -ge $parallel_count ]; do
            wait -n
            running_count=$((running_count - 1))
        done
        # Wait until the end before starting a new process
        (
            # Execute commands in child processes
            $command >> "$output_file"
        ) &
        running_count=$((running_count + 1))
    fi
done

# Wait for all remaining child processes to end
wait

