# 캐스팅
# 문자열 => 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# 문자열변수.split(sep=구분문자) : 구분문자를 기준으로 해서 리스트화
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경

txt1 = '가 나 다 라 마'
txt2 = '가/나/다/라/마'
print(txt1, type(txt1)); print(txt2, type(txt2))

result1 = txt1.split() # defalut : 공백 기준
result2 = txt2.split('/')
print(result1, type(result1)); print(result2, type(result2))

print(list(txt1), type(list(txt1)))
print(list(txt2), type(list(txt2)))

# 리스트 => 문자열
# str(리스트이름)
# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화
print('-'*100)

myList = ['100', '200', '300']
result1 = str(myList)
result2 = ' '.join(myList)
print(f'myList = {myList}')
print(f'result1 = {result1}, {len(result1)}') # 이 경우는 [ ' , 모두 다 문자로 인식
print(f'result1[0] = {result1[0]}')
print(f'result2 = {result2}, {len(result2)}')

# 중첩 리스트 구조
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]
print('-'*100)
# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]

myList2d = [[100, 200, 300], ['가', '나'], 'Python']
print(myList2d , type(myList2d), len(myList2d))
print(myList2d[0])
print(myList2d[0][0])
print(myList2d[1][-1])
print(myList2d[-1])

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성

kor = [100, 80, 85]; math = [55, 70, 35]; eng = [80, 80, 100]; phtyon = [90, 70, 88]
grade = [kor, math, eng, phtyon]

print(grade)
print('국어점수 = ', grade[0])

'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.
------------
result
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''

kor_sum = grade[0][0] + grade[0][1] + grade[0][2]
print('kor : 합계 = %d, 평균 = %.2f' %(kor_sum, kor_sum/3))
# print(f'kor : 합계 = {kor_sum}, 평균 = {(kor_sum/3):.2f}')

# 튜플
print('-'*100)
# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정) : 튜플변수 = (값1, 값2...)
# 튜플 생성2 (초기값 지정) : 튜플변수 = 값1, 값2...
# 튜플 생성3 (빈 튜플) : 튜플변수 = ()

t1 = (100, 200, 'Python', 'MySQL', True)
t2 = 1, 56, '파이썬'
t3 = ()
print(t1, type(t1), len(t1))
print(t2, type(t2), len(t2))
print(t3, type(t3), len(t3))

t4 = (1000) # 갯수 1개는 튜플로 인식 안함 -> int로 인식.
# 튜플변수 = (값,)
t4 = (1000,)
print(t4, type(t4), len(t4))

# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]

t1 = (100, 200, 'Python', 'MySQL', True)
print(t1)
print(t1[0], t1[-1])
print(t1[0:2], t1[::2])
print(t1[::-1])

# 튜플의 값은 교체가 가능한가?
# TypeError , 내용 교체가 불가능하다.

# 튜플은 값을 새로 추가할 수 있는가?
# 튜플변수 += (값1,)
# 한개 추가시에는 쉼표(,) 주의
# 튜플변수 += (값1, 값2...)

myTuple = ()
print(f'myTuple = {myTuple}')
myTuple += (10,); print(f'myTuple = {myTuple}')
myTuple += (99, 88, 77); print(f'myTuple = {myTuple}')

# 튜플의 값은 삭제가 가능한가?
# 튜플 요소 각각의 값 삭제는 불가능
# 튜플변수 전체 삭제는 가능 : del 튜플변수

del myTuple
# print(f'myTuple = {myTuple}') 삭제 했으므로 에러

# 튜플의 연산자 + : 튜플끼리 더하기 -> 조인. 즉,합집합을 의미
# 튜플의 연산자 * : 튜플 요소 반복

myTuple1 = (100, 200)
myTuple2 = ('Phtyon', 'MySQL', True)
print(myTuple1 + myTuple2)
print(myTuple1*3)

# 각각 튜플 변수 정의하기
# 튜플전체변수 = (변수1, 변수2...) = (값1, 값2...)

myTuple = (t1, t2, t3) = (100, 200, 300)
print(myTuple)
print(f't1 = {t1}, t2 = {t2}, t3 = {t3}')
print(myTuple[0], myTuple[1], myTuple[2])

# 튜플 함수
# 튜플변수.count(값)
# 튜플변수.index(값)
# 튜플변수.sort()  가능한가? AttributeError
# 튜플변수.reverse()  가능한가? AttributeError

myTuple = (100, 200, 100, 'Python', 'MySQL', True, 100)
print('100의 빈도수는? ', myTuple.count(100))
print('첫번째 100값의 위치 인덱스값은? ', myTuple.index(100))

# 캐스팅
print('-'*100)
# 문자열 => 튜플 : tuple(문자열변수나 값)
# 리스트 => 튜플 : tuple(리스트변수나 값)
# 튜플 => 리스트 : list(튜플변수나 값)

txt = 'abcd'
myList = [10, 20, 30]
myTuple = ('강아지', '고양이', '코끼리')

result1 = tuple(txt); print(result1, type(result1))
result2 = tuple(myList); print(result2, type(result2))
result3 = list(myTuple); print(result3, type(result3))

# 튜플 => 문자열
# : str(튜플변수나 값)
# : 구분자.join(튜플변수나 값)
#  주의사항은 join() 사용시에는 튜플의 자료형이 문자열이어야 한다.

myTuple = ('강아지', '고양이', '코끼리')
txt1 = ' , '.join(myTuple)
txt2 = str(myTuple)
print(txt1, type(txt1), len(txt1))
print(txt2, type(txt2), len(txt2))

# 튜플 리스트란?
# 리스트안에 튜플이 삽입되어 있는 구조
# 이중 튜플 = 중첩튜플 : 튜플 안에 튜플이 삽입되어 있는 구조

t1 = [(10, 20, 30), (40, 50, 60)]
t2 = ((10, 20, 30), (40, 50, 60))

print(t1, type(t1))
print(t2, type(t2))
print(t1[0], t1[0][0])
print(t2[0], t2[0][0])

# 딕셔너리
print('-'*100)
# CRUD : Create Read Update Delete
# 딕셔너리 생성 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능

# 딕셔너리 생성 - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키값]=값

dict1 = {'a':'apple','b':'banana','c':'cat'}
dict2 = {100:'일백',200:'이백',300:'삼백'}

print(dict1, type(dict1), len(dict1))
print(dict2, type(dict2), len(dict2))

dict3 = {}
dict3['가'] = '가지'; dict3[100] = '백'
print(dict3, type(dict3), len(dict3))

# 딕셔너리 요소 조회 : 인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시

print(dict3['가'])
print(dict3[100])

# 리스트, 튜플처럼 숫자 인덱싱이 가능할까?
# KeyError : 딕셔너리는 키값으로만 호출가능

# 리스트, 튜플처럼 슬라이싱이 가능할까?
# TypeError 딕셔너리는 슬라이싱이 불가능
# print(f'dict3[0:2] = {dict3[0:2]}')

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
dict1 = {'a':'apple','b':'banana','c':'cat','a':'apart','cc':'cat'}
print(dict1['a'])
print(dict1['c'])
print(dict1['cc'])

# 딕셔너리 값 교체
# 딕셔너리[키값]=값

dict1['b'] = 'base'
print(dict1)

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수
# del 딕셔너리변수[키값]

dict1.pop('cc')
print(dict1)
del dict1['a']
print(dict1)
dict1.clear()
print(dict1)

# 딕셔너리 함수
# 딕셔너리변수.values() : 값 만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)...

sports = {'축구':'박지성','야구':'강정호','체조':'손연제'}
print(sports.values())
print(sports.keys())
print(sports.items())

print(list(sports.values()))
print(list(sports.keys()))
print(list(sports.items()))

# 캐스팅
print('-'*100)
# 리스트 => 딕셔너리(인덱싱숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시

menuList = ['만두','순두부','제육볶음']
print(menuList)
print(enumerate(menuList))
print(dict(enumerate(menuList)),type(dict(enumerate(menuList))))

# 딕셔너리 => 문자열
# str(딕셔너리변수) => {...}
# 구분자.join(딕셔너리변수) => 키값으로 생성된 문자열

sports = {'축구':'박지성','야구':'강정호','체조':'손연제'}
print(' '.join(sports))
print(' '.join(sports.values()))
print(' / '.join(list(sports.values())))

# 딕셔너리 => 튜플
# tuple(딕셔너리) => 키값으로 구성된 튜플 생성

print(tuple(sports))
print(list(sports))

# 딕셔너리 리스트
print('-'*100)
# 리스트안에 딕셔너리가 있는 구조
dictList = [{'a':'apple', 'v':'victory'},
            {100:'백', 200:'이백'},
            {'user1':'김철수', 'user2':'고소영'}]
print(dictList, type(dictList))
print(dictList[0])
print(dictList[0]['a'])

# 집합
print('-'*100)
# {값1, 값2, 값3....}
# CRUD :
# Create, Read(전체조회만 가능), Update, Delete

# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# 중복 데이터는 불가능

s1 = set([-90, 34, 45, 56, 100, 100, 100])
s2 = {'a', 'b', 'c', 'd', 'e'}
print(s1, type(s1))
print(s2, type(s2))

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])

s3 = {} # dict로 인식
print(s3, type(s3))
s4 = set() # set([])
print(s4, type(s4))
s4.add('python'); s4.add('pandas')
print(s4)
s4.update([100, 200, 300])
print(s4)

# 집합의 요소 삭제
# 집합변수.remove(값)
# del 집합변수 => 메모리에서 삭제

s4.remove(300)
print(s4)

# 집합의 연산
# +, * => 불가능
print('-'*100)

s1 = {'최', '김', '선우', '박', '이'}
s2 = {'신', '왕', '선우', '윤', '이'}

# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)

print(s1|s2)
print(s1.union(s2))

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)

print(s1-s2)
print(s1.difference(s2))

# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)

print(s1&s2)
print(s1.intersection(s2))

# 대칭차집합

print(s1^s2)

# 캐스팅
print('-'*100)
# 집합 => 리스트 : ist(집합변수)
# 집합 => 튜플 : tuple(집합변수)
# 리스트,문자열,튜플 => 집합 : set(리스트,문자열,튜플)

print(list(s1))
print(tuple(s1))


