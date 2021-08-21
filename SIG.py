import random
#b=[]
#b.append(1)
#b.append(4)
#print(b[0], b[1])



# for i in range(1,10) :
#     a = random.randrange(1, 10)
#     if i % 2 == 0 :
#         print(i ,'짝수')
#     else:
#         print(i ,'홀수')



# for i in range(1,10) :
#     print(i*'*')


# c = 0
# a = random.randrange(1, 10)
# for i in range(2, a + 1) :
#     if a % i == 0 :
#         c += 1
#     else:
#         print(i)
# if c == 0 :
#     print('소수')




# list = []
# for i in range(1,11) :
#     list.append(random.randrange(1,10))
#     print(list)



l = []
for i in range(11) :
    l.append(random.randrange(1,10))
max_vulue = l[0]
for i in range(len(l)) :
    if max_vulue > l[i] :
        max_vulue = l[i]

print(max_vulue)








# a = 14
# l = []
# for i in range(1, a+1) :
#
#     if a % i == 0 :
#         l.append(i)
#         print(l)






