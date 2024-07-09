from abc import ABC, abstractmethod


class Account:
    def savings(self):
        print("savings")


class cards(ABC):
    @abstractmethod
    def cashBack(self):
        print("cashback")

    def easyPay(self):
        print("EasyPay")


# obj = cards()       ---> can't be acessed
# obj.cashBack()


class cards1(cards):
    def cashBack(self):
        print("hello")


on = cards1()
on.cashBack()
