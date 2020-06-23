import tkinter as tk
import math
import random

num_font = ('Arial', 40)
title_font = ('黑体', 40)
widget_font = ('宋体', 16)

class NumberPlace():
    
    def __init__(self):
        global matrix
        matrix = [['' for col in range(9)] for row in range(9)]
        self.fill_unit(0, 0, self.get_random_list())
        self.fill_unit(3, 3, self.get_random_list())
        self.fill_unit(6, 6, self.get_random_list())
        
        
    def get_random_list(self):
        num_list = list(range(1,10))
        random.shuffle(num_list)
        return num_list
    
    def fill_unit(self, indexRow, indexCol, randomList):
        for i in range(indexRow, indexRow+3):
            for j in range(indexCol, indexCol+3):
                matrix[i][j] = randomList.pop()
    

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.np = NumberPlace()
        self.create_widgets()
        
    def create_widgets(self):
        
        # 左侧框架
        frameLeft = tk.Frame(self)
        frameLeft.pack(side="left", fill="y")
        validateCMD = frameLeft.register(self.cmd_validate) # 将响应函数注册到组件
        self.entries = [[None for col in range(9)] for row in range(9)] # 生成空列表(二维)
        for i in range(81):
            rowNum = int(i/9) # 行号
            colNum = (i-1)%9 # 列号
            entry = tk.Entry(frameLeft, width=2, font = num_font, justify='center', validate = 'focusout', validatecommand=(validateCMD, '%P', rowNum, colNum))
            entry.grid(row=rowNum, column=colNum)
            entry.insert(0, matrix[rowNum][colNum])
            self.entries[rowNum][colNum] = entry

        
        # 右侧框架
        frameRight = tk.Frame(self)
        frameRight.pack(side="top", fill="y")
        
        # 标题
        lab_title = tk.Label(frameRight, text="数独", font=title_font, width=8)
        lab_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # 难度
        lF_difficulty = tk.LabelFrame(frameRight, text="难度", width=200, font=widget_font)
        lF_difficulty.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        self.iv_dif = tk.IntVar() # 定义成员变量保存选项值
        self.iv_dif.set(1)
        rb_diff_0 = tk.Radiobutton(lF_difficulty, text="入门", variable=self.iv_dif, value=1, font=widget_font)
        rb_diff_0.pack()
        rb_diff_1 = tk.Radiobutton(lF_difficulty, text="容易", variable=self.iv_dif, value=2, font=widget_font)
        rb_diff_1.pack()
        rb_diff_2 = tk.Radiobutton(lF_difficulty, text="进阶", variable=self.iv_dif, value=3, font=widget_font)
        rb_diff_2.pack()
        rb_diff_3 = tk.Radiobutton(lF_difficulty, text="大师", variable=self.iv_dif, value=4, font=widget_font)
        rb_diff_3.pack()
        
        # 生成按钮
        btn_begin = tk.Button(frameRight, text="生成", font=widget_font, command=self.cmd_generate)
        btn_begin.grid(row=3, column=0, padx=5, pady=5)
        
        # 退出按钮
        btn_quit = tk.Button(frameRight, text="退出", font=widget_font, command=self.cmd_quit)
        btn_quit.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def cmd_generate(self):
        self.np = NumberPlace()
        self.updateEntries()

        
    def cmd_quit(self):
        self.master.destroy()
    
    # 事件响应函数：验证entry框输入
    def cmd_validate(self, content, rowStr, colStr):
        rowNum = int(rowStr)
        colNum = int(colStr)
        if content.isdigit(): # 如果是数字
            if int(content)>0 and int(content)<=9: # 如果是 [1,9] 区间
                matrix[rowNum][colNum] = int(content) # 更新文本框中的数字到矩阵
            else:
                self.replaceEntry(rowNum, colNum)
        else:
            self.replaceEntry(rowNum, colNum)

        print(matrix)
        return True

    def updateEntries(self):
        for i in range(9):
            for j in range(9):
                self.replaceEntry(i, j)
                
    def replaceEntry(self, i, j):
        self.entries[i][j].delete(0, 100) # 删除数字
        self.entries[i][j].insert(0, matrix[i][j]) # 从矩阵更新的文本框
       

if __name__ == '__main__':
    root = tk.Tk()
    root.title("欢迎光临数独游戏")
    #root.geometry("900x710")
    root.iconbitmap("number.ico")
    app = Application(master=root)
    app.mainloop()