# return 뜻: 함수를 종료   값을 변환함
import random

def random_list() :
    a = []
    for i in range (10) :
        num = (random.randrange(1,10))
        a.append(num)
    return a
def find_max_value(l) :
    max_vulue = l[0]
    for i in range(len(l)):
        if max_vulue > l[i]:
            max_vulue = l[i]
    return max_vulue
tem_random = random_list()
