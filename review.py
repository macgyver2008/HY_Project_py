# 자료형
#1. 숫자(int, float)

#2. 문자열
#문자열 연산
#덧샘 = 문자열 붙이기
#곱샘 = 문자열 반복
# 인덱싱 = a[n], n은 0부터
#슬라이싱 = a[n:m:o], n = 시작, m = 끝, o = 오프셋
a = 'Life is too short.'
print(a[12:17])
print(a[::-1]) # 문자열 뒤집기
#포맷 (format) = 형식 문자열
print("im %d years old"%6)#정수 = %d, 실수는 %f, 8진수는 %o 16진수는 %x 문자열은 %s
#3. 리스트
#list(), []
# 덧샘 = [] + []
# 곱샘 리스트 내용반복
# 값 추가 .append
#값 제거 del, remove, pop
#정렬 sort, sorted
#확장 extend == 리스트 덧샘
#갯수 세기  len, count              len(리스트) 리스트 항목갯수 세기  리스트.count(n)   리스트에 n항목이 몇개있나 세기
#A리스트 역순으로 정렬
A = [1, 2, 3, 4, 5]
# A.sort(reverse=True)
b = sorted(a, reverse=True)
print(b)
A.insert(2, 'Hello_World') # 2값이 있는위치에 헬로월드 삽입

#4. 튜플(값을 변경할수없는 리스트)
#t1 = ()   #비어있는 튜플
#t2 = (1,) #하나만 있는 튜플 컴마 붙이자
#t3 = (1, 2) #두개부터는 괄호 생략이 가능함
#t4 = 1, 2, 3
#튜플도 덧샘,  곱샘, 슬라이싱이 가능함

#5.딕셔너리
#key, value
#key = immutable, value = mutable
#값을 조회 = d[key]
#값을 변경 = d[key] = value
#값을 추가 = d[new_key] = value
#값을 삭제 = del d[key]
#key 리스트    list(d.keys())
#value 리스트  list(d.value())
d = { 1:'v', 'h':3, 3.0:4}
print(d[1])
d[1] = '일'
print(d[1])
d['new1'] = 'new'
del d['new1']

#6.set 집합
#set(), {}
#순서없음, 중복없음.                             
# union(합집합), difference(차집합), intersection(교집합)
s = {1, 2, 3, 3, 3}
s2 = {3, 4, 5}


#7.bool boolean
#단 두가지 값만 가짐 . Ture, False
#참과 거짓에서 볼수있음
