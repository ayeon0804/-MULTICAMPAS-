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
                        charset = 'utf8')

with open(r'C:\Users\pc\PycharmProjects\pythonProject\data\seoul.csv') as f:
    csv_data = csv.reader(f)
    seoul_list = list(csv_data)

fieldList = seoul_list[0]

# 실제 데이타로 재정의
seoul_list = seoul_list[1:]

print('전처리 전 상태 데이타 갯수 : ', len(seoul_list)) # 39926

# 전처리 - Null 제외
seoul_result_list = []
for a, b, c, d, e in seoul_list:
    if c and d and e:
        seoul_result_list.append([a, c, d, e])

print('전처리 후 상태 데이타 갯수 : ', len(seoul_result_list)) # 39168

# 데이타베이스 테이블 저장
cursor = conn.cursor()

sql = 'DROP TABLE IF EXISTS seoulTbl;'
cursor.execute(sql)

sql = '''CREATE TABLE seoulTbl (
            id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
            day date,
            avg char(5),
            min char(5),
            max char(5)
            );'''
cursor.execute(sql)

# 레코드 삽입
for row in seoul_result_list:
    sql = ''' INSERT INTO seoulTbl (day, avg, min, max)
                VALUES (%s, %s, %s, %s); '''
    cursor.execute(sql, row)

# 데이타베이스 반영
conn.commit()

cursor.execute('SELECT count(*) FROM seoulTbl')
print(cursor.fetchone()[0], '개 레코드 생성')

# MySQL 파일의 테이블 => 데이타프레임
# cursor 객체 생성
# 작업변수 커서 생성 (딕셔너리 리스트구조) => dict cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

# slq 명령 실행
cursor.execute(''' SELECT id, day, avg, min, max FROM seoulTbl;''')

# 데이타 저장
seoulTbl_data = cursor.fetchall()

# 데이타프레임으로 저장
df = pd.DataFrame(seoulTbl_data)
print(df)

# csv 저장
df.to_csv('output/seoulTbl_data1.csv', index=False)

# 데이타베이스 종료
conn.close()