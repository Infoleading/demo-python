'''
带括号的 L 系统
用于生成植物
'F':'F[+F]F[-F]F'

'F':'F[+F]F[-F][F]'

'F':'FF-[-F+F+F]+[+F-F-F]'

'X':'F[+X]F[-X]+X'
'F':'FF'

'X':'F[+X][-X]FX'
'F':'FF'

'X':'F-[[X]+X]+F[+FX]-X'
'F':'FF'

'''
from turtle import *
from rainbow import *

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
    screensize(10000, 10000)
    tracer(False)
    hideturtle()
    bgcolor('#000000')
    speed(0)
    
    # 设置模型规则
    length = 40
    angle = 22.5
    path = 'X'
    rule = {
        'X':'F-[[X]+X]+F[+FX]-X',
        'F':'FF'
        }
    
    # 生成路径
    n = 6 # 应用规则次数 [0,~]
    for i in range(n):
        path = apply_rule(rule,path)
    print(path)
        
    # 开始绘图
    level=4 # 线条层次 level-1
    HSB=(120, 1, 1) # 色相，饱和度，明度
    wid=3  # 线宽
    shadow=1.3 # 阴影宽率
    contrast=1.4 # 色彩对比度
    origin = (0,-300) # 原点位置
    head = 90 # 朝向
    up()
    goto(origin)
    seth(head)
    for i in range(1,level):
        width(wid*((level-1)**shadow)/(i**shadow))
        color(HSB2RGB(HSB[0], HSB[1], HSB[2]*(i/(level-1))**contrast))
        draw_path(path, length/(n*2), angle)
        up()
        goto(origin)
        seth(head)
    
    exitonclick()