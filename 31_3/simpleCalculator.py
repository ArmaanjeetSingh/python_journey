import tkinter as tk
def add_nums():
    user_entry1 = int(entry1.get())
    user_entry2 = int(entry2.get())
    label3.config(text=f'{user_entry1+user_entry2} is your result')


root = tk.Tk()
root.title("Simple calculator")
root.geometry('300x200')
label1 = tk.Label(text="Enter first number")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(text="Enter second number")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
button1 = tk.Button(root,text='Add numbers',command=add_nums)
button1.pack()
label3 = tk.Label(text="Your result will be shown here")
label3.pack()
root.mainloop()