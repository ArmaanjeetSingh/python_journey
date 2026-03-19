# def add(a,b):
#     try :
#        return a+b
#     except TypeError:
#         return "Invalid types"

# print(add(2,3))
# print(add('2','3'))
# print(add('2',3))


class Dog:
    def speak(self):
        return "Bark !!!"

class Cat:
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

object_list = [dog,cat]
for obj in object_list:
    print(obj.speak())


