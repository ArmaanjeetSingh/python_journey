panagram = """The quick brown
fox jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(','))

separators = "!@#$%^&*,?"
values = " ".join(char if char not in separators else "" for char in numbers).split()
print(values)