from Tkinter import *
#from Tkinter import messagebox

top = Tk()
top.geometry("{0}x{1}+0+0".format(top.winfo_screenwidth(), top.winfo_screenheight()))

t1 = Button(top, text = "", bg = "Yellow")
t1.place(x = 50, y = 50)

top.mainloop()
