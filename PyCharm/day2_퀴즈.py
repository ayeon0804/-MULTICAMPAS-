'''
2개의 리스트를 정의하고 다음과 같이 출력한다.
myList1 : ['홍길동', '신데렐라', '알라딘', '장화',
 '홍련', '지니', '엘리스']
myList2 : ['토끼', '거북이', '물개', '펭귄']
2개의 리스트 합 : (결과값 출력 )
4개만 출력 : (결과값 출력 )
짝수번째만 출력 : (결과값 출력 )
홀수번째만 출력 : (결과값 출력 )
총 길이 :  11
'''

# 퀴즈 1
myList1 = ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
myList2 = ['토끼', '거북이', '물개', '펭귄']

print(f'myList1 : {myList1}')
print(f'myList2 : {myList2}')

myList3 = myList1 + myList2

print(f'2개의 리스트 합 : {myList3}')
print(f'4개만 출력 : {myList3[0:4]}')
print(f'짝수번째만 출력 : {myList3[1::2]}')
print(f'홀수번째만 출력 : {myList3[0::2]}')
print(f'총길이 : {len(myList3)}')

'''
리스트를 정의한 후 리스트 요소를 편집한다.
(변경, 삭제, 추가)
['사과', '배', '망고']
첫번째 요소 변경 후 : ['포도', '배', '망고']
마지막 위치에 요소 추가후 : ['포도', '배', '망고', '오렌지']
2번째 위치에 요소 추가후 : ['포도', '수박', '배', '망고', 
                        '오렌지']
마지막 위치 삭제 : ['포도', '수박', '배', '망고']
배 삭제 : ['포도', '수박', '망고']
'''

# 퀴즈 2
List = ['사과', '배', '망고']
List[0] = '포도'
print(f'첫번째 요소 변경 후 : {List}')
List.append('오렌지')
print(f'마지막 위치에 요소 추가후 : {List}')
List.insert(1,'수박')
print(f'2번째 위치에 요소 추가후 : {List}')
List.pop()
print(f'마지막 위치 삭제 : {List}')
List.remove('배')
print(f'배 삭제 : {List}')

'''
데이터를 입력받은 후 리스트에 추가하는 예제입니다.
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산
당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''

# 퀴즈 3
List = []
msg1 = input('좋아하는 음식은? '); List.append(msg1)
msg2 = input('최근 본 영화는? '); List.append(msg2)
msg3 = input('좋아하는 가수는? '); List.append(msg3)
msg4 = int(input('좋아하는 숫자? ')); List.append(msg4)
msg5 = input('최근 여행지? '); List.append(msg5)

print(f'당신에 관한 리스트 : {List}')

'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']

'''

# 퀴즈 4
foods = ['사과','망고','치즈케이크','주스']
print(f'우리집 냉장고에는? {foods}')
print(f'동생이 {foods.pop(0)}를 먹었다')
print(f'우리집 냉장고에는? {foods}')
foods.append('수박')
print(f'이모가 {foods[-1]}을 사오셨다.')
print(f'우리집 냉장고에는? {foods}')
foods.remove('치즈케이크')
foods.remove('수박')
print(f'동생 친구가 치즈케이크,수박을 먹었다')
print(f'우리집 냉장고에는? {foods}')

