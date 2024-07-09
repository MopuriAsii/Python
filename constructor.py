class sample:
    def fun(self):
        print("fun")

    def fun1(self):
        print("fun1")

    def __init__(self):  # first this will be executed because it is constructor
        print("hello")  # it is done by using "__init__"


obj = sample()
obj.fun()
obj.fun1()
