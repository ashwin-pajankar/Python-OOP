class Person:

    def assignbasic(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):

    def assignemp(self, idno):
        self.idno = idno


class Programmer(Employee):

    def assignprog(self, lang):
        self.lang = lang


def main():
    Obj1 = Programmer()
    Obj1.assignbasic("ASHWIN", 31)
    Obj1.assignemp(1002)
    Obj1.assignprog("Python 3")
    print(Obj1.name, Obj1.age, Obj1.idno, Obj1.lang)

if __name__ == "__main__":
    main()
