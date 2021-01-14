# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~elif~else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다

# 조건문 if

flag = 123 # 숫자의 경우 0인 경우는 False, 나머지는 모두 True
if flag:
    print('if문 실행')

flag1 = '' # 문자열의 경우 ''(공백과 다름)가 아닌 문자열 모두 True
if flag1:
    print('if문 실행1')

flag2 = {} # ([], (), {}) 가 아닌 집합형 자료. 즉, 길이가 0이 아닌 집합형 자료
if flag2:
    print('if문 실행2')

# 비교 연산자나 논리연산자를 이용한  if 문
# 비교연산자 : >, <, <=, >=, !=, ==
# 논리 연산자 : and, or, not
# 수의 비교

x = 10
y = 10
if x>y:
    print('x가 크다')
if x<y:
    print('y가 크다')
if x==y:
    print('x와 y가 같다')

# 조건문 1 - 단순 if 문
# if 조건:
#   명령문

# 조건문 2
# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

# 돈이 있으면(0이 아닌 숫자) 택시를 타고, 돈이 없으면(0) 걸어 간다
money = 0
if money:
    print('택시를 타고 간다.')
else:
    print('걸어간다')

# 조건문 3 - 다중 if문
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3

# 숫자값이 0, 음수, 양수 인지 출력
x = 10
if x>0:
    print(f'{x}는 양수')
elif x<0:
    print(f'{x}는 음수')
else:
    print(f'{x}는 0')

# 퀴즈 :
# 나이를 입력받아서
# 나이에 따라서 서로다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...
~7 : 영유아 
8 ~ 13 : 초등학생
14 ~ 16 : 중학생
17 ~ 19 : 고등학생
20 ~ : 성인
'''

age = int(input('당신의 나이를 입력해주세요? ...'))
if age <= 7:
    print("영유아")
elif age <= 13:
    print("초등학생")
elif age <= 16:
    print("중학생")
elif age <= 19:
    print("고등학생")
else:
    print("성인")

# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
'''
태어난 년도를 입력하세요? 2009
당신은 소띠입니다.
'''

# 문자열이 숫자,영문형태?
# 문자열.isdigit() : 문자열이 숫자이면 True
# 문자열.isdecimal() : 문자열이 숫자이면 True
# 문자열.isalpha() : 문자열이 영문글자이면 True
# 문자열.isalnum() : 문자열이 영문글자 또는 숫자 형태이면 True

txt1 = '123'
txt2 = 'python33'
txt3 = '!!**345'
print(txt1.isdigit())
print(txt2.isdigit())
print(txt1.isdecimal())
print(txt1.isalpha())
print(txt2.isalnum())
print(txt3.isalnum())

# 숫자를 입력받아서 0, 양수, 숫자가 아니다.
# 입력받은 데이타가 숫자이면 데이터형 변경, 그렇지 않으면 메세지 출력
ans = input('숫자를 입력해주세요 : ')
if ans.isdigit():
    if int(ans) > 0:
        print('양수')
    else:
        print(0)
else:
    print(ans, '는 숫자가 아닙니다.')

#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False
print('-'*100)
cityList = ['서울', '부산', '대구']
txt = 'abcdefg'

print('서울' in cityList)
print('대전' in cityList)
print('a' not in txt)
print('a' in txt)

# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3
print('-'*100)

twice = ['나연', '채영', '쯔위']
# member = '조이'
member = '쯔위'
if member in twice:
    print(f'{member} 은(는) 트와이스이다.')
else:
    print(f'{member} 은(는) 트와이스 멤버가 아니다.')

# pass 키워드 이용하기
# 명령문의 일종으로 비실행
# 함수, 클래스 생성시 등록만 시킬때 사용

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
