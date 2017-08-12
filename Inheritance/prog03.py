class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return self.first + " " + self.last + ", " + str(self.age)


class Employee(Person):
    
    def __init__(self, first, last, age, sal):
        self.sal = sal
        super().__init__(first, last, age)

    def __str__(self):
        return super().__str__() + ", " + str(self.sal)



def main():
    x = Person("Ashwin", "Pajankar", 31)
    print(x)

    y = Employee("James", "Bond", 40, 1000)
    print(y)

if __name__ == "__main__":
    main()
