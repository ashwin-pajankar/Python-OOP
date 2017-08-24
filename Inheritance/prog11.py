class A:

    def __init__(self):
        self.a = "Public"
        self._b = "Internal Use Only"
        self.__c = "Name Mangling in Action"


def main():
    x = A()
    print(x.a)
    print(x._b)
    print(x._A__c)


if __name__ == "__main__":
    main()
