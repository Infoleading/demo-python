import  tkinter as ttk
from tkinter import *


root = ttk.Tk()
maxtick = 1000

frame = ttk.Frame(root)     # , padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

inner_frame = ttk.Frame(frame)
inner_frame.grid(column=0, row=0, sticky=(N, W, E, S))
inner_frame.columnconfigure(0, weight=1)
inner_frame.rowconfigure(0, weight=1)

# Primary canvas (inner_frame)
canvas = Canvas(inner_frame, bg='#FFF', width=maxtick,
                scrollregion=(0, 0, maxtick, 16 * (128 + 1 + 1)) )
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

for y in range(1, 128 + 1 + 1):
    canvas.create_line(0, 16 * y - 1, maxtick, 16 * y - 1)

# Vertical scrollbar
vbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
vbar.grid(column=1, row=0, sticky=(N, W, E, S))
canvas.configure(yscrollcommand=vbar.set)

# canvas.create_line(10, 10, 200, 50)

root.mainloop()