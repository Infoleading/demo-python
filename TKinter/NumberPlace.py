import tkinter as tk

num_font = ('Arial', 40)
title_font = ('黑体', 40)
widget_font = ('宋体', 20)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        
        frameGrid = tk.Frame()
        frameGrid.pack(side="left", fill="y")
        global entries
        entries = [[0 for col in range(9)] for row in range(9)]
        for i in range(81):
            entries[int(i/9)][(i-1)%9] = tk.Entry(frameGrid, width=2, font = num_font, textvariable=tk.StringVar().set(str(i)))
            entries[int(i/9)][(i-1)%9].grid(row=int(i/9), column=(i-1)%9)
        
        frameForm = tk.Frame()
        frameForm.pack(side="left", fill="y")      
        lab_title = tk.Label(frameForm, text="设置", font=title_font)
        lab_title.pack(side="top")
        btn_begin = tk.Button(frameForm, text="生成", font=widget_font)
        btn_begin.pack(side='top')
        btn_quit = tk.Button(frameForm, text="退出", font=widget_font, command=self.cmd_quit)
        btn_quit.pack(side="bottom")

        
    def cmd_quit(self):
        self.master.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("欢迎光临数独游戏")
    root.geometry("900x710")
    root.iconbitmap("number.ico")
    app = Application(master=root)
    app.mainloop()