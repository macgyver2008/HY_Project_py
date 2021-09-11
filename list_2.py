pwd = []
ID = []
for i in range(4):
    print('ID')
    a = input()
    if i == 0 and len(a) >= 7 :
        ID.append(a)
    if 1 != 0:
        for q in range(len(ID)):
            if a != ID[q] and len(a) >= 7 :
                ID.append(a)
            else:
                print('*오류* ID의 길이를 8글자 이상으로 입력하시오,또는 중복된 ID입니다')
    print('psw')
    b = input()
    b2 = []
    for i2 in range(len(b)) :
        if b[i2] == '!' or b[i2] == '@' or b[i2] == '#' :
         pwd.append(b)
        elif b[i2] != '!' or b[i2] != '@' or b[i2] != '#' :
            print('**오류** 비밀번호에  !,@,#을 추가해 주세요')
print(ID)
print(pwd)
print('input_id')
c = input()
for o in range(len(ID)) :
    if c == ID[o] :
        print('input_pwd')
    d = input()
    if id[o] == (d == pwd[o]) :
        print('login')