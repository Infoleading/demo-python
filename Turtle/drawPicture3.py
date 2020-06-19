'''
边复写和结点复写的 L 系统
用于规则几何图形建模

        'F1':'F2+F1+F2',
        'F2':'F1-F2-F1'
        Fl
        'Fl':'Fl+Fr++Fr-Fl--FlFl-Fr+',
        'Fr':'-Fl+FrFr++Fr+Fl--Fl-Fr'
        -L
        'L':'LF+RFR+FL-F-LFLFL-FRFR+',
        'R':'-LFLF+RFRFR+F+RF-LFL-FR'
        -L
        'L':'+RF-LFL-FR+',
        'R':'-LF+RFR+FL-'
'''
from turtle import *

# 色彩空间转换
def HSB2RGB(h, s, v):
    h1 = h%360
    hi = int((h1)/60)%6
    f = h1/60- hi
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    RGB = [0.0, 0.0, 0.0]
    if hi==0:
        RGB = [v, t, p]
    elif hi==1:
        RGB = [q, v, p]
    elif hi==2:
        RGB = [p, v, t]
    elif hi==3:
        RGB = [p, q, v]
    elif hi==4:
        RGB = [t, p, v]
    elif hi==5:
        RGB = [v, p, q]
    return (RGB[0], RGB[1], RGB[2])

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
        if symbol == 'F' or symbol in symbolList[-1]:
            down()
            fd(length)
        elif symbol == 'B':
            down()
            bk(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
        elif symbol == 'f':
            up()
            fd(length)
        elif symbol == 'b':
            up()
            bk(length)
            
# 应用规则
# 用规则替换路径中的符号
def apply_rule(rule, path):
    pathList = split(path)
    for i in range(len(pathList)):
        symbol = pathList[i]
        if symbol in rule:
            pathList[i] = rule[symbol]
    return "".join(symbol for symbol in pathList)

# 符号表
# 定义公式所用符号
symbolList = [['F','B','f','b', '+', '-','L','R'],
              ['F1','F2']]

if __name__ == "__main__":
    # setup Screen and window
    setup(width=.99, height=.90, startx=0, starty=0)
    screensize(10000, 10000)
    tracer(False)
    hideturtle()
    bgcolor('#000000')
    speed(0)
    
    # setup parameter
    length = 60
    angle = 60
    path = 'F++F++F'
    rule = {
        'F':'F-F++F-F'
        }
    # 生成绘图路径
    n = 4 # 应用规则次数 [0,~]
    for i in range(n):
        path = apply_rule(rule,path)
    print(path)
    
    # 开始绘图
    level=10 # 线条层次 level-1
    HSB=(60, 1, 1) # 色相，饱和度，明度
    wid=3  # 线宽
    shadow=1.3 # 阴影宽率
    contrast=1.4 # 色彩对比度
    origin = (0,0) # 原点位置
    head = 60 # 朝向
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