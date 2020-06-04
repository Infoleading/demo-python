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

# 计算信息增益
# input: 样本集, 划分后样本集


# 创建决策树
# input: 训练集(二维列表，其中最后一列为标签), 属性集(一维列表，元素为列号)
# output: dicisionNode 的一个实例
def buildDicisionTree(trainSet, attrSet):
    node = decisionNode(-1, None, None, None, None)
    
    # 如果当前训练集熵为0，表明只有一种结果标签，则无需再分类，立即返回作为叶结点
    entropy = calcuEntrop(trainSet)
    if entropy = 0:
        return node.label = trainSet[0][-1]
    
    # 对各属性进行不同值的计数，每属性一个字典，各属性组成字典列表
    counterDictList = [Counter(entry[colNum] for entry in trainSet) for colNum in range(0, len(attrSet))]
    # 对取字典中的计数最小值生成计数最小值列表,
    minCounterList = [ min(counterDict.values()) for counterDict in counterDictList]
    
    # 如果已没有未参与分类的属性 或 属性取值全部相同(没有分辨力)，则生成叶结点对象返回
    if len(attrSet) == 0 or min(minCounterList) == len(trainSet):
        # 对标签不同值计数
        labelCountsDict = Counter(entry[-1] for entry in trainSet)
        # 取计数值最大的标签 用作中结点标签
        label = max(labelCountsDict, key=lambda x:labelCountsDict[x])        
        node.label = label # 叶结点仅有 label 值
        return node    
    
    
    # 否则，遍历当前属性集，寻找最优划分属性
    gainList = list()
    for colNum in range(0, len(attrSet)):
        # 如果当前属性有不同的取值
        if minCounterList[colNum]<len(attrSet):
            gainList[colNum] = 
            # 生成当前训练子集中属性colNum的值列表
            colValue = [row[colNum] for row in trainSet]
        # 遍历此列所有列值
        for value in colValue:
            # 按此列值拆分数据集
            (subSet1, subSet2) = divideSet(trainSet, colNum, value)
            set1Entropy = calcuEntrop(subSet1)
            set2Entropy = calcuEntrop(subSet2)
            if set1Entropy = 0
                decisionNode(colNum, colValue, subSet1[0][-1], None, None)
            else:
                
            calcuEntrop(subSet2)
            if :
                return 
            
                


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
    
    