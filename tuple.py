#! python3
t= (1,2,2,3)
l = [1,2,3]

print(type(t))
print(type(l))

print(t.index(2))

print(t.count(2))

t= (1,2,3,l)

print(t[3][0])
