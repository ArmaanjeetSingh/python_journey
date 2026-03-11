shopping_list = ["milk","sauce","sugar","rice","wheat","spices"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"] #list concatenation
print(shopping_list)
print(id(shopping_list))

print(another_list)

# a = b = c = d = e = f = another_list
# print(id(a))
# print(a)
# print(id(c))
# print(id(b))
# b.append("butter")
# print(id(d))
# print(id(e))

# print(a)
# print(d)
# print(shopping_list)