import tkinter as tk

root = tk.Tk()
root.title("To-Do App")
root.geometry("300x250")

taskList = []

frame = tk.Frame(root)
frame.pack(pady=10)

def read_from_entry():
    text = entry.get()
    if text != "":
        taskList.append(text)
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)  

def delete_task():
    listbox.delete(tk.ACTIVE)

entry = tk.Entry(frame)
entry.pack()

btn = tk.Button(frame, text="Add Task", command=read_from_entry)
btn.pack(pady=5)

tk.Button(root, text="Delete", command=delete_task).pack()

listbox = tk.Listbox(root)
listbox.pack(pady=10)

root.mainloop()