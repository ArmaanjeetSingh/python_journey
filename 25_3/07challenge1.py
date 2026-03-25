# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).
 
text = input("Please enter your text: ")
 
output = []
for x in text.split():
    output.append(len(x))
print(output)
 
# type your solution here:
output_comp = [len(x) for x in text.split()]
print(output_comp)
 
# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):
 
output = []
for x in text.split():
    output.append((x, len(x)))
print(output)
 
# type the corresponding comprehension here:
output_comp1 = [(x,len(x)) for x in text.split()]
print(output_comp1)

# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.
#
# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimetres to 1 inch.
 
inch_measurement = (3, 8, 20)
 
cm_measurement = [inch* 2.54 for inch in inch_measurement]
print(cm_measurement)
 
# Once you've got the correct values, change the code to produce a tuple, rather than a list.
cm_measurement = tuple([inch* 2.54 for inch in inch_measurement])
print(cm_measurement)