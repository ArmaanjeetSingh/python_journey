import tkinter as tk 

def login():
    if username.get() == 'admin' and password.get()=='1234':
        result.config(text='Successful Login')
    else:
        result.config(text='Invalid credentials')

root = tk.Tk()

tk.Label(root,text='Username').pack()
username = tk.Entry(root)
username.pack()

tk.Label(root,text='Password').pack()
password = tk.Entry(root,show='*')
password.pack()

tk.Button(root,text='Click me',command=login).pack()
result = tk.Label(root, text="")
result.pack()
root.mainloop()