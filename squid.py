#다리 갯수 26~24 참가자 16명 자신의 말 = □  다른사람들의 말 = ○ 사망자 = △
#필드 「 1」 「 2」 「 3」 「 4」 「 5」 「 6」 「 7」 「 8」 「 9」 「 10」 「 11」 「 12」「 13」 「 14」 「 15」 「 16」 「 17」
#필드 「 1」 「 2」 「 3」 「 4」 「 5」 「 6」 「 7」 「 8」 「 9」 「 10」 「 11」 「 12」「 13」 「 14」 「 15」 「 16」 「 17」
import random
A = []
B = []
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
def make_place() :
    for i in range(16) :
        a = (random.randrange(1, 3))
        if a == 1 :
            A.append('r')
            B.append('f')
        else:
            A.append('f')
            B.append('r')
    return()

def others(pl) :
    for i in range(1, 13) :
        ran = random.randrange(1, 3)
        if i == 1 :
            if ran == 1 :
                p1 = pl
            else:
                p1 = pl
        if i == 2 :
            if ran == 1 :
                p2 = pl
            else:
                p2 = pl
        if i == 3 :
            if ran == 1 :
                p3 = pl
            else:
                p3 = pl
        if i == 4 :
            if ran == 1 :
                p4 = pl
            else:
                p4 = pl
        if i == 5 :
            if ran == 1 :
                p5 = pl
            else:
                p5 = pl
        if i == 6 :
            if ran == 1 :
                p6 = pl
            else:
                p6 = pl
        if i == 7 :
            if ran == 1 :
                p7 = pl
            else:
                p7 = pl
make_place()
print(A)
print(B)
for i1 in range(1, 17) :
    others(i1)
print(p1, p2, p3, p4, p5, p6, p7)


