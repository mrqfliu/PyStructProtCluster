import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import to_tree
import pandas as pd


data = pd.read_csv('similarity_matrix.csv', index_col=0)
column_labels = data.index.tolist()
column_labels.extend(data.columns.tolist())
column_labels = sorted(set(column_labels))
column_labels = [label.replace(".pdb:A", "") for label in column_labels if ".pdb:A" in label]
similarity_matrix = data.values
# print(similarity_matrix)
# similarity_matrix =np.array(
#     [[0.5617,   0.5628,   0.5595,   0.56635],
#     [1.000001, 0.9337,   0.93555,  0.9342],
#     [1.000001, 1.000001, 0.9711,   0.98745],
#     [1.000001, 1.000001, 1.000001, 0.97]])

# 相似性矩阵转换成距离矩阵 (assuming distance = 1 - similarity)
distance_matrix = 1 - similarity_matrix

# 将距离矩阵转换为链接矩阵
condensed_distance_matrix = distance_matrix[np.triu_indices(distance_matrix.shape[0], k=0)]

# print(condensed_distance_matrix)
linkage_matrix = linkage(condensed_distance_matrix, method='average')
print(linkage_matrix)


# 链接矩阵转换为生成树
rootnode, nodelist = to_tree(linkage_matrix, rd=True)

# Create a recursive function to label the tree
# def add_newick(node, parent=None):
#     if node.is_leaf():
#         # Use the label for leaves
#         return column_labels[node.id]
#     else:
#         # Otherwise, build newick format for children
#         return '(%s,%s)' % (add_newick(node.get_left(), node), add_newick(node.get_right(), node))

def add_newick_with_distances(node, parent=None):
    if node.is_leaf():
        # 对于叶子节点，返回标签
        return column_labels[node.id]
    else:
        # 获取左右子节点的距离
        left_dist = (node.dist - node.get_left().dist)/2
        right_dist =(node.dist - node.get_right().dist)/2

        # 构造包含距离的字符串
        left_subtree = f'{add_newick_with_distances(node.get_left(), node)}:{left_dist}'
        right_subtree = f'{add_newick_with_distances(node.get_right(),node)}:{right_dist}'
        return '(%s,%s)' % (left_subtree, right_subtree)

# 构建生成树并写入文件
newick_tree = add_newick_with_distances(rootnode) + ';'
with open('tree.nwk', 'w') as f:
    f.write(newick_tree)

print('Newick tree:', newick_tree)

## 绘制树状图
#plt.figure()
#dendrogram(linkage_matrix, labels=column_labels)
#plt.title('UPGMA Hierarchical Clustering')
#plt.xlabel('Samples')
#plt.ylabel('Distance')
#plt.show()
