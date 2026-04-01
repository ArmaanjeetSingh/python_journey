import tkinter as tk 
from tkinter import messagebox
def show_info():
    messagebox.showinfo('Info','Good info')
root = tk.Tk()

tk.Label(root,text='Name').grid(row=0,column=0)
tk.Entry(root).grid(row=0,column=1)

tk.Label(root,text='Age').grid(row=1,column=0)
tk.Entry(root).grid(row=1,column=1)

tk.Button(root,text='Submit',command=show_info).grid(row=2,column=0,columnspan=2)

tk.Label(root,text='Show result').grid(row=0,column=1)
root.mainloop()