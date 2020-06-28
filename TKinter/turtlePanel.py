import tkinter as tk
import turtle as tt

class Panel():
    def __init__(self, canvas):
        self.screen = tt.TurtleScreen(canvas)
        self.path = tt.RawTurtle(self.screen)
    
    def drawTriangle(self):
        self.path.circle(100, 360, 3)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.panel = Panel(self.canvas)
        
    def create_widgets(self):
        
        framePanel = tk.Frame(self, width=200, height=800, highlightbackground='#FF0000', highlightcolor='#FF0000', highlightthickness=1, )
        framePanel.pack(side='left', fill='y')
        
        frameCanvas = tk.Frame(self, width=1000, height=800, highlightbackground='#FF0000', highlightcolor='#FF0000', highlightthickness=1, )
        frameCanvas.pack(side='right', fill='y')
        
        self.canvas = tk.Canvas(frameCanvas, width=1000, height=800, bg='#000000')
        self.canvas.pack()
        
        self.btn_shape_trangle = tk.Button(framePanel, text='画三角形', command=self.cmd_shape_trangle)
        self.btn_shape_trangle.pack(side="top", fill='y')
        
    def cmd_quit(self):
        self.master.destroy()
        
    def cmd_shape_trangle(self):
        self.panel.drawTriangle()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    #root.geometry("1400x900")
    app = Application(master=root)
    app.mainloop()
