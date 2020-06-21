'''
完整符号的 L 系统
在Lsystem3的基础上引入更多的控制符号

F    前进单位长度并划线
f    前进单位长度但不划线
+    左转单位角度
-    右转单位角度
|    反向，转180度
[    将当前绘画状态入栈
]    弹栈并获取绘画状态
#    增加线的宽度
!    减少线的宽度
@    以线宽作为半径画点
{    打开一个多边形
}    关闭一个多边形，并以填充色填充
>    将线长乘以线长比例因子
<    将线长除以线长比例因子
&    交换 + - 符号含义
(    通过转弯角度增量来减少转弯角度
)    通过转弯角度增量来增加转弯角度
'''
from turtle import *

# 符号表
# 定义公式所用符号
# 二维表格，从单字符到多字符
symbol_list = [
    ['F','f','+','-','|','[',']','#','!','@','{','}','>','<','&','(',')',  'V','W','X','Y','Z'],
    ['Fl', 'Fr']
    ]

# 状态栈
# 用List来充当栈，仅用其 append 和 pop 方法操作，实现绘图状态的保存
state_stack = []

# 拆分路径为符号列表
def split(path):
    pathList = list()
    i = 0
    while i<len(path):
        for j in range(len(symbol_list), 0, -1): # 从最长的符号开始寻找，先匹配较长的符号
            if i+j<=len(path) and path[i:i+j] in symbol_list[j-1]:
                pathList.append(path[i:i+j])
                i = i+j
                break;
    return pathList

# 执行指令
# 解析路径并
def execute(path, length, angle, lengthFactor, angleIncrement, widthRate):
    pathList = split(path)
    for symbol in pathList:
        # 前进单位长度并划线
        if symbol == 'F' or symbol == 'Fr' or symbol == 'Fl':
            down()
            forward(length)
        # 前进单位长度但不划线
        elif symbol == 'f':
            up()
            forward(length)
        # 左转单位角度
        elif symbol == '+':
            right(angle)
        # 右转单位角度
        elif symbol == '-':
            left(angle)
        # 反向，转180度
        elif symbol == '|':
            seth(heading()-180)
        # 将当前绘画状态入栈
        elif symbol == '[':
            state = [pos(), heading(), pensize(), color()]
            state_stack.append(state)
        # 弹栈并获取绘画状态
        elif symbol == ']':
            state = state_stack.pop()
            up()
            setpos(state[0])
            seth(state[1])
            pensize(state[2])
            color(state[3][0], state[3][1])
        # 增加线的宽度
        elif symbol == '#':
            pensize(pensize()*widthRate)
        # 减少线的宽度
        elif symbol == '!':
            pensize(pensize()/widthRate)
        # 以线宽作为半径画点
        elif symbol == '@':
            dot()
        # 打开一个多边形
        elif symbol == '{':
            begin_poly()
        # 关闭一个多边形，并以填充色填充
        elif symbol == '}':
            end_poly()
        # 将线长乘以线长比例因子
        elif symbol == '>':
            length *= lengthFactor
        # 将线长除以线长比例因子
        elif symbol == '<':
            length /= lengthFactor
        # 交换 + - 符号含义
        elif symbol == '&':
            pass
        # 通过转弯角度增量来减少转弯角度
        elif symbol == '(':
            angle -= angleIncrement
        # 通过转弯角度增量来增加转弯角度
        elif symbol == ')':
            angle += angleIncrement    
        

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
    speed(0)
    seth(90)
    width(2)
    up()
    setpos(0,-300)
    
    # 设置模型规则
    length = 1500
    angle = 22.5
    path = 'VZFFF'
    rule = {
        'V':'[+++W][---W]YV',
        'W':'+X[-W]Z',
        'X':'-W[+X]Z',
        'Y':'YZ',
        'Z':'[-FFF][+FFF]F'
        }
    
    # 生成路径
    n = 10 # 应用规则次数 [0,~]
    for i in range(n):
        path = apply_rule(rule,path)
    print(path)
        
    # 执行命令
    execute(path, length/(1.6**n), angle, 1, 1, 1)
    
    exitonclick()