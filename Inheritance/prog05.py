class Animal:

    def move(self):
        print("I move therefore I am...")


class Human(Animal):

    def move(self):
        print("Humans can walk and run...")


class Fish(Animal):

    def move(self):
        print("Fishes can swim and dive...")

def main():
    h1 = Human()
    h1.move()

    f1 = Fish()
    f1.move()


if __name__ == "__main__":
    main()











