import tkinter as tk

root = tk.Tk()

root.title('My first gui')
root.geometry('300x200')

label = tk.Label(root,text='Hello Tkinter!')
label.pack()

root.mainloop()