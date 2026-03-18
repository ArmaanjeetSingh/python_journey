from enemy import Enemy, Troll, Vampyre

random_monster = Enemy("Basic enemy",17,1)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll("troll1")
print("Ugly troll = {}".format(ugly_troll))

# another_troll = Troll("Ug",18,1)
# print("Another troll = {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)
print("*"*80)

# while vamp.alive:
#     vamp.take_damage(1)
    # print(vamp)

vamp.lives = 0
vamp.hit_points = 1
print(vamp)