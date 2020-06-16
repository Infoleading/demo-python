from collections import Counter
from functools import reduce
import operator
import math
import copy

attrName = ['site', 'nation', 'FAQ', 'pages']

# 结点数据结构
class decisionNode:
    def __init__(self, colNum=-1, conditionValue=None, label=None, tb=None, fb=None):
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
    # 本方法仅将数据集划分为两类
    set1 = [row for row in dataSet if split_function(row)]
    set2 = [row for row in dataSet if not split_function(row)]
    #print(len(set1))
    #print(len(set2))
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
def calcuEntropy(dataSet):
    labelCounts = Counter(entry[-1] for entry in dataSet)
    #print(labelCounts)
    probability = [float(v)/sum(labelCounts.values()) for v in labelCounts.values()]
    return -1*reduce(operator.add, map(lambda x:x*math.log(x,2), probability ))

# 计算信息增益
# input: 样本集, 划分后样本集
# output: 信息增益
def calcuGain(dataSet, subSetTuple):
    return calcuEntropy(dataSet)-sum([len(subSet)/len(dataSet)*calcuEntropy(subSet) for subSet in subSetTuple])


# 创建决策树
# input: 训练集(二维列表，其中最后一列为标签), 属性集(一维列表，元素为列号)
# output: dicisionNode 的一个实例
def buildDicisionTree(trainSet, attrSet):
    print("--------------------------------------------")
    print(trainSet)
    node = decisionNode(-1, None, None, None, None)
    
    # 如果当前训练集熵为0，表明只有一种结果标签，则无需再分类，立即返回作为叶结点
    entropy = calcuEntropy(trainSet)
    if entropy == 0:
        node.label = trainSet[0][-1]
        print("classificationis done, class is : ",end="")
        print(node.label)
        return node
    
    # 对数据集中各属性进行不同取值的计数，每属性一个字典，各属性组成字典列表
    counterDictList = [Counter(entry[colNum] for entry in trainSet) for colNum in range(0, len(attrSet))]
    # 对字典中的计数取最小值生成计数最小值列表,
    minCounterList = [ min(counterDict.values()) for counterDict in counterDictList]   
    # 如果已没有未参与分类的属性 或 属性取值全部相同(没有分辨力)，则生成叶结点对象返回
    if len(attrSet) == 0 or min(minCounterList) == len(trainSet):
        # 对标签不同值计数
        labelCountsDict = Counter(entry[-1] for entry in trainSet)
        # 取计数值最大的标签 用作中结点标签
        label = max(labelCountsDict, key=lambda x:labelCountsDict[x])        
        node.label = label # 叶结点仅有 label 值
        print("no attribute to use")
        return node    
        
    # 否则，遍历当前属性集，寻找最优划分属性的最优划分值
    bestGain = 0
    bestAttr = 0
    bestValue = 0
    for colNum in range(0, len(attrSet)):
        # 获取 colNum 属性的全部值，并去重复
        colValue = list(set([row[attrSet[colNum]] for row in trainSet]))
        # 遍历此列所有值，用每个取值试拆分数据集，并计算拆分后的信息增益
        for value in colValue:
            #print(attrSet[colNum])
            #print(value)
            # 试拆分数据
            setTuple = divideSet(trainSet,attrSet[colNum],value)
            # 只有在划分出的两个子集都有数据的情况下才计算信息增益
            if len(setTuple[0])>0 and len(setTuple[1])>0:
                gain = calcuGain(trainSet, setTuple)
            if gain>bestGain:
                bestAttr = attrSet[colNum]
                bestValue = value
                bestGain = gain
    # 拆分数据集            
    subSetTuple = divideSet(trainSet, bestAttr, bestValue)
    # 记录本次拆分属性、值
    node.colNum = bestAttr
    node.conditionValue = bestValue
    # 打印结点信息
    print("if ",end="")
    print(attrName[bestAttr],end="")
    print(" is(or grate) ",end="")
    print(bestValue)
    # 递归生成本结点左右子树
    attrSet.remove(bestAttr) # 移除已经考虑过的属性
    print("the least attribute is: ",end="")
    print(attrSet)
    node.tb = buildDicisionTree(subSetTuple[0], copy.deepcopy(attrSet))
    node.fb = buildDicisionTree(subSetTuple[1], copy.deepcopy(attrSet))
    return node
               


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
    entropy1 = calcuEntropy(set1)
    entropy2 = calcuEntropy(set2)
    print("Entropy:")
    print(entropy1)
    print(entropy2)
    
    # 创建决策树
    buildDicisionTree(data, list(range(0,len(data[0])-1)))
    