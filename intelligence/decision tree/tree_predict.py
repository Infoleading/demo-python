# 结点数据结构
class decision_node:
    def __init__(slef, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col # 属性列值
        self.value = value # 判定条件值（一般是判定为True的值）
        self.results = results # 标签值，除叶结点外，其它结点都为None值
        self.tb = tb # true 子树
        self.fb = fb # false 子树
    
# 数据集划分函数
# 根据某一列的值将数据划分成两个集合
# 处理数值数据和字符串数据
def divide_set(rows, column, value):
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


#结果值计数
#从分类结果中找出每种结果的个数
def unique_counts(rows):
    results = {} # 用字典来保存各种结果的计数
    for row in rows:
        r = row[len(row)-1]
        if r not in results:
            results[r] = 0 # 初始化字典项，key=r  value=0
        results[r]+=1 # 按key值r来索引value并+1
    return results
    
#基尼不纯度
def gini_impurity(rows):
    total = len(rows)
    lab_counts = unique_counts(rows)
    imp = 0
    for k1 in lab_counts:
        p1 = float(lab_counts[k1])/total
        for k2 in lab_counts:
            if k1 == k2: continue
            p2 = float(lab_counts[k2])/total
            imp+=p1*p2
    return imp


if __name__ == '__main__':
    
    # 从有分割符的文件数据中生成数据字典
    file = open('decision_tree_example.txt', 'rt')
    raw = [line.strip('\n').split('\t') for line in file]
    data = [[item[0], item[1], item[2], int(item[3]), item[4]] for item in raw]
    
    # 按某一列值分割数据集
    (set1, set2) = divide_set(data, 2, 'No')
    print([item[4] for item in set1])
    print([item[4] for item in set2])
    
    # 统计这一分割下标签的划分情况
    set3 = unique_counts(set1)
    set4 = unique_counts(set2)
    print(set3)
    print(set4)
    
    # 计算每个分类的基尼不纯度
    g1 = gini_impurity(set3)
    g2 = gini_impurity(set4)
    print(g1)
    print(g2)
    