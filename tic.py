import random
def make_map() :
    tic_map = ["" for i in range(9)]            #tic_map = []
    return tic_map                              # for i in range(9):

def AI(tic_map) :
    while True:
        a = random.randrange(8)
        if tic_map[a] == "" :
            tic_map[a] = "o"
            return tic_map

def player(tic_map):
    while True:
         pos = int(input("1~9"))
         pos = pos - 1
         if tic_map[pos] == "" :
             tic_map[pos] = "x"
             return tic_map

def print_map(tic_map):
    print("-----------------")
    print(" | " + tic_map[0] + " | " + tic_map[1] + " | " + tic_map[2] + " | ")
    print(" | " + tic_map[3] + " | " + tic_map[4] + " | " + tic_map[5] + " | ")
    print(" | " + tic_map[6] + " | " + tic_map[7] + " | " + tic_map[8] + " | ")

tic_map = make_map()                      #    tic_map.append(0)
print('player_x')
print("AI_o")
while True:
    tic_map = player(tic_map)

    print_map(tic_map)

    tic_map = AI(tic_map)

    print_map(tic_map)