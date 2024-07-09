class EligibleError(Exception):
    def __init__(self, value):
        pass


class Sample:
    def eligible(self, age, percentage):
        if age < 18 or percentage < 60:
            raise EligibleError("not elligible for registration")
        else:
            print("registration is successful")


obj1 = Sample()
try:
    obj1.eligible(17, 65)
except EligibleError as e:
    print(e)
print("end of program")
