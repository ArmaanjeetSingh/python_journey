with open("Jabberwocky.txt","r") as jabber:
    text = jabber.read()


print(text)
for character in reversed(text):
    # print(character)
    pass

with open("Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break
print("*"*80)

with open("Jabberwocky.txt") as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.strip():
            break