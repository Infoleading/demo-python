'''
带括号的 L 系统
用于生成植物
'''
from turtle import *

# 符号表
# 定义公式所用符号
# 二维表格，从单字符到多字符
symbol_list = [['F','f', '+', '-','[',']','X'],
              ['Fl', 'Fr']]

# 结点栈
# 用一个List来模拟stack, 仅使用其 append pop 方法取数
node_stack = []

# 拆分路径为符号列表
def split(path):
    pathList = list()
    i = 0
    while i<len(path):
        for j in range(len(symbol_list), 0, -1):
            if i+j<=len(path) and path[i:i+j] in symbol_list[j-1]:
                pathList.append(path[i:i+j])
                i = i+j
                break;
    return pathList

# 绘制路径
def draw_path(path, length, angle):
    pathList = split(path)
    for symbol in pathList:
        if symbol == 'F' or symbol == 'Fr' or symbol == 'Fl':
            down()
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
        elif symbol == 'f':
            up()
            forward(length)
        elif symbol == '[':
            node = [pos(), heading(), width()]
            node_stack.append(node)
        elif symbol == ']':
            node = node_stack.pop()
            up()
            setpos(node[0])
            seth(node[1])
            width(node[2])

# 应用规则
# 用规则替换路径中的符号
def apply_rule(rule, path):
    pathList = split(path)
    for i in range(len(pathList)):
        symbol = pathList[i]
        if symbol in rule:
            pathList[i] = rule[symbol]
    return "".join(symbol for symbol in pathList)


if __name__ == "__main__":
    
    # 设置屏幕
    setup(width=.99, height=.90, startx=0, starty=0)
    screensize(10000, 6000)
    tracer(False)
    hideturtle()
    speed(0)
    seth(90)
    up()
    setpos(0,-300)
    
    # 设置模型规则
    length = 400
    angle = 35
    path = 'F'
    rule = {
        'F':'F[-F][+F]'
        }
    
    # 生成路径
    n = 6 # 应用规则次数 [0,~]
    for i in range(n):
        path = apply_rule(rule,path)
        
    # 开始绘图
    draw_path(path, length/(n*2), angle)
    
    exitonclick()