class Wing(object):
    def __init__(self,ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("This is fun")

        elif self.ratio == 1:
            print("THis is hard but I'll fly")

        else:
            print("I think I'll just walk")

class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle,waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):
    def __init__(self):
        self._wing = Wing(0)

    def walk(self):
        print("Waddle waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's bit chilly this far south")

    def quack(self):
        print("Are you avain or larf ? I am penguin")

    def fly(self):
        self._wing.fly()

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    # test_duck(donald)
    donald.fly()

    percy = Penguin()
    percy.fly()
    # test_duck(percy)