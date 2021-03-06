from collections import Counter
from functools import reduce
import operator
import math

# 结点数据结构
class decisionNode:
    def __init__(slef, colNum=-1, conditionValue=None, label=None, tb=None, fb=None):
        self.colNum = colNum # 属性列值
        self.conditionValue = conditionValue # 判定条件值（一般是判定为True的值）
        self.label = label # 标签值，除叶结点外，其它结点都为None值
        self.tb = tb # true 子树
        self.fb = fb # false 子树
    
# 数据集划分函数
# 根据某一列的值将数据划分成两个集合
# 处理数值数据和字符串数据
def divideSet(dataSet, column, value):
    # 定义一lambda函数，用于划分判断 
    split_function = None
    if isinstance(value, int) or isinstance(value, float):
        # 处理数值型数据
        split_function = lambda row:row[column]>=value
    else:
        # 处理非数值型数据
        split_function = lambda row:row[column]==value
    
    set1 = [row for row in dataSet if split_function(row)]
    set2 = [row for row in dataSet if not split_function(row)]
    return (set1, set2)


# 计算基尼不纯度
# input: 样本集(二维列表，其中最后一列为标签)
# output: 该样本集的基尼不纯度(float)
def calcuGini(dataSet):
    labelCounts = Counter(entry[-1] for entry in dataSet) # 生成标签计数字典(取最后一列为标签值)
    probability = [float(v)/sum(labelCounts.values()) for v in labelCounts.values()] # 计算各标签概率
    return 1 - reduce(operator.add, map(lambda x: x**2, probability )) # 返回 gini impurity
    
    
# 计算信息熵
# input: 样本集(二维列表，其中最后一列为标签)
# output: 该样本集的信息熵(float)
def calcuEntrop(dataSet):
    labelCounts = Counter(entry[-1] for entry in dataSet)
    probability = [float(v)/sum(labelCounts.values()) for v in labelCounts.values()]
    return -1*reduce(operator.add, map(lambda x:x*math.log(x,2), probability ))


# 创建决策树(书中原码)
# 二分法，每个结点分出两个子树
# input：数据集rows，分值函数
# output: 结点对象
def buildtree(rows,scoref=calcuEntrop):
    # 如果数据为空，返回一个空结点
    if len(rows)==0: return decisionnode( )
    
    current_score=scoref(rows)
    # 设置变量追踪最佳划分
    best_gain=0.0
    best_criteria=None
    best_sets=None
    column_count=len(rows[0])-1 # 列数，最后一列是标签不考虑
    # 遍历各列
    for col in range(0,column_count):
        # Generate the list of different values in
        # this column
        column_values={} # 计数字典
        # 遍历各行
        for row in rows:
            column_values[row[col]]=1 # 取值计数
        # 使用本列各取值尝试划分数据
        for value in column_values.keys( ):
            (set1,set2)=divideset(rows,col,value)
            # 计算信息增益
            p=float(len(set1))/len(rows)
            gain=current_score-p*scoref(set1)-(1-p)*scoref(set2)
            if gain>best_gain and len(set1)>0 and len(set2)>0:
                best_gain=gain
                best_criteria=(col,value)
                best_sets=(set1,set2)
    # Create the subbranches
    if best_gain>0:
        trueBranch=buildtree(best_sets[0])
        falseBranch=buildtree(best_sets[1])
        return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
    else:
        return decisionnode(results=uniquecounts(rows))
                    
if __name__ == '__main__':
    
    # 从有分割符的文件数据中生成数据字典
    file = open('decision_tree_example.txt', 'rt')
    raw = [line.strip('\n').split('\t') for line in file]
    data = [[item[0], item[1], item[2], int(item[3]), item[4]] for item in raw]
    
    # 按某一列值分割数据集
    (set1, set2) = divideSet(data, 2, 'No')
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
    
    