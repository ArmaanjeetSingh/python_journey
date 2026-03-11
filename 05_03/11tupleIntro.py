name = "Tim"
age = 10
print(name,age,"python",2020)
print((name,age,"python",2020))


welcome = ("Welcome to my Nightmare","Alice cooper",1973)
bad = ("Bad company",1974,"Bad company")
budgie = ("Nightflight","Budgie",1981)
metallica = ("Ride the Lighting","Metallica",1984)


print(metallica[0])
print(metallica[1])
print(metallica[2])

#tupple doon't support item assignment
#tuples are immutable
metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

table = ("Coffee table",200,100,75,34.50)
print(table[1]*table[2])
name,length,width,height,price = table
print(length*width)

albums = [
    ("Welcome to my Nightmare","Alice cooper",1973),
    ("Bad company",1974,"Bad company"),
    ("Nightflight","Budgie",1981),
    ("Ride the Lighting","Metallica",1984)    
]
for album in albums:
    name,artist,year = album
    print("Album : {}, Artist : {}, Year: {}".format(name,artist,year))