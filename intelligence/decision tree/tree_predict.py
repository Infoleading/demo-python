from collections import Counter
from functools import reduce
import operator
import math

# 结点数据结构
class decisionNode:
    def __init__(slef, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col # 属性列值
        self.value = value # 判定条件值（一般是判定为True的值）
        self.results = results # 标签值，除叶结点外，其它结点都为None值
        self.tb = tb # true 子树
        self.fb = fb # false 子树
    
# 数据集划分函数
# 根据某一列的值将数据划分成两个集合
# 处理数值数据和字符串数据
def divideSet(rows, column, value):
    # 定义一lambda函数，用于划分判断 
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        # 处理数值型数据
        split_function = lambda row:row[column]>=value
    else:
        # 处理非数值型数据
        split_function = lambda row:row[column]==value
    
    set1 = [row for row in rows if split_function(row)]
    set2 = [row for row in rows if not split_function(row)]
    return (set1, set2)


# 计算基尼不纯度
# input: 数据集列表(其中最后一列为标签)
# output: 这一分类数据集的基尼不纯度(float值)
def calcuGini(dataSet):
    labelCounts = Counter(entry[-1] for entry in dataSet) # 生成标签计数字典(取最后一列为标签值)
    probability = [float(v)/sum(labelCounts.values()) for v in labelCounts.values()] # 计算各标签概率
    return 1 - reduce(operator.add, map(lambda x: x**2, probability )) # 返回 gini impurity
    
    
#计算数据集的信息熵
#input: 给定数据集
#output: 该数据集的信息熵
def calcuEntrop(dataSet):
    labelCounts = Counter(entry[-1] for entry in dataSet)
    probability = [float(v)/sum(labelCounts.values()) for v in labelCounts.values()]
    return -1*reduce(operator.add, map(lambda x:x*math.log(x,2), probability ))


if __name__ == '__main__':
    
    # 从有分割符的文件数据中生成数据字典
    file = open('decision_tree_example.txt', 'rt')
    raw = [line.strip('\n').split('\t') for line in file]
    data = [[item[0], item[1], item[2], int(item[3]), item[4]] for item in raw]
    
    # 按某一列值分割数据集
    (set1, set2) = divideSet(data, 4, 'None')
    print([item[-1] for item in set1])
    print([item[-1] for item in set2])
    
    # 计算 gini impurity
    g3 = calcuGini(set1)
    g4 = calcuGini(set2)
    print("Gini impurity:")
    print(g3)
    print(g4)
    
    # 计算 信息熵
    entropy1 = calcuEntrop(set1)
    entropy2 = calcuEntrop(set2)
    print("Entropy:")
    print(entropy1)
    print(entropy2)
    
    