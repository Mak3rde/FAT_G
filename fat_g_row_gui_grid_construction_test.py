from tkinter import *

root = Tk()

root.geometry("1500x1000")


emptybox_001 = 25, 25

btn_column = Button(root, text="I'm in column 1")
btn_column.grid(column=0)

image.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)

btn_column = Button(root, text="I'm in column 3")
btn_column.grid(column=2)

root.mainloop()