import tkinter as tk
import turtle as tt

# 画板类
# 请在此类中添加各种形状的绘制
class Panel():
    def __init__(self, canvas):

        self.screen = tt.TurtleScreen(canvas)
        self.screen.screensize(3000, 3000) # Screen 大小决定绘图可视区域大小，当Screen 大小超出屏幕区域时，ScrolledCanvas会出现滚动条
        self.screen.bgcolor('#FF0000')
        self.screen.tracer(True)
        self.path = tt.RawTurtle(self.screen)
        
    # 画三角形
    def drawTriangle(self):
        self.path.circle(100, 360, 3)
        self.screen.update()

# 应用类
# 应用程序框架，为画板方法提供人机接口
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.panel = Panel(self.canvas) # 实例化一个画板
        
    def create_widgets(self):
        
        # 功能面板
        frameFunction = tk.Frame(self, width=200, height=800, highlightbackground='#FF0000', highlightcolor='#FF0000', highlightthickness=1, )
        frameFunction.pack(side='left', fill='y')
        
        # 画布面板
        self.frameCanvas = tk.Frame(self, highlightbackground='#FF0000', highlightcolor='#FF0000', highlightthickness=1, )
        self.frameCanvas.pack(side='right', fill='y')
        
        # 画布
        # 画布大小决定窗口大小，超出屏幕区域时不会出现滚动条
        self.canvas = tt.ScrolledCanvas(self.frameCanvas, width=1200, height=800)
        self.canvas.pack()
        
        # 按钮：画三角形
        self.btn_draw_trangle = tk.Button(frameFunction, text='画三角形', command=self.cmd_draw_trangle)
        self.btn_draw_trangle.pack(side="top", fill='y')

    # 事件响应：画三角形
    def cmd_draw_trangle(self):
        self.panel.drawTriangle()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    #root.geometry("1400x900")
    app = Application(master=root)
    app.mainloop()
