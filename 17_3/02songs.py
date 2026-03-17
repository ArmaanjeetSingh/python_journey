class Song:
    """Class to represent a song"""

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album"""

    def __init__(self, name, year, artist):
        self.name = name
        self.year = year
        self.artist = artist
        self.tracks = []

    def add_song(self, song):
        """Add song to album if it doesn't already exist"""
        song_found = find_object(song.title, self.tracks)

        if song_found is None:
            self.tracks.append(song)
        else:
            print("Song {} already exists".format(song.title))


class Artist:
    """Class to store artist details"""

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add album if it doesn't already exist"""
        album_found = find_object(album.name, self.albums)

        if album_found is None:
            self.albums.append(album)
            return album
        else:
            return album_found

    def add_song(self, album_name, year, song_title):
        """Add a song to an album"""
        album_found = find_object(album_name, self.albums)

        if album_found is None:
            album_found = Album(album_name, year, self)
            self.albums.append(album_found)

        new_song = Song(song_title, self)
        album_found.add_song(new_song)


def find_object(field, object_list):
    """Find object in list using its name/title"""
    for item in object_list:
        if hasattr(item, "name") and item.name == field:
            return item
        elif hasattr(item, "title") and item.title == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip("\n").split('\t')
            )

            year_field = int(year_field)

            print("{}:{}:{}:{}".format(
                artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file to verify data"""

    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(
                        "{0.name}\t{1.name}\t{1.year}\t{2.title}".format(
                            new_artist, new_album, new_song),
                        file=checkfile
                    )


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)