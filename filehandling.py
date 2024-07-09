# write:
'''
f1 = open("test.txt", "w")
"""
f1.write("hello world\n")
f1.write("Testing Purpose\n")
f1.write("welcome\n")
"""
f1.write("hii\n")

f1.close()


# read:
"""
f1 = open("test.txt", "r")
# print(f1.read())
for i in range(1, 4):
    print(f1.readlines(i))
----for readline
print(f1.readline())
f1.close()

f1.close()
"""


# appending:
"""
f1 = open("test.txt", "a")
f1.write("welcome1\n")
f1.close()
"""

f1 = open("test.txt", "r")
print(f1.readline())
f1.close()

'''
