# b = []
# c = [1,2,3,4,5,6,7,8]
#
# b.append(1)
# c.append(2)
#
# print(b)
# print(c)
#
# import random
# a = random.randrange(1,100) #a 는 1에서 100까지 무작위 수로 정한다
# print(a)
import random
#
# a = []
# b = []
# for i in range(100) :
#     a.append(1)
# for j in range(100) :
#     c = random.randrange(1,100)
#     b.append(c)
# print(b)



# 20210814 숙제 임의의 수 하나 입력받고 이거와 약수를 리스트에 넣기
a = int(input())
b = []
for i in range(1,a+1) :
    if a % i == 0 :
        b.append(i)
        print('b')
