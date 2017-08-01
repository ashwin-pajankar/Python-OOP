class Point:
    'Sample docstring of class Point!'


    def __init__(self, x, y, z):
        self.assign(x, y, z)
        

    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def printPoint(self):
        print(self.x, self.y, self.z)


p1 = Point(2, 3, 5)
p2 = Point(6, 2, -4)

a = 5
pi = 3.14
text = "Hello World!"

print(type(3))
