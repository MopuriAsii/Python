class Practice:
    name = "ashritha"

    def new(self):
        print("learning python")

    def hii(self):
        print(self.name)


obj = Practice()
obj.hii()


print(obj.name)
obj.new()


class hello:
    def fun(self):
        print("hello")

    new = "hii"


new1 = hello()

new1.fun()
print(new1.new)


class Example:
    def p1(self):
        print("hello")

    def p2(self):
        print("hii")

    def p3(self):
        a = 10
        print(a)
        self.p1()  # hii.p1()[hii--->object]
        self.p2()


hii = Example()
hii.p3()
