#함수
# 1. 반복되는 내용을 재사용
# 2. 어떠한 ㅇ임력에 대한 출력 정의
# def 함수명(매개변수):
#  < 수행할 문장>
#  <수행할 문장 > ,,,

# def say():
#     return 'hi'
# def empty():
#     pass
#
# print(empty())

# 3. 매개변수 여러개면??  (*매개변수)
def all_sum(*args):      #튜플 형식
    print(args)

    all_sum(1,2,3,4,5,6)
# 4. 키워드 매개변수 (**매개변수)
def print_kwargs(**kwargs):       #딕셔너리 형식
    print(kwargs)
print_kwargs(a=1, b=2, c=3, d=4)

# 5.결과값(return)은 항상 하나
# 6. 매개변수에는 초기값을 지정할 수 있음

def people(name, age, gender="남성"):
    print(f'이름은{name}, 나이는{age}살, 성별은{gender}')

# 7. 변수의 범위는 함수 내에서만 유호함
# 8. 함수 밖의 변수를 함수 내에ㅐ서 변경 가능(global)
# 9. 한줄짜리 함수도 작성 가능(lambda)
# 10. 함수는 자기 자신을 호출할수있음 (재귀(recursive)함수라고 함)
#    재귀함수는 일반항을 구하는게 Point!!
def my_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

#. 클래스class
#1. 클래스란? 자신만의 데이터 타입을 정의하는 것
#2. 클래스란 붕어빵 틀?, 데이터의 형식을 정의하고, 틀에서 나온 붕어빵은 실체가 된다.
#   클래스 -> 붕어빵 트ㄹ, 인스턴트 -> 붕어빵
# class 클래스 이름:
#  < 클래스 내용>
#  < 클래스 내용 > ,,,
class 붕어빵:

    def __init__(self, taste):
        #붕어빵 멤버 필드(속성)
        self.taste = taste
        #붕어빵 멤버 메소드(함수)
    def print_taste(self):
        print(f'{self.taste}맛 붕어빵')

붕어빵 = 븡어빵('팥')
붕어빵 = 붕어빵('Pizza')
print(붕어빵)
# 3.클래스는 자신의 인스턴트를 만들때 '생성자' 라고 불리는 함수를 호출
#
# class 클래스 이름(상속 받을 클래스 이름)
# 5.클래스는 부모 멤버 메소드를 재작성할수있음(override)
# 6. 클래스는 연산자의 기능을 재작성할 수 있음 (연산자 override)

# stackElement 클래스 정의
class StackElement:
    # 자기 자신의 아래쪽 링크를 정의햐아함 (next)
    # 데이터를 가지고있어야함 (value)
    def __init__(self):
        pass
class Stack:

# 맨 위의 스텍 엘리먼트를 링크해야함
#push pop peek의 세가지 메소드를 정의해야함
#push는 데이터를 쌓는것
#pop은 스택의 맨 위의 데이터를 삭제하는거
#peek은 스택의 맨위의 데이터를 보는거
