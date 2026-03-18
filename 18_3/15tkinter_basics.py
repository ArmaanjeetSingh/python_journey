# import tkinter as tk 
# root = tk.Tk()
# root.title("My App")

# label = tk.Label(root,text='Hello world !')
# label.pack()

# btn1 = tk.Button(root,text='Top')
# btn1.pack(side='top',fill='x')
# btn2 = tk.Button(root,text='Bottom')
# btn2.pack(side='bottom')
# btn3 = tk.Button(root,text='left')
# btn3.pack(side='left',fill='y')
# btn4 = tk.Button(root, text="Right")
# btn4.pack(side="right",fill='both')
# btn = tk.Button(root, text="Click", padx=20, pady=10)
# btn.pack(expand=True,anchor='e')
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

btn1 = tk.Button(root, text="Top")
btn1.pack(side="top", fill="x")

btn2 = tk.Button(root, text="Left")
btn2.pack(side="left", fill="y")

btn3 = tk.Button(root, text="Right")
btn3.pack(side="right", fill="y")

btn4 = tk.Button(root, text="Center")
btn4.pack(expand=True)

root.mainloop()