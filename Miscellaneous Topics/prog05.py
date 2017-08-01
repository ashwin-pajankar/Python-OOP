'This is docstring section for this file'


class Point:
    'This is a docstring for class Point'


    def __init__(self, x, y, z):
        'This is initializer method for class Point'
        self.assign(x, y, z)
        

    def assign(self, x, y, z):
        'This method assigns the values to the co-ordinates of Point'
        self.x = x
        self.y = y
        self.z = z


    def printPoint(self):
        'this method print the values of the co-ordinates of the point'
        print(self.x, self.y, self.z)


p1 = Point(0, 0, 0)
#print(p1.__doc__)
#print(help(p1))

print(p1.assign.__doc__)
print(help(p1.assign))
#print(p1.printPoint.__doc__)
#print(p1.__init__.__doc__)
