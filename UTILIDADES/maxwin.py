import tkinter as tk

ST = [1]
def minwin(key):
    if ST[0]:
        win.attributes("-fullscreen", False)
        ST[0] = 0
        print('minwin', ST[0])
    else:
        win.attributes("-fullscreen", True)
        ST[0] = 1
        print('minwin', ST[0])


win = tk.Tk()
win.attributes('-fullscreen', True)
frame = tk.Frame(win)
frame.pack()
win.bind("<F11>", minwin)
win.mainloop()
