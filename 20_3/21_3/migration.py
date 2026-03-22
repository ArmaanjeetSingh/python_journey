import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
d1 = ducks.Duck()
d2 = ducks.Duck()
d3 = ducks.Duck()
d4 = ducks.Duck()
d5 = ducks.Duck()
d6 = ducks.Duck()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(d1)
flock.add_duck(d2)
flock.add_duck(percy)
flock.add_duck(d3)
flock.add_duck(d4)
flock.add_duck(d5)
flock.add_duck(d6)


flock.migrate()