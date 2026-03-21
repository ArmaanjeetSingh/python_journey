import tkinter as tk 

mainWindow = tk.Tk()

mainWindow.title("Hello world")
mainWindow.geometry("640x400")

label = tk.Label(mainWindow,text = 'Hello World')
label.pack(side='top')

leftFrame = tk.Frame(mainWindow)
leftFrame.pack(side='left',anchor='n',fill=tk.Y,expand=False)

rightFrame = tk.Frame(mainWindow)
rightFrame.pack(side='right',anchor='w',expand=True)

button1 = tk.Button(rightFrame,text = 'button1')
button2 = tk.Button(rightFrame,text = 'button2')

canvas = tk.Canvas(mainWindow,relief='raised',borderwidth=1)
canvas.pack(side='top',fill=tk.Y,expand = True)

mainWindow.mainloop()