import tkinter as tk

def click(btn):
    print(f"{btn} clicked")

root = tk.Tk()
root.title("4 Button Grid")
root.geometry("200x150")


btn1 = tk.Button(root, text="Button 1", command=lambda: click("Button 1"))
btn2 = tk.Button(root, text="Button 2", command=lambda: click("Button 2"))
btn3 = tk.Button(root, text="Button 3", command=lambda: click("Button 3"))
btn4 = tk.Button(root, text="Button 4", command=lambda: click("Button 4"))


btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
