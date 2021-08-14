print("hello world")

# variable 변수
a = 2
a = 4
print(a) #정수 int
print(type(a))
a = 'text' #문자 str
print(a , type(a))

a = 3.14 #소수 float
print(type(a))

a = 4 + 1
a = a - 1
a = a * a
print(a)

if a == 16 :
    print('t')
if a != 16 :
    print('f')

num = int(input())
print(num)
print(type(num))

if (num % 2) == 0 :
    print("even")
else:
    print('odd')

print('first num')
a = int(input())
print('seccond num')
b = int(input())
print('더하기,빼기,나누기,곱하기')
c = input()
if c == '더하기' :
    print(a + b)
if c == '빼기' :
    print(a - b)
if c == '나누기' :
    print(a / b)
if c == '곱하기' :
    print(a * b)
