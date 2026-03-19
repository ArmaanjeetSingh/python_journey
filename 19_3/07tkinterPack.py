import tkinter as tk 

root = tk.Tk()

root.title("Counter App")
root.geometry("300x200")

count = 0
label = tk.Label(root,text=str(count),font=('Arial',30))

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -=1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

frame = tk.Frame(root)
frame.pack()

btn_inc = tk.Button(frame, text="Increase", command=increase)
btn_inc.pack(side="left", padx=10)

btn_dec = tk.Button(frame, text="Decrease", command=decrease)
btn_dec.pack(side="left", padx=10)

btn_reset = tk.Button(frame, text="Reset", command=reset)
btn_reset.pack(side="left", padx=10)

label.pack()



root.mainloop()