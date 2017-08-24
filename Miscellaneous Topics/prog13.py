class A:


    def method01(self, i=None):
        if i is None:
            print("Sequence 01")
        else:
            print("Sequence 02")
            return 1


def main():
    x = A()
    x.method01()
    ret = x.method01(5)
    print(ret)


if __name__ == "__main__":
    main()
