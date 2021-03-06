import tkinter as tk
import tkinter.messagebox
import math
import random
import time
import collections

num_font = ('Arial', 40)
num_btn_font = ('Arial', 16)
title_font = ('黑体', 40)
widget_font = ('宋体', 18)

# ========================数独类===========================
class NumberPlace():
    
    def __init__(self):
        global matrix
        matrix = [['' for col in range(9)] for row in range(9)]
        
    # 生成1-9随机数列表    
    def get_random_list(self):
        num_list = list(range(1,10))
        random.shuffle(num_list)
        return num_list
    
    # 随机数装填宫
    def random_fill_unit(self, unitNum, randomList):
        x_LT = 3*int((unitNum-1)/3) # 获得本宫左上角x坐标
        y_LT = (unitNum-1-x_LT)*3 # 获得本宫左上角y坐标
        x_RB = x_LT+2 # 获得本宫右下角x坐标
        y_RB = y_LT+2 # 获得本宫右下角y从标
        for i in range(x_LT, x_RB+1):
            for j in range(y_LT, y_RB+1):
                matrix[i][j] = randomList.pop()
    
    # 获得1-9宫数集
    def get_unit(self, unitNum):
        x_LT = 3*int((unitNum-1)/3) # 获得本宫左上角x坐标
        y_LT = (unitNum-1-x_LT)*3 # 获得本宫左上角y坐标
        x_RB = x_LT+2 # 获得本宫右下角x坐标
        y_RB = y_LT+2 # 获得本宫右下角y从标
        #print("unit: ", unitNum)
        #print("LTx, LTy, RBx, RBy", x_LT, y_LT, x_RB, y_RB)
        unitList = []
        for i in range(x_LT, x_RB+1):
            for j in range(y_LT, y_RB+1):
                if matrix[i][j]!='':
                    unitList.append(matrix[i][j])
        #print('current unit: ',unitList)
        return unitList
    
    # 获取当前坐标所在宫数集
    # currentRow 当前位置 x 坐标
    # currentCol 当前位置 y 坐标
    def get_current_unit(self, currentRow, currentCol):
        if currentRow<3 :
            if currentCol<3: # 第1宫
                return self.get_unit(1)                        
            elif currentCol<6: # 第2宫
                return self.get_unit(2)
            else: # 第3宫
                return self.get_unit(3)
        elif currentRow<6 :
            if currentCol<3: # 第4宫
                return self.get_unit(4)
            elif currentCol<6: # 第5宫
                return self.get_unit(5)
            else: # 第6宫
                return self.get_unit(6)
        elif currentRow<9 :
            if currentCol<3: # 第7宫
                return self.get_unit(7)
            elif currentCol<6: # 第8宫
                return self.get_unit(8)
            else: # 第9宫            
                return self.get_unit(9)
                
    # 清空矩阵      
    def clean(self):
        for i in range(9):
            for j in range(9):
                matrix[i][j] = ''
    
    # 重置数独矩阵
    # 按生成一个新的数独矩阵
    def reset(self, difficult):
        self.clean()
        self.backtracking(1)
        for i in range(9):
            for j in range(9):
                if random.randint(0,10) < difficult:
                    matrix[i][j]=''
        
    # 生成对角矩阵
    def makeCube():
        self.clean()
        self.random_fill_unit(1, self.get_random_list())
        self.random_fill_unit(5, self.get_random_list())
        self.random_fill_unit(9, self.get_random_list())
        return True#self.backtracking(1)
    
    # 生成候选集
    # 根据已知条件寻找i 行 j 列格子的候选数集
    def find_candidate_list(self, i, j):
        # 本行元素+本列元素+本宫元素
        exist_list = list(set(matrix[i] + [X[j] for X in matrix] + self.get_current_unit(i, j)))
        #print("exist_list: ", exist_list)
        return [k for k in range(1, 10) if k not in exist_list]
    
    # 验证单个元素num 是否可放 i, j 处
    # i,j 处还未放置该数
    def isLegal(self, num, i, j):
        if num in self.find_candidate_list(i, j):
            return True
        else:
            return False
    
    # 检验 i,j 处num值的合法性
    # i,j处已放置该数
    def isCorrect(self, num, i, j):
        # 判断行,列,
        x_dict = collections.Counter(matrix[i])
        y_dict = collections.Counter([X[j] for X in matrix])
        u_dict = collections.Counter(self.get_current_unit(i, j))
        #print('x,y,u dict: ',x_dict, y_dict, u_dict)
        if x_dict[num]==1 and y_dict[num]==1 and u_dict[num]==1:
            return True
        else:
            return False
    
    # 回溯求解
    # 递归算法
    # 参数: pos 求解起始位置，区间 [1, 81]
    # 返回：True 求解完成， False 求解失败
    def backtracking(self, pos):
        #print(" >>>>> ")
        while pos<82:
            i = int((pos-1)/9)
            j = (pos-1)%9
            #print('current row and col: ',i, j)
            if matrix[i][j] == '':
                candidate_list = self.find_candidate_list(i, j)
                #print("candidate:",candidate_list)
                while len(candidate_list)>0:
                    #matrix[i][j] = candidate_list.pop() # 固定求解，每次解出的答案均相同
                    matrix[i][j] = candidate_list.pop(random.randint(0,len(candidate_list)-1)) # 不定求解，从候选集中随机抽取
                    #print("candidate:",candidate_list)
                    #print(matrix)
                    #input()
                    if self.backtracking(pos+1): # 递归
                        #print("<<<< True") # 计算成功，逐级返回
                        return True;
                    matrix[i][j] = '' # 如果下层没有成功，则清除本次试值
                #print("<<<< False")
                return False
            else:
                pos+=1
        # end while
        #print("<<<< End")
        return True

        
    
# ===================应用程序类====================
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.mode = False # False--答题模式， True--解题模式
        
        self.np = NumberPlace() # 数独 成员对象
        self.create_widgets()
        
    def create_widgets(self):
        
        # ====左侧框架====
        frameLeft = tk.Frame(self)
        frameLeft.pack(side="left", fill="y")
        frameLeftTop = tk.Frame(frameLeft)
        frameLeftTop.pack(side="top", fill="x")
        frameLeftBottom = tk.Frame(frameLeft)
        frameLeftBottom.pack(side="bottom", fill="x", pady=5)
        # ----左上方数阵----
        validateCMD = frameLeftTop.register(self.cmd_validate) # 将响应函数注册到组件,这样才能使用 validatecommand=(validateCMD, '%P', i, j) 带参数的事件响应方法, 其中 %P是获取文本框中输入的内容
        self.entries = [[None for col in range(9)] for row in range(9)] # 生成空列表(二维)
        for i in range(9):
            for j in range(9):
                if (i in [3, 4, 5] and j not in [3, 4, 5]) or (j in [3, 4, 5] and i not in [3, 4, 5]):
                    entry = tk.Entry(frameLeftTop, width=2, font = num_font, justify='center', highlightcolor='#6666FF', highlightbackground="#6666FF", highlightthickness=4, validate = 'focusout', validatecommand=(validateCMD, '%P', i, j))
                else:
                    entry = tk.Entry(frameLeftTop, width=2, font = num_font, justify='center', highlightcolor='#66FF66', highlightbackground="#66FF66", highlightthickness=4, validate = 'focusout', validatecommand=(validateCMD, '%P', i, j))        
                entry.grid(row=i, column=j)
                entry.insert(0, matrix[i][j])
                self.entries[i][j] = entry 
        # ----左下方数表----
        #emphasizeCMD = frameLeftBottom.register(self.cmd_emphasize)
        #for i in range(1,10):
        #    btnNum = tk.Button(frameLeftBottom, text=str(i), width=2, height=1, padx=17, justify='center', font=num_btn_font, command=(emphasizeCMD, i))
        #    btnNum.pack(side="left", fill="y")
                

        
        # ====右侧框架====
        frameRight = tk.Frame(self)
        frameRight.pack(side="top", fill="y")
        
        # ----标题----
        #lab_title = tk.Label(frameRight, text="数独", font=title_font, width=8)
        #lab_title.pack(side="top", fill="x")
        #lab_title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # ----出题----
        lF_difficulty = tk.LabelFrame(frameRight, text="出题", width=200, font=widget_font, padx=5, pady=5)
        lF_difficulty.pack(side="top", fill="x")
        #lF_difficulty.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        # 难度单选框
        self.iv_dif = tk.IntVar() # 定义成员变量保存选项值
        self.iv_dif.set(1)

        rb_diff_0 = tk.Radiobutton(lF_difficulty, text="入门      ", variable=self.iv_dif, value=1, font=widget_font)
        rb_diff_0.pack()
        rb_diff_1 = tk.Radiobutton(lF_difficulty, text="容易      ", variable=self.iv_dif, value=3, font=widget_font)
        rb_diff_1.pack()
        rb_diff_2 = tk.Radiobutton(lF_difficulty, text="进阶      ", variable=self.iv_dif, value=5, font=widget_font)
        rb_diff_2.pack()
        rb_diff_3 = tk.Radiobutton(lF_difficulty, text="大师      ", variable=self.iv_dif, value=8, font=widget_font)
        rb_diff_3.pack()
        # 生成按钮
        btn_begin = tk.Button(lF_difficulty, text="生成题目", font=widget_font, command=self.cmd_generate)
        btn_begin.pack()
        # 验证结果
        btn_check = tk.Button(lF_difficulty, text="计算得分", font=widget_font, command=self.cmd_check)
        btn_check.pack()
        
        # ----解题----
        lF_resolve = tk.LabelFrame(frameRight, text="解题", font=widget_font, padx=5, pady=5)
        lF_resolve.pack(side="top", fill="x")
        #lF_resolve.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        # 清空按钮
        btn_resolve = tk.Button(lF_resolve, text="清空", font=widget_font, command=self.cmd_clean)
        btn_resolve.pack()           
 
        # 求解按钮
        btn_resolve = tk.Button(lF_resolve, text="求解", font=widget_font, command=self.cmd_resolve)
        btn_resolve.pack()
        
        # ----标注----
        lF_emphasize = tk.LabelFrame(frameRight, text="标注", font=widget_font, padx=10, pady=5)
        lF_emphasize.pack(side="top", fill="x")        
        
        # 数表
        emphasizeCMD = lF_emphasize.register(self.cmd_emphasize)
        for i in range(1,10):
            btnNum = tk.Button(lF_emphasize, text=str(i), width=2, height=1, padx=10, justify='center', font=num_btn_font, command=(emphasizeCMD, i))
            btnNum.grid(row=int((i-1)/3), column=(i-1)%3)
        
        # ----功能按钮组----
        frameEnd = tk.Frame(frameRight, padx=5, pady=8)
        frameEnd.pack(side="top", fill="x")
         
        # 退出按钮
        btn_quit = tk.Button(frameEnd, text="退出", font=widget_font, command=self.cmd_quit)
        btn_quit.pack(side="right")
        #btn_quit.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # 帮助按钮
        btn_help = tk.Button(frameEnd, text="帮助", font=widget_font, command=self.cmd_help)
        btn_help.pack(side="left")
        #btn_help.grid(row=3, column=0, columnspan=2, padx=5, pady=5)        
    
    # 事件响应函数：帮助
    def cmd_help(self):
        tk.messagebox.showinfo('帮助','《数独大师》v2.0\n欢迎使用，程序功能包括：生成数独题目和求解数独题目。\n\n1.出题\n请选择四种题目难度中的一种，然后点击生成题目按钮，答题过程中只能在空格内填入1-9的数字符号，填入其它内容无效。答题完成后请点击计算得分，程序会自动计时、判错、并给出一种参考得分。\n\n2.解题\n解题是一种自动求解数独的计算器，首先清空数格，然后手工填入已有的数据，点击求解按钮便可自动填写其它空格。手工填入数字时，每填写一项程序会自动检查所填数字是否符合数独规则')
    
    # 事件响应函数：在数阵中强调显示数字
    def cmd_emphasize(self, num):
        print('number: ',num)
        for i in range(9):
            for j in range(9):
                if matrix[i][j]==int(num):
                    print('Red: ',i,j)
                    self.entries[i][j]['fg']='#FF0000'
                else:
                    self.entries[i][j]['fg']='#000000'
        
    
    # 事件响应函数：计算得分
    def cmd_check(self):
        usetime = time.time()-self.starttime # 耗时
        wrongNum = 0 # 错题数
        for i in range(9):
            for j in range(9):
                if self.np.isCorrect(matrix[i][j], i, j):
                    continue
                else:
                    wrongNum+=1
        factor = self.iv_dif.get()/10 # 难度因子
        score = 100-int(usetime/(120*factor))-wrongNum # 得分计算方法
        print('use time: ',usetime,'  wrong: ',wrongNum,'  factor:', factor,'  score:',score)
        tk.messagebox.showinfo('检查结果', '耗时：'+str(round(usetime/60,1))+'分钟 \n错题数：'+str(wrongNum)+'\n得分：'+str(score))

    
    
    # 事件响应函数：清空数格
    def cmd_clean(self):
        self.np.clean()
        print(matrix)
        self.updateEntriesState(False)        
        self.updateEntries()
        self.mode = True # 答题模式设为 True，此时自动更正非法数字, 参见 cmd_validate 方法
        self.cmd_emphasize('0')
    
    # 事件响应函数：求解数独
    def cmd_resolve(self):
        self.updateMatrix()
        if self.np.backtracking(1): # 格子编号 1~81
            print("求解成功！")
            self.updateEntries()
        else:
            print("求解失败！")
        self.updateEntries()
     
    # 事件响应函数：生成题目
    def cmd_generate(self):
        self.starttime = time.time()
        self.np.reset(self.iv_dif.get())
        self.updateEntriesState(False)
        self.updateEntries()
        self.updateEntriesState(True)
        self.mode = False # 模式设为答题模式，不自动更正非法数字

    # 事件响应函数：退出程序
    def cmd_quit(self):
        self.master.destroy()
    
    # 事件响应函数：获取Entry输入并验证
    # correction 布尔值，是否自动纠错
    def cmd_validate(self, content, rowStr, colStr):
        rowNum = int(rowStr)
        colNum = int(colStr)
        if content.isdigit(): # 如果是数字和空值
            if int(content)>0 and int(content)<=9: # 如果是 [1,9] 区间
                if not self.mode: # 不验证合法性
                    matrix[rowNum][colNum] = int(content) # 更新文本框中的数字到矩阵
                elif self.np.isLegal(int(content), rowNum, colNum): # 验证输入是否合法
                    matrix[rowNum][colNum] = int(content) # 更新文本框中的数字到矩阵
                else:
                    self.replaceEntry(rowNum, colNum)
            else:
                self.replaceEntry(rowNum, colNum)
        elif content == '':
            matrix[rowNum][colNum] = ''
        else: # 用矩阵值恢复输入框原值
            self.replaceEntry(rowNum, colNum)

        print(matrix)
        return True
    
    # 从Entries更新数据到矩阵
    def updateMatrix(self):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].get() != '':
                    matrix[i][j] = int(self.entries[i][j].get())

    # 从矩阵更新数据到Entries
    # lock 是否锁定单元格
    def updateEntries(self):
        for i in range(9):
            for j in range(9):
                self.replaceEntry(i, j)
                
    # 更新Entries的显示状态
    # isLock: True 锁定有数字的格子，False 所有格子可编辑
    def updateEntriesState(self, isLock):
        for i in range(9):
            for j in range(9):
                self.entries[i][j]['state'] = 'normal'
                if isLock and matrix[i][j]!='' :
                    self.entries[i][j]['state'] = 'readonly'                
    
    # 在i行j列处更新 entry
    def replaceEntry(self, i, j):
        self.entries[i][j].delete(0, 100) # 删除数字
        self.entries[i][j].insert(0, matrix[i][j]) # 从矩阵更新的文本框
        

       

if __name__ == '__main__':
    root = tk.Tk()
    root.title("数独大师 v2.0")
    #root.geometry("900x710")
    root.iconbitmap("number.ico")
    app = Application(master=root)
    app.mainloop()