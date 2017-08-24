class A:

    def m(self):
        print("m() from A....")


class B:

    def m(self):
        print("m() from B....")


class C(B, A):

    def m(self):
        print("m() from C....")


def main():
    Obj1 = C()
    Obj1.m()


if __name__ == "__main__":
    main()
