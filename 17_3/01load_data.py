class Song:
    """Class to represent a song
    Attributes:
        title (str):The title of song
        artist (Artist): An artist object representing the songs creator
        duration (int):The duration of song in seconds
    """    

    def __init__(self,title,artist,duration =0):
        """Song init method

        Args:
            title (str): title of song
            artist (Artist): An artist object representing song creatir
            duration (int, optional): The duration of song in seconds. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent Album using its track list

    Attributes:
    album_name (str):The name of album
    year(int): The year was album was released
    artist(Artist) : The artist responsible for album. If not specified the artist will default to an artist with name "Various Artist"
    track(List[Song]) : A list of songs on the album

    Methods :
    addSong: used to add a new song to album's track list
    """
    def __init__(self,name,year,artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self,song,position = None):
        """Adds a song to track list

        Args:
            song (Song): A song to add
            position (int, optional): If specified, the song will be added to that position in track list - inserting it between other songs if necessary. Otherwise song willl be added to end of the list. Defaults to None.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position,song)

class Artist:
    """Basic class to store artist details

    Attributes:
        name(str) : name of the artist
        albums (List(Album)); A list of the album by this artist. The list only includes those albums in colection, it is not an exhaustive list of artist's published albums    
        
        
    Methods :
        add_album : Use to add a new album to artist's albums list
        """
    def __init__(self,name):
        self.name = name
        self.albums = []

    def add_album(self,album):
        """Add a new album to list

        Args:
            album (Album): Album object to add to the list. If the album is already present , it will not be added again
        """
        self.albums.append(album)

def find_object(field,object_list):
    """Check object_list to see if an object with a name attribute eqal to field exists
    """
    for item in object_list:
        if item.name == field:
            return item
    return None 


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field = tuple(line.strip("\n").split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{} ".format(artist_field,album_field,year_field,song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                #We have just read details for new artist
                #retrieve artist object if there is one,
                #otherwise create a new artist object and add it to artist list
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field,year_field,new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                #We have kust read details for new album
                #Retrieve the album object for current artist
                #otherwise create a new album object and store it in artist's collection
                new_album = find_object(album_field,new_album.albums)
                if new_album is None:
                   new_album = Album(album_field,year_field,new_artist)
                   new_artist.add_album(new_album)

            new_song = Song(song_field,new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

        return artist_list

def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with original file

    Args:
        artist_list (list): _description_
    """
    with open("checkfile.txt",'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist,new_album,new_song),file=checkfile)




if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)