l = [1, 2 ,5]
id_1 = id(l)
print(id(l))
l.append(54)
print(id(l))
id_2 = id(l)
print(id_1 == id_2)

l = [1, 2 ,5] + [5, 4 ,7]
print(l)
print(id(l))

t = (1, 5)
print(id(t))
t = (1, 5) + (9, 8)
print(id(t))
"kunal"