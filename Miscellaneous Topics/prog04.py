def fun1(a, b):
    return a+b


class Point:


    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def printPoint(self):
        print(self.x, self.y, self.z)


p1 = Point()
p1.assign(2, 3, 5)
p1.printPoint()

print(fun1(2, 3))

p2 = Point()
p1.assign(6, 2, -4)
p1.printPoint()
