class Student:
    def __init__(self,name,score):
        self.name = name
        self._score = score

    @property
    def score(self):
        print("Get scores")
        return self._score

    @score.setter
    def score(self,value):
        print("Setting score")
        if 0 < value < 100:
            self._score = value
        else:
            print("Invalid score")


if __name__ == '__main__':
    s =Student("Rahul",80)
    print(s.score)