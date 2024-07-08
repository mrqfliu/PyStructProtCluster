import pandas as pd
import os

# 自动获取当前工作目录
current_path = os.getcwd()

# 定义文件路径
file_path = current_path + '/test/af_output/'

# 自动获取符合格式的文件名列表
file_list = sorted([f for f in os.listdir(file_path) if f.startswith('align') and f.endswith('.txt') and len(f) > len('align.txt')])

# 读取第一个文件并将其存储为一个DataFrame
result_df = pd.read_csv(file_path +file_list[0], sep='\t')

# 遍历剩余的文件并将它们与result_df进行堆叠
for file in file_list[1:]:
    temp_df = pd.read_csv(file_path + file, sep='\t')
    result_df = pd.concat([result_df, temp_df], axis=0)

result_df.iloc[:, 0] = result_df.iloc[:, 0].str.replace(current_path + '/pdbs/', "")
# 将结果保存为一个新的txt文件
result_df.to_csv('combined_similarity.txt', sep='\t', index=False)
