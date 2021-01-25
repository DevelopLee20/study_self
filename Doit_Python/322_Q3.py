a = [1,2,3]
a = a + [4,5]
b = a
a = [1,2,3]
a.extend([4,5])
c = a
print(b)
print(c)
print(b == c)