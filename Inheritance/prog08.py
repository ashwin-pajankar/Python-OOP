class A:

    def m(self):
        print("m() from class A...")


class B(A):
    
    def m(self):
        print("m() from class B...")


class C(A):
    
    def m(self):
        print("m() from class C...")


class D(B, C):

    def m(self):
        print("m() from class D...")
        B.m(self)
        C.m(self)
        A.m(self)



def main():
    Obj1 = D()
    Obj1.m()

if __name__ == "__main__":
    main()
