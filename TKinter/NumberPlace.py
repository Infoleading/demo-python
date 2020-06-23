import tkinter as tk
import math
import random

num_font = ('Arial', 40)
title_font = ('黑体', 40)
widget_font = ('宋体', 20)
PINK = (4,2,2)

# 数独类
class NumberPlace():
    
    def __init__(self):
        global matrix
        matrix = [['' for col in range(9)] for row in range(9)]
        self.fill_unit(0, 0, self.get_random_list())
        self.fill_unit(3, 3, self.get_random_list())
        self.fill_unit(6, 6, self.get_random_list())
        self.candidates = [['' for col in range(9)] for row in range(9)]
        
    # 生成1-9随机数列表    
    def get_random_list(self):
        num_list = list(range(1,10))
        random.shuffle(num_list)
        return num_list
    
    # 随机数装填宫
    def fill_unit(self, indexRow, indexCol, randomList):
        for i in range(indexRow, indexRow+3):
            for j in range(indexCol, indexCol+3):
                matrix[i][j] = randomList.pop()
    # 清空矩阵      
    def clean(self):
        for i in range(9):
            for j in range(9):
                matrix[i][j] = ''
    
    # 重置矩阵
    def reset(self):
        self.clean()
        self.fill_unit(0, 0, self.get_random_list())
        self.fill_unit(3, 3, self.get_random_list())
        self.fill_unit(6, 6, self.get_random_list())
    
    # 生成候选集
    # 根据已知条件寻找i 行 j 列格子的候选数集
    def find_candidate_list(self, i, j):
        exist_list = matrix[i] + [X[j] for X in matrix]
        return [k for k in range(1, 10) if k not in exist_list]
    
    # 回溯求解
    def backtracking(self, pos):
        if pos<82:
            i = int(pos/9)
            j = (pos-1)%9
            if matrix[i][j] == '':
                candidate_list = self.find_candidate_list(i, j)
                while len(candidate_list)>0:
                    matrix[i][j] = candidate_list.pop()
                    print(matrix)
                    if self.backtracking(pos+1):
                        return True;
                return False
            else:
                self.backtracking(pos+1)
        else:
            return True

        
    
# 应用程序类
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.np = NumberPlace() # 数独 成员对象
        self.create_widgets()
        
    def create_widgets(self):
        
        # ====左侧框架====
        frameLeft = tk.Frame(self)
        frameLeft.pack(side="left", fill="y")
        validateCMD = frameLeft.register(self.cmd_validate) # 将响应函数注册到组件
        self.entries = [[None for col in range(9)] for row in range(9)] # 生成空列表(二维)
        for i in range(9):
            for j in range(9):
                if (i in [3, 4, 5] and j not in [3, 4, 5]) or (j in [3, 4, 5] and i not in [3, 4, 5]):
                    entry = tk.Entry(frameLeft, width=2, font = num_font, justify='center', bg='#FFEEEE', validate = 'focusout', validatecommand=(validateCMD, '%P', i, j))
                else:
                    entry = tk.Entry(frameLeft, width=2, font = num_font, justify='center', bg='#EEFFEE', validate = 'focusout', validatecommand=(validateCMD, '%P', i, j))        
                entry.grid(row=i, column=j)
                entry.insert(0, matrix[i][j])
                self.entries[i][j] = entry

        
        # ====右侧框架====
        frameRight = tk.Frame(self)
        frameRight.pack(side="top", fill="y")
        
        # ====标题====
        lab_title = tk.Label(frameRight, text="数独", font=title_font, width=8)
        lab_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # ====出题====
        lF_difficulty = tk.LabelFrame(frameRight, text="出题", width=200, font=widget_font)
        lF_difficulty.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        self.iv_dif = tk.IntVar() # 定义成员变量保存选项值
        self.iv_dif.set(1)
        # 难度单选框
        rb_diff_0 = tk.Radiobutton(lF_difficulty, text="入门", variable=self.iv_dif, value=1, font=widget_font)
        rb_diff_0.pack()
        rb_diff_1 = tk.Radiobutton(lF_difficulty, text="容易", variable=self.iv_dif, value=2, font=widget_font)
        rb_diff_1.pack()
        rb_diff_2 = tk.Radiobutton(lF_difficulty, text="进阶", variable=self.iv_dif, value=3, font=widget_font)
        rb_diff_2.pack()
        rb_diff_3 = tk.Radiobutton(lF_difficulty, text="大师", variable=self.iv_dif, value=4, font=widget_font)
        rb_diff_3.pack()   
        # 生成按钮
        btn_begin = tk.Button(lF_difficulty, text="     生成题目     ", font=widget_font, command=self.cmd_generate)
        btn_begin.pack()
        
        # ====解题====
        lF_resolve = tk.LabelFrame(frameRight, text="解题", font=widget_font)
        lF_resolve.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        # 清空按钮
        btn_resolve = tk.Button(lF_resolve, text="     清    空     ", font=widget_font, command=self.cmd_clean)
        btn_resolve.pack()           
 
        # 求解按钮
        btn_resolve = tk.Button(lF_resolve, text="     开始求解     ", font=widget_font, command=self.cmd_resolve)
        btn_resolve.pack()        
        
        # ====退出按钮====
        btn_quit = tk.Button(frameRight, text="退出", font=widget_font, command=self.cmd_quit)
        btn_quit.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    # 事件响应函数：清空数格
    def cmd_clean(self):
        self.np.clean()
        print(matrix)
        self.updateEntries()
        pass
    
    # 事件响应函数：求解数独
    def cmd_resolve(self):
        if self.np.backtracking(1): # 格子编号 1~81
            print("求解成功！")
            self.updateEntries()
        else:
            print("求解失败！")
     
    # 事件响应函数：生成数独
    def cmd_generate(self):
        self.np.reset()
        self.updateEntries()

    # 事件响应函数：退出程序
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

    # 从矩阵更新数据到Entries
    def updateEntries(self):
        for i in range(9):
            for j in range(9):
                self.replaceEntry(i, j)
    
    # 在i行j列处更新 entry
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