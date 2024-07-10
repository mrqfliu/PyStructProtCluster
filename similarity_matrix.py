import pandas as pd

data = pd.read_csv('combined_similarity.txt', sep='\t')

# Calculate similarity score (TM1 + TM2) / 2
numeric_cols = ['TM1', 'TM2']
data['Similarity'] = data[numeric_cols].apply(lambda row: row.dropna().mean(), axis=1)

# Extract PDB chain ID and de reformat to form a new list
protein_ids_index = sorted(data['#PDBchain1'].drop_duplicates().values.flatten())
protein_ids_columns = sorted(data['PDBchain2'].drop_duplicates().values.flatten())


# Create an initial similarity matrix with values of 1 + 10**(-6)
similarity_matrix = pd.DataFrame([[1 + 10**(-6)] * len(protein_ids_columns) for _ in protein_ids_index],columns=protein_ids_columns, index=protein_ids_index)
# print(similarity_matrix)
# Update the matrix and fill the calculated similarity values into the corresponding positions
for _, row in data.iterrows():
    similarity_matrix.at[row['#PDBchain1'], row['PDBchain2']] = row['Similarity']

# Save the results as a .csv file
similarity_matrix.to_csv('similarity_matrix.csv')
print(similarity_matrix)
