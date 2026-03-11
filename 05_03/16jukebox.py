from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("please choose your album (invalid choice exits):")
    # for index, (title, artist, year, songs) in enumerate(albums):
    #     print("{}: {}, {}, {}, {}".format(index+1,title,artist,year,songs))
    # for index,value in enumerate(albums):
    #     title,artist,year,songs = value
    #     print(index,title,artist,year,songs)
    #     print()
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index+1,title))
        
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]
    else:
        break
    
    print("Please chose your song:")
    for index,(track_number,song) in enumerate(songs_list):
        print(f"{index+1}: {song}")
        
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice-1][SONG_TITLE_INDEX]
    else:
        print("Please chose your song:")
        for index,(track_number,song) in enumerate(songs_list):
            print(f"{index+1}: {song}")
        song_choice = int(input())
    
    print("Playing {}".format(title))
    print("="*40)