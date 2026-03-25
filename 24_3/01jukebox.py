import sqlite3
from scrollbox import Scrollbox
from get_albums import get_albums

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect("music.db")

mainWindow = tk.Tk()
mainWindow.title("Muisc DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0,weight=2)
mainWindow.columnconfigure(1,weight=2)
mainWindow.columnconfigure(2,weight=2)
mainWindow.columnconfigure(3,weight=1)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=5)
mainWindow.rowconfigure(2,weight=5)
mainWindow.rowconfigure(3,weight=1)


#-----labels------
tk.Label(mainWindow,text='Artists').grid(row=0,column=0)
tk.Label(mainWindow,text='Albums').grid(row=0,column=1)
tk.Label(mainWindow,text='Songs').grid(row=0,column=2)


#----Artists Listbox---
artistList = Scrollbox(mainWindow)
artistList.grid(row=1,column=0,sticky='nsew',pady=2,padx=(30,0))
artistList.config(border=2,relief='sunken')

artistScroll = tk.Scrollbar(mainWindow,orient=tk.VERTICAL,command=artistList.yview)
artistScroll.grid(row=1,column=0,sticky='nse',rowspan=2)
artistList.config(yscrollcommand=artistScroll.set)

for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artistList.insert(tk.END,artist[0])

artistList.bind('<<ListboxSelect>>',get_albums)


#----Album Listbox---
albumLV = tk.Variable(mainWindow)
albumLV.set(("Choose Artist",))
albumList = Scrollbox(mainWindow,listvariable=albumLV)
albumList.grid(row=1,column=1,sticky='nsew',padx=(30,0))
albumList.config(border=2,relief='sunken')

albumScroll = tk.Scrollbar(mainWindow,orient=tk.VERTICAL,command=albumList.yview)
albumScroll.grid(row=1,column=0,sticky='nse',rowspan=2)
albumList.config(yscrollcommand=albumScroll.set)



#-----Song Listbox----
songsLV = tk.Variable(mainWindow)
songsLV.set(("Choose Album",))
songsList = Scrollbox(mainWindow,listvariable=songsLV)
songsList.grid(row=1,column=2,sticky='nsew',padx=(30,0))
songsList.config(border=2,relief='sunken')

#-----Mainloop------
testList = range(0,100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
conn.close()