# All the primitive data types are immutable
a = 23
b = 23
print(id(a) == id(b))
a = "hey"
b = "hey"
print(id(a) == id(b))
# t = (1, 2, 3)
# t2 = (1, 2, 3)
l = [1, 2, 3]
l2 = [1, 2, 3]
print(l == l2)
print(id(l)==id(l2))
t = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t) == id(t2))