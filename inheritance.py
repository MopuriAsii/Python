# single inheritance:


class Parent:
    def fun(self):
        print("Parent classs")


class Child(Parent):
    def fun1(self):
        print("Child Class")


obj = Child()
obj.fun1()
obj.fun()


# MULTI LEVEL INHERITANCE:


class Iphone13:
    def chargerPort(self):
        print("lighting port")


# add camera fun
class Iphone14(Iphone13):
    def camera(self):  # ------>polymorphism
        print("20MP")

    def os(self):
        print("ios 17")


class Iphone15(Iphone14):
    def camera(self):  # --------------->Polymorphism
        print("30MP")
        super().camera()

    def chargerPort(self):
        print("Type c")

    def display(self):
        print("Dynamic Island")


obj = Iphone15()
obj.camera()
obj.chargerPort()
obj.display()
obj.os()


# hierarchical inheritance:


class teacher:
    def english(self):
        print("engilsh teacher")


class student1(teacher):
    pass


class student2(teacher):
    pass


obj = student1()
obj.english()

# multiple inheritance


class Father:
    def m1(self):
        print("m1 from Father")


class Mother:
    def m1(self):
        print("m2 from Mother")


class child(Father, Mother):  # father is given first so it will acess father first
    pass


obj = child()
obj.m1()


#
