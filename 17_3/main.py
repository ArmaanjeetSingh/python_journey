import player

tim = player.Player("tim")

print(tim.name)
print(tim.lives)

# tim.lives -= 1 can't called outside class
# print(tim.lives) protected
print(tim.get_name())
tim.set_lives(300)
print(tim.get_lives())
print(tim)


tim.lives -= 1
print(tim)

tim.lives = 9
print(tim)