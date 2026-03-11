# pangram = "The quick Brown fox Jumps oVer the Lazy dog"

# # list specially-#sort() -none / original list changes
# # iterable-string,list,tuple,range#sorted - new list

# letter = sorted(pangram)#new list
# # print(set(letter))
# print(letter)
# # ''-ascii
# # A-Z - 65 -90
# # a-z 91

numbers = [2.3, 4.5, 8.7, 9.2, 1.6]#iterable-list
sorted_nums = sorted(numbers)
print('New list',sorted_nums)#new list value stored
print('Original list ',numbers.sort(reverse=True))
print(numbers)


# another_sorted_numbers = numbers.sort()
# print(numbers)
# print(another_sorted_numbers)

missing_letter = sorted("The quick fox jumped over the lazy dog",
                        key = str.casefold)
missing_letter = sorted("the quick fox jumped over the lazy dog",
                        key = str.casefold)
print(missing_letter)

names = ["Graham","John","terry","eric","Terry","michael"]
#str.casefold-> names = ["graham","john","terry","eric","terry","michael"] -> sort()
names.sort(key=str.casefold,reverse=True)
print(names)

