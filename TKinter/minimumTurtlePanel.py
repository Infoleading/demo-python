import tkinter as tk
import turtle as tt

# 画板类
# 请在此类中添加各种形状的绘制
class Panel():
    def __init__(self, canvas):
        self.screen = tt.TurtleScreen(canvas)
        self.screen.screensize(100, 100) # Screen 大小决定绘图可视区域大小，当Screen 大小超出屏幕区域时，ScrolledCanvas会出现滚动条
        self.screen.bgcolor('grey')
        self.screen.tracer(False)
        self.turtle = tt.RawTurtle(self.screen)
        self.turtle.ht()
        
    # 画三角形
    def drawTriangle(self):
        self.turtle.circle(100, 360, 3)
        self.screen.update()

# 应用类
# 应用程序框架，为画板方法提供人机接口
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=5, pady=5)
        self.create_widgets()
        self.panel = Panel(self.canvas) # 实例化一个画板
        
    def create_widgets(self):
        
        # 面板：功能
        frameFunction = tk.Frame(self, width=500)
        frameFunction.pack(side='left', fill='both')
        
        # 画布
        # 画布大小决定窗口大小，超出屏幕区域时不会出现滚动条
        self.canvas = tt.ScrolledCanvas(self, width=10000, height=10000)
        self.canvas.pack(side='right', fill='y')
        
        # 按钮：画三角形
        self.btn_draw_trangle = tk.Button(frameFunction, text='画三角形', command=self.cmd_draw_trangle)
        self.btn_draw_trangle.pack(side="top", fill='both')
        
        # 按钮：退出
        self.btn_quit = tk.Button(frameFunction, text='退出', command=self.cmd_quit)
        self.btn_quit.pack(side="bottom", fill='x')

    # 事件响应：画三角形
    def cmd_draw_trangle(self):
        self.panel.drawTriangle()
        
    # 事件响应：退出
    def cmd_quit(self):
        self.master.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    root.attributes('-fullscreen', True) # 是否全屏显示
    root.attributes('-alpha', 1) # 窗口透明度[0,1]
    root.geometry("1000x600") # 非全屏下窗口大小
    app = Application(master=root)
    app.mainloop()
