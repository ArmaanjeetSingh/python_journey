import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

def login():
    username = name_entry.get()
    password = pass_entry.get()
    
    if username == 'armaan' and password == '12345':
        messagebox.showinfo("Login successful", "Verified")
    else:
        messagebox.showinfo("Invalid details", "Try again")

tk.Label(root,text='Username').grid(row=0,column=0, padx=10, pady=10)
tk.Label(root,text='Password').grid(row=1,column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
name_entry.grid(row=0,column=1)

pass_entry = tk.Entry(root)
pass_entry.grid(row=1,column=1)

tk.Button(root, text="Login",command=login).grid(row=2, column=0, columnspan=2)

root.mainloop()