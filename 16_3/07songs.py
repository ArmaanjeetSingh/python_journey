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
        self.duraion = duration

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







help(Song)
print(Song.__init__.__doc__)