import tkinter
import CONF_APUNTO



path = CONF_APUNTO.logo_path
print(path)



root = tkinter.Tk()


logo = tkinter.PhotoImage(file = path)

w1 = tkinter.Label(root, text = "apunto")
w = tkinter.Label(root, image = logo)
w1.pack()
w.pack()

root.mainloop()
