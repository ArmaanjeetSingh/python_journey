word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

for element in text.casefold():
    if element.isalnum():
        if element in word_count:
           word_count[element] += 1
        else:
            word_count[element] = 1

for letter, count in sorted(word_count.items()):
    print(letter, count)
