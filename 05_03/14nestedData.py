albums = [
    ("Welcome to my Nightmare","Alice cooper",1973),
    ("Bad company",1974,"Bad company"),
    ("Nightflight","Budgie",1981),
    ("Ride the Lighting","Metallica",1984)    
]
# for album in albums:
#     name,artist,year = album
#     print("Album : {}, Artist : {}, Year: {}".format(name,artist,year))
    
# for name,artist,year in albums:
#     print("Album : {}, Artist : {}, Year: {}".format(name,artist,year))
    
albums = [
    ("Welcome to my Nightmare","Alice cooper",1975,[
        (1, "Welcome to my Nightmare"),
        (2, "Devil's Food"),
        (3,"The Black Widow"),
        (4,"Some Folks"),
        (5,"only Women Bleed")
    ]
    ),
    ("Bad Company","Bad Company",1974,
    [
        (1,"Can't get Enough"),
        (2,"Rock Ready"),
        (3,"Ready for Love"),
        (4,"Don't Let Me Down"),
        (5,"Bad company"),
        (6,"The way I choose")
    ]
    ),
        ("More Mayhem","Imelda May",2011,
        [
            (1,"Pulling the Rug"),
            (2,"Psycho"),
            (3,"Mayhem"),
            (4,"Kentish Town Waltz")
        ])
    
]

for name,artist,year,songs in albums:
    print("Album: {}, Artist: {}, Year: {},Songs: {}".format(name,artist,year,songs))
print()

album = albums[2]
print(album)

songs = album[3]
print(songs)

song = songs[1]
print(song[1])