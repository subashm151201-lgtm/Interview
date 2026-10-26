class A:
    # Parent class

    def fun1(self):
        print("fun1() is working")

    def fun2(self):
        print("fun2() is working")


class B(A):
    # Child class of A

    def fun3(self):
        print("fun3() works")

    def fun4(self):
        print("fun4() works")


obj1 = B()

obj1.fun1()  # Inherited from A
obj1.fun2()  # Inherited from A
obj1.fun3()
obj1.fun4()


class C(B):
    # Child class of B

    def fun5(self):
        print("fun5() works")

    def fun6(self):
        print("fun6() works")


c = C()

c.fun1()  # Inherited from A through B
c.fun5()