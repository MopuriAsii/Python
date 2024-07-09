"""
def add(a, b):
    return a * b


print(add(10, 20))


# lambda arguments:expression

a = lambda a, b: a * b
print(a(10, 20))

"""

"""
def mul():
    a1 = [5, 3, 7, 3, 8]
    l = []
    for i in range(len(a1)):
        b = a1[i] * 2
        l.append(b)
    print(l)


mul()
"""

# map(function,values)--->applies logic to each and every element
"""
a2 = [5, 3, 7, 3, 8]
b1 = list(map(lambda x: x * 2, a2))
print(b1)
"""

"""
def m3():
    a3 = ["1", "2", "3"]
    for i in range(len(a3)):
        a3[i] = int(a3[i])
    return a3


print(m3())

a3 = ["1", "2", "3"]
out = list(map(int, a3))
print(out)
"""
