class Example:
    def test(self, a, b):
        try:
            print(a / b)
        except Exception:
            print("divide by zero")


obj = Example()
obj.test(1, 0)


class Example1:
    def m1(self, a, b):
        try:
            a1 = [1, 2, 3]
            print(a1[5])
            print(a / b)
        except Exception:
            print("@")


obj1 = Example1()
obj1.m1(2, 0)
print("error solved")
