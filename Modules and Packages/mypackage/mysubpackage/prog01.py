class Class01:

    def __init__(self):
        print("Created an Object for Class01...")


class Class02:

    def __init__(self):
        print("Created an Object for Class02...")


def main():
    O1 = Class01()
    O2 = Class02()
    

if __name__ == "__main__":
    print("The module prog01 is being run directly...")
    main()
else:
    print("The module prog01 is imported to the current module...")

