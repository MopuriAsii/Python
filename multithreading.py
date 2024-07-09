from threading import Thread
from time import sleep


class Sample(Thread):
    def m1(self):
        print("m1")

    def run(self):
        for i in range(1, 11):
            print(i)
            sleep(2)
        self.m1()  # -----> calling one function inside another function using self


class Demo(Thread):
    def run(self):
        for i in range(11, 21):
            print(i)
            sleep(2)


obj = Sample()
obj1 = Demo()
obj.start()
obj1.start()
obj.join()
obj1.join()  # ----->wait until the Thread gets terminated and the prints the end of the program otherwise it will print the statement in the middle
print("End Of The Program")
