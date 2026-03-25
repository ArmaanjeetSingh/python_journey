class Artist:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def albums(self):
        return self.db.get_albums(self.name)

    def song_count(self):
        return self.db.count_songs_per_artist(self.name)

    def add_album(self, album_name):
        self.db.add_album(album_name, self.name)

    def songs(self):
        return self.db.get_songs_by_artist(self.name)