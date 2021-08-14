count = 0
a = input(int())
for i in range(2, a) :
    if i % 2 == 0 :
        count += 1  #count = count + 1
        break
    if count == 0 :
        print("prime")
    else:
        print('not prime')


