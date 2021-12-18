def find_prime(a) :
    count = 0
    for i in range(2, a//2 +1):
        if a % i == 0:
            count += 1
            break
    if (count == 0 or a == 2) and a !=1 :
        return 1
    else:
        return 0
TS = 0
FP = 0

for i in range(n, m +1):
    flag = FP(i)
    if flag ==1:
        TS += i
        if FP == 0:
            FP = i
if FP ==0:
    print(-1)
else:
    print(TS)
    print(FP)
