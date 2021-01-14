import os

# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949') as 파일변수:
#   명령문

# 1~5행 쓰기
with open('data/national_anthem.txt', 'r') as f:
    data_list = f.readlines()
    for row in data_list[:3]:
        print(row)

# 10~1까지 특정파일에 쓰기
with open('data/sample_100.txt', 'w', encoding='utf-8') as f:
    for i in range(10, 0, -1):
        f.write(str(i) + '\n')

# 특정파일에 내용 추가하기
# 구구단
with open('data/sample_100.txt', 'a', encoding='utf-8') as f:
    for i in range(2,10):
        f.write(f'=== {i}단 ===\n')
        for j in range(1,10):
            f.write(f'{i} X {j} = {i*j} \n')