import sqlite3
conn = sqlite3.connect("music.db")

def get_albums(event):
    lb = event.widget
    if not lb.curselection():
        return

    index = lb.curselection()[0]
    artist_name = lb.get(index)

    artist_id = conn.execute(
        "SELECT _id FROM artists WHERE name=?",
        (artist_name,)
    ).fetchone()

    if artist_id:
        alist = []
        for row in conn.execute(
            "SELECT name FROM albums WHERE artist=? ORDER BY name",
            (artist_id[0],)
        ):
            alist.append(row[0])

        albumLV.set(tuple(alist))

conn.close()