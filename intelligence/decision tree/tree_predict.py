
class decision_node:
    def __init__(slef, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb
    
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

def unique_counts(rows):
    results = {} # 用字典来保存各种结果的计数
    for row in rows:
        r = row[len(row)-1]
        if r not in results:
            results[r] = 0 # 初始化字典项，key=r  value=0
        results[r]+=1 # 按key值r来索引value并+1
    return results


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
    print(unique_counts(set1))
    print(unique_counts(set2))
    