import tkinter as tk
import turtle as tt
import Lsystem as ls
import time

# L系统类
class Lsystem():
    def __init__(self):
        self.run = True
        
    def draw(self, turtle, path, length, angle):
        for symbol in path:
            if self.run == False:
                return
            elif symbol == 'F':
                turtle.down()
                turtle.fd(length)
            elif symbol == '+':
                turtle.rt(angle)
            elif symbol == '-':
                turtle.lt(angle)
    
    def gen(self, path, rule, n):
        for i in range(n):
            path = path.replace('F', rule)
        return path

# 海龟画板类
class TurtlePen():
    def __init__(self, canvas):
        self.screen = tt.TurtleScreen(canvas)
        self.screen.bgcolor('black')
        self.screen.tracer(True)
        self.turtle = tt.RawTurtle(self.screen)
        self.turtle.speed(0)
        self.turtle.ht()
        self.turtle.color('white')
        self.turtle.up()
        self.turtle.goto(0,0)
        self.turtle.seth(0)
    
    # 绘制曲线
    def drawCurve(self):
        # 设置模型规则
        length = 20
        angle = 90
        path = 'F-F-F-F'
        rule = 'FF-F+F-F-FF'
        # 生成路径
        self.l = Lsystem()
        path = self.l.gen(path, rule, 5)
        # 执行绘制
        self.l.draw(self.turtle, path, length, angle)
    
    def stopDraw(self):
        self.l.run = False


# 画布类
class TurtleCanvas(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, bg='#000000', width=3000, height=3000)
        self.bind('<Motion>', self.cmd_motion)
        self.pack(fill='both', padx=0, pady=0)
        self.pen = TurtlePen(self)
        self.pen.drawCurve()
        
    def cmd_motion(self, event):
        self.pen.stopDraw()
        self.master.destroy()        

        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)   
    root.attributes('-alpha', 0.4)
    canvas = TurtleCanvas(root)
    canvas.mainloop()
