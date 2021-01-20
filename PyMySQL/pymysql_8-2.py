# 퀴즈
# seoul.csv =>seoulTbl 테이블로 저장  => 데이타프레임 => CSV
# 서울의 기온 데이타 (1907-10 ~ 2018.3)
# 날짜 / 평균기온 / 최저기온 / 최고기온
# NULL 데이타 제외
import csv
import pymysql
import pandas as pd

conn = pymysql.connect( host = 'localhost',
                        port=3306,
                        user='root',
                        password = '1234',
                        db = 'sqldb',
                        charset = 'utf8' )

with open(r'C:\Users\pc\PycharmProjects\pythonProject\data\seoul.csv') as f:
    csv_data = csv.reader(f)
    seoul_list = list(csv_data)

fieldList = seoul_list[0]
seoul_list = seoul_list[1:]

# 전처리 1 - Null 데이타 삭제
seoul_result_list = []
for a, b, c, d, e in seoul_list:
    if c and d and e:
        seoul_result_list.append([a, c, d, e])

# 전처리 2 - 문자열 => 실수 (음수 처리)
seoul_result_list2 = []
for a, c, d, e in seoul_result_list:
    print(c, type(c))
    if c[0] == '-':
        temp1 = float(c[1:])*-1
    else :
        temp1 = float(c)

    if d[0] == '-':
        temp2 = -1 * float(d[1:])
    else :
        temp2 = float(d)

    if e[0] == '-':
        temp3 = -1 * float(e[1:])
    else :
        temp3 = float(e)

    seoul_result_list2.append([a, temp1, temp2, temp3])

cursor = conn.cursor()

sql = 'DROP TABLE IF EXISTS seoulTbl2;'
cursor.execute(sql)

sql = '''CREATE TABLE seoulTbl2 (
            id int PRIMARY KEY AUTO_INCREMENT NOT NULL, 
            day date,
            avg float(3,1),
            min float(3,1),
            max float(3,1)
            );'''
cursor.execute(sql)

# 레코드 삽입
for row in seoul_result_list2:
    sql = ''' INSERT INTO seoulTbl2 (day, avg, min, max)
                VALUES (%s, %s, %s, %s); '''
    cursor.execute(sql, row)

# 데이타베이스 반영
conn.commit()

cursor.execute('SELECT count(*) FROM seoulTbl2')
print(cursor.fetchone()[0], '개 레코드 생성')

# MySQL 파일의 테이블 => 데이타프레임
# cursor 객체 생성
# 작업변수 커서 생성 (딕셔너리 리스트구조) => dict cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

# slq 명령 실행
cursor.execute(''' SELECT id, day, avg, min, max FROM seoulTbl2;''')

# 데이타 저장
seoulTbl_data = cursor.fetchall()

# 데이타프레임으로 저장
df = pd.DataFrame(seoulTbl_data)
print(df)

# csv 저장
df.to_csv('output/seoulTbl_data2.csv', index=False)

# 데이타베이스 종료
conn.close()