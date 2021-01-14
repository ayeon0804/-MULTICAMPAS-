#1.  입력받은 데이터에 따라 양수, 음수, 숫자가 아니다 형태로 출력하세요.
#  조건 :
# 입력받은 데이타가 0인 경우에는 메세지를 출력하지 않는다.
# 입력값에 공백이 있는 경우 공백은 삭제한다. - 문자열변수.strip() : 좌우공백 삭제

# 데이타를 입력하세요...파이썬
# 숫자가 아니다

# 데이타를 입력하세요...- world
# 숫자가 아니다

# 데이타를 입력하세요...-90
# 음수

# 데이타를 입력하세요...9000
# 양수

data = input('데이타를 입력하세요...')
data = data.strip().replace(' ','')
if data.isdigit():
    if int(data) > 0:
        print("양수")
    else:
        pass
elif data[0] == '-':
    if data[1:].isdigit():
        print("음수")
    else:
        print("숫자가 아니다")
else:
    print("숫자가 아니다")

# 2. bmi 값에 따라 다음과 같은 메세지를 출력하세요
print('-'*100)
'''
# 키를 입력해주세요... 단위 cm...175
# 체중을 입력해주세요... 단위 kg...67
# bmi = 21.8776
# 정상
'''


# bmi 공식
# k = 키(입력값) 단위 cm
# w = 체중(입력값) 
# bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

# bmi 값에 따라 출력되는 메세지
# 고도 비만 : 35 보다 클 경우 
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만 
# 저체중 : 18.5 미만

k = int(input('키를 입력해주세요... 단위 cm...'))
w = int(input('체중을 입력해주세요... 단위 kg...'))
bmi = w/(k/100)**2
print(f'bmi = {bmi:.4f}')

if bmi > 35:
    print("고도 비만")
elif bmi > 30:
    print("중등도 비만")
elif bmi > 25:
    print('경도 비만')
elif bmi> 23:
    print('과체중')
elif bmi > 18.5:
    print('정상')
else:
    print('저체중')

# 3.# 입력받은 나이에 따라 메세지를 출력하세요
print('-'*100)
#  age > 19 : 성인
#  17 <= age <= 19 : 고등학생
#  14 <= age < 17 : 중학생
#  8 <= age < 14 : 초등학생
#  age < 8  : 유치원생 또는 영유아
# 
'''
# 당신의 나이를 입력해주세요 ... 12
#
# 당신은 초등학생 입니다.
 '''

age = int(input('당신의 나이를 입력해주세요 ... '))

if age > 19:
    print('당신은 성인입니다')
elif age >= 17:
    print('당신은 고등학생입니다')
elif age >= 14:
    print('당신은 중학생입니다')
elif age >= 8:
    print('당신은 초등학생입니다')
else:
    print('당신은 유치원생 또는 영유아입니다')

# 4. 학점을 입력받아서 다음과 같은 메세지를 출력하세요
print('-'*100)
# score = float(input("학점 입력> "))
# if ~ elif ~ else 문 이용하여 메세지 출력
#
# 4.2 <= score <= 4.5 : 교수님의 사랑
# 3.5 <= score < 4.2 : 현 체제의 수호자
#  2.8 <= score < 3.5 : 일반인
# 2.3 <= score < 2.8  : 일탈을 꿈꾸는 소시민
# 2.3 미만 : 시대를 앞서가는 혁명의 씨앗
#
# '''
# 학점 입력> 4.5
#
# score = 4.5   : 교수님의 사랑
#
# '''

score = float(input("학점 입력> "))
if 4.2 <= score <= 4.5:
    msg = '교수님의 사랑'
elif 3.5 <= score < 4.2:
    msg = '현 체제의 수호자'
elif 2.8 <= score < 3.5:
    msg = '일반인'
elif 2.3 <= score < 2.8:
    msg = '일탈을 꿈꾸는 소시민'
else:
    msg = '시대를 앞서가는 혁명의 씨앗'

print('score =', score, '\t :', msg)

# 5. 세 개의 숫자를 입력받아 리스트로 구성하고 가장 큰 수를 출력하세요.
print('-'*100)
#
# '''
# 첫번째 숫자 입력 => 100
# 두번째 숫자 입력 => 59
# 세번째 숫자 입력 => 70
# numList = [100, 59, 70]
# 가장 큰 수는 100 입니다.
#
# 첫번째 숫자 입력 => 50
# 두번째 숫자 입력 => 70
# 세번째 숫자 입력 => 90
# numList = [50, 70, 90]
# 가장 큰 수는 90 입니다.

num1 = int(input('첫번째 숫자 입력 => '))
num2 = int(input('두번째 숫자 입력 => '))
num3 = int(input('세번째 숫자 입력 => '))
numList = [num1, num2, num3]
numList.sort()
print(f'가장 큰 수는 {numList[-1]} 입니다.')

# 6. 가장 큰 수와 가장 작은 수를 출력하고 리스트에서 삭제한 후 출력하세요
print('-'*100)
'''
Before =  [100, 200, 50, -30, 999, 10, -30]
최대값은? 999
최솟값은? -30
Result =  [100, 200, 10, 50]
'''

Before = [100, 200, 50, -30, 999, 10, -30]
Before = set(Before)

max_val = 0
for val in Before:
    if max_val < val:
        max_val = val

min_val = 0
for val in Before:
    if min_val > val:
        min_val = val

print('최대값은?', max_val)
print('최솟값은?', min_val)
Result = list(Before)
Result.remove(min_val)
Result.remove(max_val)
print('Result = ', Result)

# 7. 딕셔너리 값에 'a' 글자가 있는 아이템만 표시하고 총 갯수를 출력하세요
print('-'*100)
# dict2 = {'a': 'africa', 's': 'say',
#         'c': 'coffee', 'd': 'drama', 'y':'yes'}

dict2 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}

sum_a = 0
for item in dict2.values():
    if item.find('a') != -1:
        print(item, end='\t')
        sum_a += 1

print()
print('a가 포함된 글자의 총 갯수 :', sum_a)


# 8. 다음 리스트 중에서 '을' 글자를 제외하고 출력하세요.
print('-'*100)
# for, if 이용
# '''
# qList = ['갑', '을', '병', '정']
# 갑 / 병 / 정 /
# '''

qList = ['갑', '을', '병', '정']
for q in qList:
    if q == '을':
        qList.remove('을')

newList = ' / '.join(qList)
print(newList)

# 9. 1부터 30까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
print('-'*100)
#  반복문 for와 조건문 사용
'''
 Result -------------------- 

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 
'''

i = 0
while i < 50:
    i += 1
    if i % 2 == 1:
        print(i, end=' ')
print()
# 10. 1부터 50까지 자연수 중 6의 배수만 리스트로 생성하고 다음과 같이 출력 하세요.
print('-'*100)
#  반복문 while,  조건문 사용
#  result = []
'''
Result --------------------
결과 리스트 = [6, 12, 18, 24, 30, 36, 42, 48]
총합 = 216
'''

resultList = []
i = 0
while i <= 50:
    i += 1
    if i % 6 == 0:
        resultList.append(i)
print('결과 리스트 =', resultList)

sum_six = 0
for i in resultList:
    sum_six += i

print('총합 =', sum_six)

# 11. 다음 리스트에서 평균, 합, 최소값을 출력하세요
print('-'*100)
# 리스트 : [95, 77, 56, 100, 85]
# 합 : 413
# 평균 : 82.60
# 최소값 : 56

myList = [95, 77, 56, 100, 85]
sumList = 0
for i in myList:
    sumList += i

print('합 :', sumList)
avg = sumList/len(myList)
print(f'평균 : {avg:.2f}')
myList.sort()
print('최소값 :', myList[0])

# 12. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
print('-'*100)
# 제어문과 len() 이용
# qList2 = ["nice", "study", "python", "anaconda", "!"]

qList2 = ["nice", "study", "python", "anaconda", "!"]
for q in qList2:
    if len(q) >= 5:
        print(q)

# 13. 다음과 같은 wordList 에서 첫 글자만 추출하여 keyList 리스트를 만들고
# #   두개의 리스트 조합으로 다음과 같은 딕셔너리를 만들어 출력하세요
print('-'*100)
# '''
# wordList = ['nice', 'study', 'python', 'anaconda', 'mySQL']
# keyList = ['n', 's', 'p', 'a', 'm']
# Result ------------------------------
#  dictList = {'n': 'nice', 's': 'study', 'p': 'python', 'a': 'anaconda', 'm': 'mySQL'}
# '''

wordList = ['nice', 'study', 'python', 'anaconda', 'mySQL']
keyList = []

for word in wordList:
    keyList.append(word[0])

dictList = dict()

for key in keyList:
    for word in wordList:
        if key == word[0]:
            dictList[key] = word

print(dictList)


# 14. 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하세요.
print('-'*100)
'''
[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
 총 22 개
'''

myList = [i for i in range(1, 101) if (i % 11 == 0) | (i % 7 == 0)]
print(myList)
print('총',len(myList),'개')

# 15. 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여 보세요
print('-'*100)
# ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']

myList = ['%d - %d' %(i,j) for i in range(1,6) for j in range(1,4)]

print(myList)

# 16. 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여 보세요'
print('-'*100)
# employees = [
#                 ['김수철', '서울', 25, '남', '총무부'],
#                 ['고길동', '부산', 33, '남', '회계부'],
#                 ['최미나', '대전', 22, '여', '기획부'],
#                 ['은지원', '서울', 44, '남', '영업부'],
#                 ['김영탁', '울산', 36, '남', '영업부'],
#                 ['마동탁', '대구', 50, '남', '기획부'],
#                 ['이은미', '창원', 42, '여', '총무부']
#               ]
#
# 	----------------------------------------
#  	 사원명 	 출신지 	 나이 	 성별 	 부서
# 	----------------------------------------
#  	 김수철 	 서울 	 25 	 남 	 총무부
#  	 고길동 	 부산 	 33 	 남 	 회계부
#  	 최미나 	 대전 	 22 	 여 	 기획부
#  	 은지원 	 서울 	 44 	 남 	 영업부
#  	 김영탁 	 울산 	 36 	 남 	 영업부
#  	 마동탁 	 대구 	 50 	 남 	 기획부
#  	 이은미 	 창원 	 42 	 여 	 총무부

employees = [
                 ['김수철', '서울', 25, '남', '총무부'],
                 ['고길동', '부산', 33, '남', '회계부'],
                 ['최미나', '대전', 22, '여', '기획부'],
                 ['은지원', '서울', 44, '남', '영업부'],
                 ['김영탁', '울산', 36, '남', '영업부'],
                 ['마동탁', '대구', 50, '남', '기획부'],
                 ['이은미', '창원', 42, '여', '총무부']
               ]
print('-'*50)
print('사원명 \t 출신지 \t 나이 \t 성별 \t 부서')
print('-'*50)

for i in employees:
    print(i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t', i[4])

# 17. 16번의 리스트에서 남자 사원 목록만 출력하여 보세요.
print('-'*100)

for i in employees:
    if i[3] == '남':
        print(i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t', i[4])

# 18. 16번의 리스트에서 성이 '김'인 사원 목록만 출력하여 보세요.
print('-'*100)

for i in employees:
    if i[0][0] == '김':
        print(i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t', i[4])
