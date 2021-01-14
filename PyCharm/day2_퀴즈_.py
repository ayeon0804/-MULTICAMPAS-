# 1. a, b, c, d, e를 저장하는 튜플을 정의하고
# 첫 번째 튜플값과 마지막 튜플값을 출력하여라.

tuple1 = ('a', 'b', 'c', 'd', 'e')
print(tuple1[0], tuple1[-1])

# 2. 다음 리스트에서 "Apple" 항목만 삭제하여라. : ["Banana", "Apple", "Orange"]

List2 = ["Banana", "Apple", "Orange"]
List2.remove("Apple")
print(List2)

# 3. 다음 튜플 데이터를 리스트 데이터로 변환한 후에 'fun-coding0' 데이터를 첫번째에 추가하고,
#    다시 튜플 데이터로 변환하여라.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
List3 = list(tupledata)
List3.insert(0, 'fun-coding0')
tuple3 = tuple(List3)
print(tuple3)

# 4. 다음 항목을 딕셔너리(dict)으로 선언하여라.
# : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dict4 = {'성인':100000, '청소년':70000, '아동':30000}
print(dict4)

# 5. 4번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dict4["소아"] = 0
print(dict4)

# 6. 5번의 딕셔너리(dict)에서 Key 항목만 리스트로 저장하여 정렬한 후 튜플로 변경하여라.
#  결과 => ('성인', '소아', '아동', '청소년')

List6 = list(dict4.keys())
List6.sort()
List6 = tuple(List6)
print(List6)


# 7. number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
#  number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]

number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
set7 = set(number_list)
List7 = list(set7)
print(List7)

# 8. 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}

set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}

set8 = set1.intersection(set2)
List8 = list(set8)
print(List8)

# 9. 8의 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
#  아이템1 / 아이템2 / ....

print(' / '.join(List8))

# 10. 빈 집합을 생성하고 값을 입력받아 집합의 원소를 삽입하여라. 집합 원소의 갯수는 5개로 한다.
'''
 mySet = set() <class 'set'>
첫번째 아이템 값 => 갈비탕
두번째 아이템 값 => 소머리국밥
세번째 아이템 값 => 삼계탕
네번째 아이템 값 => 순두부
다섯번째 아이템 값 => 김치찌게
 mySet = {'김치찌게', '소머리국밥', '갈비탕 ', '순두부', '삼계탕'} <class 'set'>
'''

set10 = set()
item1 = input("첫번째 아이템 값 => "); set10.add(item1)
item2 = input("두번째 아이템 값 => "); set10.add(item2)
item3 = input("세번째 아이템 값 => "); set10.add(item3)
item4 = input("네번째 아이템 값 => "); set10.add(item4)
item5 = input("다섯번째 아이템 값 => "); set10.add(item5)
print(set10)


# 11. 10의 집합을 다음과 같은 딕셔너리 구조로 변환하여라.

#  mydict =  {0: '소머리국밥', 1: '갈비탕', 2: '순두부', 3: '김치찌게', 4: '삼계탕'}
#  <class 'dict'>

dict11 = dict(enumerate(set10))
print(dict11)