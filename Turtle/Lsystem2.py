from turtle import *

# 符号表
# 定义公式所用符号
symbolList = [['F','f', '+', '-'],
              ['Fl', 'Fr']]

# 拆分路径为符号列表
def split(path):
    pathList = list()
    i = 0
    while i<len(path):
        for j in range(len(symbolList), 0, -1):
            if i+j<=len(path) and path[i:i+j] in symbolList[j-1]:
                pathList.append(path[i:i+j])
                i = i+j
                break;
    return pathList

# 绘制路径
def draw_path(path, length, angle):
    pathList = split(path)
    for symbol in pathList:
        if symbol == 'Fr' or symbol == 'Fl':
            down()
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
        elif symbol == 'f':
            up()
            forward(length)

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
    # setup Screen and window
    setup(width=.99, height=.90, startx=0, starty=0)
    screensize(10000, 6000)
    tracer(True)
    hideturtle()
    speed(0)
    # setup parameter
    length = 100
    angle = 60
    path = 'Fr'
    rule = {
        'Fl':'Fr+Fl+Fr',
        'Fr':'Fl-Fr-Fl',
        }
    # generate path
    n = 4 # 应用规则次数 [0,~]
    for i in range(n):
        path = apply_rule(rule,path)
    # 开始绘图
    
    draw_path(path, length/(n*2), angle)
    
    exitonclick()