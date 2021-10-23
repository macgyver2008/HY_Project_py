import random
class makeCH() :
    def __init__(self) :
        self.hp = random.randrange(150, 250)
        self.mp = random.randrange(170, 200)
def hit(self) :
    return self.hp * 0.1 

a = makeCH()
print('A charcter hp : {}   , mp {}   '.format(a.hp, a.mp))
b = makeCH()
print('A charcter hp : {}   , mp {}   '.format(b.hp, b.mp))   

while b.hp == 0 :   

    chat = str(input)
    v = random.randrange(0, 2)

    if chat == 'at' :
        b.hp = b.hp - a.hit()
        print("after b charcter hp : {} , mp {}".format(b.hp,b.mp))


    if v == 2 :
        a.hp = a.hp - b.hit()
        print("after a charcter hp : {} , mp {}".format(a.hp,a.mp))
