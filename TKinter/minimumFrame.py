import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.btn_Quit = tk.Button(self)
        self.btn_Quit["text"] = "Quit"
        self.btn_Quit["command"] = self.cmd_quit
        self.btn_Quit.pack(side="bottom")
        
    def cmd_quit(self):
        self.master.destroy()
        

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello world")
    root.geometry("800x600")
    app = Application(master=root)
    app.mainloop()