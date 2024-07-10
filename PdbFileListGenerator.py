import os

# Obtain all the PDB files in the "pdbs" folder.
pdb_files = os.listdir('pdbs')
pdb_files = sorted([f for f in pdb_files if f.endswith('.pdb')])

# Traverse files for processing
for i in range(1, len(pdb_files)):
    target_files = pdb_files[i:]
    file_path = os.path.join('pdbs', f'list_pdb{i + 1}{len(pdb_files)}.txt')
    with open(file_path, 'w') as f:  # Overwrite updates if present
        for file in target_files:
            f.write(file + '\n')

