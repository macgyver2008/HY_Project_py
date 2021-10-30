import random
class makeCH() :
    def __init__(self) :
        self.hp = random.randrange(150, 200)
        self.mp = random.randrange(170, 200)
    def hit(self) :
        return self.hp * 0.05
    def heal(self) :
        return self.hp * 0.03
at = 0
a = makeCH()
print('A charcter hp : {}   , mp {}   '.format(a.hp, a.mp))
b = makeCH()
print('B charcter hp : {}   , mp {}   '.format(b.hp, b.mp))

while not b.hp <= 0 or a.hp <= 0 :
    print('a = 공격, h = 힐')

    chat = input()
    if chat == 'a' :
        at = random.randrange(2)

    if at  == 1 :
        b.hp = b.hp - a.hit()
        a.mp = a.mp +10
        print("after b charcter hp : {} , mp {}".format(b.hp,b.mp))
    if chat == 'h' :
        if a.mp < 15 :
            a.hp = a.hp + a.heal()
            a.mp = a.mp - 15
        at = 3
        print("after a charcter hp : {} , mp {}".format(a.hp, a.mp))
    if at == 0 :
        print("적이 회피하였습니다")
    v = random.randrange(2)
    if v == 1 :
        a.hp = a.hp - b.hit()
        print("after a charcter hp : {} , mp {}".format(a.hp,a.mp))
    if v == 0 :
        print("적 Miss")




























