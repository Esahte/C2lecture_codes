class A:
    def __init__(self):
        self.x = 1
        self.__y = 1
    def getY(self):
        return self.__y
a = A()
print(a.getY())

