# from musicdb import MusicDB
class Album:
    def __init__(self, name, db):
        self.name = name
        self.db = db

    def songs(self):
        return self.db.get_songs(self.name)