import random
a = []
b = 0
c = 0
d = 100
for i in range (100) :
    b = (random.randrange(1, 100))
    a.append(b)
    if 100 - b < 100 - c :
        c = b
    if 100 - b > 100 - d :
        d = b
print(a)
print(c)
print(d)