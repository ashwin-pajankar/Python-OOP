class Point:


    def __init__(self, x, y, z):
        self.assign(x, y, z)
        

    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def printPoint(self):
        print(self.x, self.y, self.z)


p1 = Point(2, 3, 5)
p1.printPoint()

p2 = Point(6, 2, -4)
p2.printPoint()
