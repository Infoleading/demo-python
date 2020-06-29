import tkinter as tk
import turtle as tt
import Lsystem as ls

# 海龟画板类
# 请在此类中添加各种形状的绘制
class TurtlePen():
    def __init__(self, canvas):
        self.screen = tt.TurtleScreen(canvas)
        #self.screen.screensize(100, 100) # Screen 大小决定绘图可视区域大小，当Screen 大小超出屏幕区域时，ScrolledCanvas会出现滚动条
        self.screen.bgcolor('black')
        self.screen.tracer(True)
        self.turtle = tt.RawTurtle(self.screen)
        self.turtle.speed(0)
        self.turtle.ht()
        self.turtle.color('white')
        self.turtle.up()
        self.turtle.goto(1100,-350)
        self.turtle.seth(0)
    
    # 绘制曲线
    def drawCurve(self):
        # 设置模型规则

        length = 100
        angle = 90
        path = 'Fl'
        rule = {
            'Fl':'Fl+Fr+',
            'Fr':'-Fl-Fr'
            }
        
        # 生成路径
        l = ls.Lsystem()
        n = 12 # 应用规则次数 [0,~]
        for i in range(n):
            path = l.apply_rule(rule,path)
        print(path)
            
        # 执行绘制
        l.draw(self.turtle, path, length/(1.2**n), angle, 1, 1, 1)



# 画布类
# 为turtle提供一个全屏的画布
class TurtleCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, bg='#000000', width=5000, height=3000)
        self.pack(fill='both', padx=0, pady=0)
        self.pen = TurtlePen(self) # 实例化一个海龟画板
        self.pen.drawCurve()

        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    root.attributes('-fullscreen', True) # 是否全屏显示
    root.attributes('-topmost', True) # 窗口置顶    
    root.attributes('-alpha', 0.4) # 窗口透明度[0,1]
    canvas = TurtleCanvas(root)
    root.mainloop()
