t = (1, 2, 3)
print(t)
t = list(t)
t[1] = 100
t = tuple(t)
print(t)

for x in t:
    print(x)

print(type(t))
x = ('apple', )
print(type(x))

print(t + x)
