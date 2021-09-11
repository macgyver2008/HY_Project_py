import random
a = []
found1 = 0
found2 = 0
found3 = 0
found4 = 0
found5 = 0
for i in range(99) :
    a.append(random.randrange(1, 6))
print(a)
for j in range(99) :
    if a[j] == 1:
        found1 += 1
    elif a[j] == 2:
        found2 += 1
    elif a[j] == 3:
        found3 += 1
    elif a[j] == 4:
        found4 += 1
    elif a[j] == 5:
        found5 += 1
print(found1,found2,found3,found4,found5)
