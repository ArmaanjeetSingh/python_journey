import sqlite3
from artist import Artist
from album import Album

class MusicDB:

    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)

    def get_artists(self):
        cursor = self.conn.execute("SELECT name FROM artists ORDER BY name LIMIT 10")
        return [row[0] for row in cursor]

    def get_albums(self,artist_name):
        artist_id = self.conn.execute("SELECT _id FROM artists WHERE name = ?",(artist_name,)).fetchone()
        if artist_id:
            cursor = self.conn.execute(
            "SELECT name FROM albums WHERE artist = ? ORDER BY name",(artist_id[0],))
            return [row[0] for row in cursor]
        return []


    def get_songs(self,album_name):
        album_id = self.conn.execute("SELECT _id FROM albums WHERE name = ?",(album_name,)).fetchone()
        if album_id:
            cursor = self.conn.execute("SELECT title FROM songs WHERE album = ? ORDER BY track",(album_id[0],))
            return [row[0] for row in cursor]
        return []

    def add_artist(self, name):
        self.conn.execute(
        "INSERT INTO artists (name) VALUES (?)",
        (name,))
        self.conn.commit()

    def add_album(self,album_name,artist_name):
        artist_id = self.conn.execute(
            "SELECT _id FROM artists WHERE name=?",
            (artist_name,)
        ).fetchone()
        if artist_id:
            self.conn.execute(
                "INSERT INTO albums (name,artist) VALUES(?,?)",
                (album_name,artist_id[0])
            )
            self.conn.commit()

    def count_songs_per_artist(self,artist_name):
        cursor = self.conn.execute("""
        SELECT COUNT(*)
        FROM songs s
        JOIN albums a ON a._id = s.album
        JOIN artists ar ON ar._id = a.artist
        WHERE ar.name = ?
         """,(artist_name,))
        return cursor.fetchone()[0]

    def get_songs_by_artist(self,artist_name):
        cursor = self.conn.execute("""
        SELECT ar.name,s.title,s.track
        FROM songs s
        JOIN albums a ON a._id = s.album
        JOIN artists ar ON ar._id = a.artist
        WHERE ar.name = ?
         """,(artist_name,))
        return [(row[0],row[1]) for row in cursor]


if __name__ == '__main__':
    db = MusicDB("music.db")
    print(db.get_artists())
    print(db.get_albums("Allan Holdsworth"))
    print(db.get_songs("All Night Wrong"))

    artist = Artist("Allan Holdsworth", db)
    print(artist.albums())
    print(artist.song_count())
    artist.songs()

    # album = Album("All Night Wrong", db)
    # print(album.songs())
    # print(db.count_songs_per_artist("Allan Holdsworth"))