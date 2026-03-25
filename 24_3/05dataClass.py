import sqlite3
import tkinter as tk
from scrollbox import Scrollbox

conn = sqlite3.connect("music.db")


# ---------- FUNCTIONS ----------

def get_albums(event):
    if not artistList.curselection():
        return

    index = artistList.curselection()[0]
    artist_name = artistList.get(index)

    artist_id = conn.execute(
        "SELECT _id FROM artists WHERE name=?",
        (artist_name,)
    ).fetchone()

    if artist_id:
        albums = []
        for row in conn.execute(
            "SELECT name FROM albums WHERE artist=? ORDER BY name",
            (artist_id[0],)
        ):
            albums.append(row[0])

        albumLV.set(tuple(albums))
        songsLV.set(("Choose Album",))   # reset songs


def get_songs(event):
    if not albumList.curselection():
        return

    index = albumList.curselection()[0]
    album_name = albumList.get(index)

    album_id = conn.execute(
        "SELECT _id FROM albums WHERE name=?",
        (album_name,)
    ).fetchone()

    if album_id:
        songs = []
        for row in conn.execute(
            "SELECT title FROM songs WHERE album=? ORDER BY track",
            (album_id[0],)
        ):
            songs.append(row[0])

        songsLV.set(tuple(songs))


# ---------- UI ----------

mainWindow = tk.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

# grid config
for i in range(3):
    mainWindow.columnconfigure(i, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=1)


# labels
tk.Label(mainWindow, text='Artists').grid(row=0, column=0)
tk.Label(mainWindow, text='Albums').grid(row=0, column=1)
tk.Label(mainWindow, text='Songs').grid(row=0, column=2)


# ---------- LISTBOXES ----------

# Artists
artistList = Scrollbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', padx=(30, 0))
artistList.config(border=2, relief='sunken')

# Albums
albumLV = tk.StringVar()
albumLV.set(("Choose Artist",))

albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# Songs
songsLV = tk.StringVar()
songsLV.set(("Choose Album",))

songsList = Scrollbox(mainWindow, listvariable=songsLV)
songsList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songsList.config(border=2, relief='sunken')


# ---------- BIND EVENTS ----------
artistList.bind('<<ListboxSelect>>', get_albums)
albumList.bind('<<ListboxSelect>>', get_songs)


# ---------- LOAD DATA ----------
for row in conn.execute("SELECT name FROM artists ORDER BY name"):
    artistList.insert(tk.END, row[0])


# ---------- MAIN LOOP ----------
mainWindow.mainloop()
conn.close()