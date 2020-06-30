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
import turtle as tt

class Lsystem():
    def __init__(self):
        # 符号表
        # 定义公式所用符号
        # 二维表格，从单字符到多字符
        self.symbol_list = [
            ['F','f','+','-','|','[',']','#','!','@','{','}','>','<','&','(',')',  'V','W','X','Y','Z'],
            ['Fl', 'Fr']
        ]
        # 状态栈
        # 用List来充当栈，仅用其 append 和 pop 方法操作，实现绘图状态的保存
        self.state_stack = []
        self.running = True # 终止绘制

    # 拆分路径为符号列表
    def split(self, path):
        pathList = list()
        i = 0
        while i<len(path):
            for j in range(len(self.symbol_list), 0, -1): # 从最长的符号开始寻找，先匹配较长的符号
                if i+j<=len(path) and path[i:i+j] in self.symbol_list[j-1]:
                    pathList.append(path[i:i+j])
                    i = i+j
                    break;
        return pathList

    # 执行指令
    # 解析路径并
    def draw(self, turtle, path, length, angle, lengthFactor=1, angleIncrement=0, widthRate=1):
        pathList = self.split(path)
        for symbol in pathList:
            # 前进单位长度并划线
            if self.running == False:
                return
            elif symbol == 'F' or symbol == 'Fr' or symbol == 'Fl':
                turtle.down()
                turtle.forward(length)
            # 前进单位长度但不划线
            elif symbol == 'f':
                turtle.up()
                turtle.forward(length)
            # 左转单位角度
            elif symbol == '+':
                turtle.right(angle)
            # 右转单位角度
            elif symbol == '-':
                turtle.left(angle)
            # 反向，转180度
            elif symbol == '|':
                turtle.seth(heading()-180)
            # 将当前绘画状态入栈
            elif symbol == '[':
                state = [turtle.pos(), turtle.heading(), turtle.pensize(), turtle.color()]
                self.state_stack.append(state)
            # 弹栈并获取绘画状态
            elif symbol == ']':
                state = self.state_stack.pop()
                turtle.up()
                turtle.setpos(state[0])
                turtle.seth(state[1])
                turtle.pensize(state[2])
                turtle.color(state[3][0], state[3][1])
            # 增加线的宽度
            elif symbol == '#':
                turtle.pensize(pensize()*widthRate)
            # 减少线的宽度
            elif symbol == '!':
                turtle.pensize(pensize()/widthRate)
            # 以线宽作为半径画点
            elif symbol == '@':
                turtle.dot()
            # 打开一个多边形
            elif symbol == '{':
                turtle.begin_poly()
            # 关闭一个多边形，并以填充色填充
            elif symbol == '}':
                turtle.end_poly()
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
    def apply_rule(self, rule, path):
        pathList = self.split(path)
        for i in range(len(pathList)):
            symbol = pathList[i]
            if symbol in rule:
                pathList[i] = rule[symbol]
        return "".join(symbol for symbol in pathList) #将字符串列表合并为一个字符串
    

if __name__ == "__main__":
    
    # 设置屏幕
    tt.setup(width=.99, height=.90, startx=0, starty=0)
    tt.screensize(10000, 10000)
    tt.tracer(False)
    tt.hideturtle()
    tt.speed(0)
    tt.seth(90)
    tt.pensize(2)
    tt.up()
    tt.setpos(0,-300)
    
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
    l = Lsystem()
    n = 10 # 应用规则次数 [0,~]
    for i in range(n):
        path = l.apply_rule(rule,path)
    print(path)
        
    # 执行绘制
    l.draw(tt, path, length/(1.6**n), angle, 1, 1, 1)
    
    tt.exitonclick()