import Tkinter as tk

main = tk.Tk()
canvas1 = tk.Canvas(main, width=800, height=100, bg='white')
canvas1.pack(side=LEFT)
label = tk.Label(canvas1, text='hai', bg='black')
tk.mainloop()
