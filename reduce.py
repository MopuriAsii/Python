from functools import reduce

"""
# cumulative freguency
x = [1, 2, 3, 4]
out = reduce(lambda a, b: a + b, x)
print(out)
"""

"""
## filter:
a1 = [1, 2, 4, 5, 8]
out = list(filter(lambda x: x % 2 == 0, a1))
print(out)
"""
# zip:

eno = [101, 102, 103, 104]

ename = ["abc", "bcd", "cde", "def"]
out = list(zip(eno, ename))
print(out)

eno = [101, 102, 103, 104]
ename = ["abc", "bcd", "cde", "def"]
out = dict(zip(eno, ename))
print(out[101])

print(list(filter(lambda x: x > 102, eno)))  # applies the condition
i = dict(filter(lambda x: x[0] > 102, out.items()))
print(i)
