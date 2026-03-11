text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

words = text.split()
print(words)

print()
preps_used = prepositions.intersection(set(words))
print(preps_used)