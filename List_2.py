pwd = []
ID = []
for i in range(4):
    print('ID')
    a = input()
    if i == 0:
        ID.append(a)
    if 1 != 0:
        for q in range(len(ID)):
            if a != ID[q]:
                ID.append(a)
    print('psw')
    b = input()
    pwd.append(b)
print(ID)
print(pwd)
print('input_id')
c = input()
for o in range(4) :
    if c == ID[o] :
        print('input_pwd')
    d = input()
    if id[o] == (d == pwd[o]) :
        print('login')
#비번에 !@#$% 특수문자가 포함하게
#ID 8자 이상 입력받게하기

