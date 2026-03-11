i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
    
available_exits = ["north","south","east","west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction")
    if chosen_exit == "quit":
        print("game over")
        break
    print(chosen_exit)

print("aren;t you glad you got out of there")


for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(0,20):
    if i % 3  == 0 or i % 5 == 0:
        continue
    print(i)