# 사용자정의 에러
#  raise 문 이용
# 일부러 에러 발생
# if 조건식:
#   raise Exception(오류 메세지)

# 입력값이 0이면 오류 발생
# x = input('0이 아닌 문자를 입력하세요')
# if x == '0':
#     raise Exception('입력 에러 => 입력값이 0입니다. ')
# else:
#     print(f' x = {x}')
# print('사용자정의 에러 테스트')

# try..except.. + raise Exception
# 사용자정의 에러에 대해서도 예외처리하기

# 입력값이 0이면 오류 발생
# try:
#     x = input('0이 아닌 문자를 입력하세요...')
#     if x == '0':
#         raise Exception('입력 에러 => 입력값이 0입니다. ')
# except Exception as e:
#     print(e)
# else:
#     print(f' x = {x}')
# print('사용자정의 에러 테스트 종료')



# data = input('데이타 입력 => ')
# if (data[0] == '-') and (data[1:].isdigit()):
#     # print(f'{data} => 음수')
#     raise Exception('입력 에러')



# 입력값이 음수이면 에러발생
# 음수는 - 와 나머지는 0이 아닌 숫자
# -0 은 0으로 출력
try:
    data = input('데이타 입력 => ')
    if (data[0] == '-') and (data[1:].isdigit()) and (data[1] != '0' ):
        raise Exception('입력 에러')
    elif (data[0] == '-') and (data[1] == '0'):
        data = 0
except Exception as e:
    print(e)
else:
    print(f' x = {data}')
print('사용자정의 에러 테스트 종료')

# 사용자정의 에러
# 에러코드 + 에러 메세지 등록
# Exception 클래스 상속받아서 에러코드 등록

# 1단계 : 사용자 에러코드 등록
# Exception 내장 클래스를 상속받아
# 임의의 에러명으로 클래스 생성
# class 에러명클래스(Exception):
#       명령문
# 사용자정의 에러
# 에러코드 + 에러 메세지 등록
# Exception 클래스 상속받아서 에러코드 등록

# 1단계 : 사용자 에러코드 등록
# Exception 내장 클래스를 상속받아
# 임의의 에러명으로 클래스 생성
# class 에러명클래스(Exception):
#       명령문

# 에러 코드 + 에러 메세지 등록
class MyError(Exception):
    def __str__(self):
        return 'MyError => 사용자정의 에러 발생'

# 2단계
# 에러 발생시 에러코드 호출
# raise 에러코드클래스명()

# 입력값이 0이면 오류 발생
x = input('0이 아닌 문자를 입력하세요...')
try:
    if x == '0':
        raise MyError()
except MyError as e:
    print(e)
else:
    print(f' x = {x}')
finally:
    print('사용자정의 에러 테스트')

# 닉네임 금칙어 에러 코드 만들기
# 닉네임 금칙어 - 바보

class NicknameError(Exception):
    def __str__(self):
        return '닉네임 금칙어 에러 - 닉네임으로 사용할 수 없습니다.'

# 함수 정의
def check_nickname(nickname):
    stop_nickname_list = ['바보', '악마', '멍청이']
    if nickname in stop_nickname_list:
        raise NicknameError()
    else:
        return f'{nickname} 승인 완료'

try:
    print(check_nickname('스머프'))
    print(check_nickname('악마'))
except NicknameError as e:
    print(e)