#과목점수 구하기 N개의 과목점수 입력받아 평균 점수 구하기
A =[]
B = 0
answer = 0
while len(A) == 3:
    A = A.append(input())
for i in range(2):
    B += A[i]
answer = b/3


#주민등록번호 881120-1068234에서 연도, 월 ,일을 추출하여 생년월일 print
Num = '881120-3068234'
cen = 0
if Num[7] == '1' :
    print("남(male)")
    cen = 19
if Num[7] == '3':
    print("남(male)")
    cen = 20
if Num[7] == "2":
    print("여(female)")
    cen = 19
if Num[7] == "4":
    print("여(female)")
    cen = 20
print("%s년 %s월 %s일"%(str(cen) + Num[:2], Num[2:4], Num[4:6]))
# print("19{}년 {}월 {}일".format(Num[:2], Num[2:4], Num[4:6]))



a = [3, 2, 1, 3, 4, 6, 7, 6, 6, 7]
b = list(set(a))
b.sort()
print(b)
