# 퀴즈 1: FileNotFoundError
#  data/test.txt 가 없다면
#  에러메세지(e)와 함께 '파일이 없습니다.' 메세지 출력
#  있다면 파일의 내용을 출력한다.

try:
    f = open('data/test.txt', 'r')
except FileNotFoundError as e:
    print('에러 메세지 :', e, '파일이 없습니다.')
else:
    print(f.read())


# 퀴즈 2: ValueError
# 2개의 숫자글자를 입력받아서 더한다.
# 입력된 글자가 숫자가 아니라면 에러 메세지 출력
# 입력된 글자가 숫자라면  더한후 출력한다.

try:
    num1 = input('첫번째 숫자를 입력하세요 ... ')
    num2 = input('두번째 숫자를 입력하세요 ... ')

    sum_num = int(num1) + int(num2)
except ValueError as e:
    print('에러 메세지 :', e)
else:
    print(sum_num)


# 퀴즈 3 : ValueError, ZeroDivisionError
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?

try:
    n1 = int(input('첫번째 데이타를 입력하세요 ... '))
    n2 = int(input('두번째 데이타를 입력하세요 ... '))

    div = n1 / n2
except ValueError as e:
    print('에러 메세지 :', e, '데이타 오류...')
except ZeroDivisionError as e:
    print('에러 메세지 :', e, '데이타 오류...')
else:
    print(div)


# 퀴즈 4
# data_eng.txt 파일을 파일 변수로 저장한다.
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.

try:
    f = open('data/data_eng.txt', 'r')
    fileList = f.readlines()
except FileNotFoundError as e:
    print(e, '=> 파일없음')
else:
    fileSum = 0
    for num in fileList:
        fileSum += int(num)
    fileAvg = fileSum / len(fileList)

    print('총합 :', fileSum)
    print('평균 :', fileAvg)


# 퀴즈 5
# 함수의 매개변수값에 따라 다음과 같은 메세지를 출력한다.
# 0과 같거나 0보다 작다
# 0보다 크다
# 매개변수값이 숫자가 아닌경우에는 오류를 무시하도록
# try...except 문을 작성하여라


def input_num(par):
    try:
        num = int(par)
    except Exception as e:
        pass
    else:
        if par <= 0:
            print('0과 같거나 0보다 작다.')
        elif par > 0:
            print('0보다 크다.')



input_num(-3)
input_num(5)
input_num('가')

# 퀴즈6
# 학생의 학년을 저장하는 변수 classYear값은
# 1학년, 2학년, 3학년, 4학년 이어야한다.
# 나머지 값은  raise Exception 을
# 이용하여 오류를 발생시켜라

while True:
    try:
        classYear = input('학년을 입력하세요')
        if len(classYear) != 3:
            raise Exception('다시 입력해 주세요.')
        if classYear[0] not in ('1','2','3','4'):
            raise Exception('다시 입력해 주세요.')
        if classYear[1:3] != '학년':
            raise Exception('다시 입력해 주세요.')
        else:
            print('학년이 저장되었습니다.')
            break
    except Exception as e:
        print(e)



