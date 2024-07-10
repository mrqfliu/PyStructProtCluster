import pandas as pd
import os

# Automatically obtain the current working directory
current_path = os.getcwd()

# Define file path
file_path = current_path + '/test/af_output/'

# Automatically obtain a list of file names that match the format
file_list = sorted([f for f in os.listdir(file_path) if f.startswith('align') and f.endswith('.txt') and len(f) > len('align.txt')])

# Read the first file and store it as a DataFrame
result_df = pd.read_csv(file_path +file_list[0], sep='\t')

# Traverse the remaining files and stack them with result_df
for file in file_list[1:]:
    temp_df = pd.read_csv(file_path + file, sep='\t')
    result_df = pd.concat([result_df, temp_df], axis=0)

result_df.iloc[:, 0] = result_df.iloc[:, 0].str.replace(current_path + '/pdbs/', "")
# Save the result as a new txt file
result_df.to_csv('combined_similarity.txt', sep='\t', index=False)
