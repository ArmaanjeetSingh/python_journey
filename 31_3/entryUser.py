import tkinter as tk 
def show_text():
    user_entry = entry.get()
    label.config(text=f'You entered {user_entry}')
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,text='Submit',command=show_text)
button.pack()

label = tk.Label(root,text='')
label.pack()
root.mainloop()