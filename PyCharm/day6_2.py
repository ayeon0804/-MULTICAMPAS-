import os
def read_file(url, enc):
    f = open(url, 'r', encoding=enc) # encoding : utf-8 또는 cp949
    result = f.read()
    f.close()
    return result

print('-'*100)
print(read_file('data/national_anthem.txt', 'cp949'))
print('-'*100)
print(read_file('data/coding.txt', 'utf-8'))


def printWord(url, enc):
    f = open(url, 'r', encoding=enc)
    result = f.read()
    f.close()
    result_list = list(set(result.split()))
    print(f'파일명 : {url}')
    print(f'단어 갯수 : {len(result_list)}')
    print(f'단어 5개 출력 : {result_list[:5]}')

printWord('data/Yesterday.txt','cp949')

# 퀴즈
# data_eng.txt, data_kor.txt
# 파일에 삽입된 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
# 함수 정의 => 파일읽기 => 리스트화
# => 리스트의 값 더하기(숫자형데이터로 변환) : 합
# => 합 / 리스트갯수 : 평균

# '''
# # 함수 호출
# sumAvr('data/data_eng.txt', 'cp949')
# sumAvr('data/data_kor.txt', 'cp949')
#
# >> 결과
#
# 파일명 =  data/data_eng.txt
# 데이터 수 =  12
# 합 =  933
# 평균 = 77.75
#
# ----------
# 파일명 =  data/data_kor.txt
# 데이터 수 =  12
# 합 =  892
# 평균 = 74.33
#
# '''

def sumAvr(url, enc):
    f = open(url, 'r', encoding=enc)
    socre_list = f.readlines()
    f.close()

    tot = 0
    for item in socre_list:
        tot += int(item)
    print('-'*100)
    print(f'총합 : {tot}')
    print(f'평균 : {(tot/len(socre_list)):.2f}')

sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')

# 파일 쓰기
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

print(os.getcwd()) # C:\Users\pc\PycharmProjects\pythonProject

# 특정 위치에 빈 파일 생성하기

f = open('sample_0.txt', 'w')
f.close()

# 작업 위치 이동

os.chdir('data')
print(os.getcwd())

os.chdir('../')
print(os.getcwd())

# 특정 파일에 내용 쓰기
# 기존 파일 목록이 있다면 덮어쓴다.
print(os.getcwd())
# 지정한 폴더가 없다면 에러 발생 : FileNotFoundError

f = open('sample_1.txt', 'w', encoding='utf-8')
f.write('='*50+'\n')
f.write('사과\n')
f.write('과수원\n')
f.write('원숭이\n')
f.close()

# 반복문 이용해서 파일에 내용추가하기
myFoodList = ['라면', '김치전', '모밀', '초밥', '샐러드']

f = open('munu.txt', 'w', encoding='utf-8')
count = 1
for item in myFoodList:
    f.write(str(count) + ' => ' + item + '\n')
    count += 1
f.close()

# 퀴즈 :
# data/Yesterday.txt 파일에서 10줄만
# data/result_Yesterday.txt 파일에 저장하기
# 작업 과정
# 파일 읽기
# 리스트 구조로 저장
# 슬라이싱 = 리스트변수[0:10]
# 파일 쓰기

f = open('data/Yesterday.txt', 'r', encoding='utf-8')
result = []
for i in range(10):
    result.append(f.readline().replace('\n',''))
f.close()

f = open('data/result_Yesterday.txt', 'w', encoding='utf-8')

for i in range(len(result)):
    f.write(result[i] + '\n')

f.close()

# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

# 빈 파일에 내용추가하기
f = open('sample_0.txt', 'w')
f.write('========== Start 1 ==========')
f.close()

f = open('sample_0.txt', 'a')
f.write('\n========== Start 2 ==========')
f.close()

# 기존 파일에 입력받은 내용 추가하기
f = open('sample_0.txt', 'a', encoding='utf-8')
while True:
    item = input('데이타 삽입(q 는 프로그램 종료)d == > ')
    if item == 'q':
        break
    else:
        f.write('\n' + item)
print('테스트 종료')
f.close()

# 파일 내용 삭제
f= open('sample_0.txt', 'w', encoding='utf-8')
f.close()

# 파일 삭제
ans = input('파일을 삭제하시겠습니까? ...')
if ans.upper() == 'Y':
    os.remove('sample_1.txt')

# 파일이 있다면 삭제
# 없다면 메세지 출력
print(os.listdir())
print('*'*50)
remove_file = 'sample_0.txt'
if remove_file in os.listdir():
    ans = input('파일을 삭제하시겠습니까? ...')
    if ans.upper() == 'Y':
        os.remove(remove_file)
        print('파일이 삭제되었습니다.')
else:
    print('파일 목록이 없습니다. 삭제가 불가능합니다.')

