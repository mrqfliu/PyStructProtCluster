import pandas as pd

data = pd.read_csv('combined_similarity.txt', sep='\t')

# 计算相似性分数 (TM1 + TM2) / 2
numeric_cols = ['TM1', 'TM2']
data['Similarity'] = data[numeric_cols].apply(lambda row: row.dropna().mean(), axis=1)

# 提取PDB链ID并去重形成一个新的列表
protein_ids_index = sorted(data['#PDBchain1'].drop_duplicates().values.flatten())
protein_ids_columns = sorted(data['PDBchain2'].drop_duplicates().values.flatten())
print(protein_ids_index)
print(protein_ids_columns)


# 创建一个初始的相似性矩阵，其中值为1 + 10**(-6)
similarity_matrix = pd.DataFrame([[1 + 10**(-6)] * len(protein_ids_columns) for _ in protein_ids_index],columns=protein_ids_columns, index=protein_ids_index)
# print(similarity_matrix)
# 更新矩阵，将计算出的相似性值填入相应的位置
for _, row in data.iterrows():
    similarity_matrix.at[row['#PDBchain1'], row['PDBchain2']] = row['Similarity']

# 将结果保存为csv文件
similarity_matrix.to_csv('similarity_matrix.csv')
print(similarity_matrix)



