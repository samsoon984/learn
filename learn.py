class Fourcal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#a = Fourcal()
#b = Fourcal()

#a.setData(4, 2)
#b.setData(3, 7)


class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

if __name__ == "__main__":
    a = MoreFourcal(4, 0)
    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())
    print(a.pow())