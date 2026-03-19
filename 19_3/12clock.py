import tkinter as tk
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)

    clock_label.after(1000, update_clock)


root = tk.Tk()
root.title("Clock App")
root.geometry("300x200")

clock_label = tk.Label(root, text="", font=("Arial", 30))
clock_label.pack(pady=50)
update_clock()
root.mainloop()