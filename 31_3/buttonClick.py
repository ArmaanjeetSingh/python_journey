import tkinter as tk  

def on_click():
    label.config(text="Button Clicked!")
root = tk.Tk()
root.title('Button Example')


label = tk.Label(root,text='Click the button')
label.pack()

button = tk.Button(root,text="Click Me",command=on_click)

root.mainloop()