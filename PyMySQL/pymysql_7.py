# csv(data.csv) => 2차원리스트 => MySQL
# MySql => 데이타프레임 => csv

# 모듈 임포트
import pymysql
import pandas as pd
import csv
import os

# 데이타베이스 접속
conn = pymysql.connect( host = 'localhost',
                        port=3306,
                        user='root',
                        password = '1234',
                        db = 'sqlDb',
                        charset = 'utf8')

# csv(data.csv) => 2차원 리스트
# data/data.csv
with open(r'C:\Users\pc\PycharmProjects\pythonProject\data\data.csv') as f:
    csv_data = csv.reader(f)
    data_list = list(csv_data)

print(type(data_list)) # <class 'list'>
print(type(data_list[0])) # <class 'list'>
print(data_list[0]) # ['class', 'name', 'kor', 'eng', 'mat', 'bio']
print(data_list[1]) # ['1', 'adam', '67', '87', '90', '98']
for row in data_list:
    print(row)

print(len(data_list)) # 13

# 커서 생성
cursor = conn.cursor()

# mySQL에서 dataTbl 테이블 생성
'''
id int -- 기본키, 자동증감 
class int -- 반  
name varchar(10) -- 학생이름
kor int
eng int
mat int
bio int
'''
sql = 'DROP TABLE IF EXISTS dataTbl;'
cursor.execute(sql)

sql = '''CREATE TABLE dataTbl 
        (
            id int PRIMARY KEY AUTO_INCREMENT NOT NULL, 
            class int NOT NULL,  
            name varchar(10) NOT NULL,
            kor int NOT NULL,
            eng int NOT NULL,
            mat int NOT NULL,
            bio int NOT NULL
            );
        '''
cursor.execute(sql)

# 레코드 삽입
for row in data_list[1:]:
    sql = ''' INSERT INTO dataTbl (class, name, kor, eng, mat, bio)
                VALUES (%s, %s, %s, %s, %s, %s); '''
    cursor.execute(sql, row)

# 데이타베이스 반영
conn.commit()

# MySQL 파일의 테이블 => 데이타프레임
# cursor 객체 생성
# 작업변수 커서 생성 (딕셔너리 리스트구조) => dict cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

# slq 명령 실행
cursor.execute(''' SELECT id, name, kor, eng, mat, bio 
                         FROM dataTbl ORDER BY name;
               ''')

# 데이타 저장
dataTbl_data = cursor.fetchall()

# 데이타프레임으로 저장
df = pd.DataFrame(dataTbl_data)
print(df)

# csv 저장
df.to_csv('output/dataTbl_data.csv', index=False)

# 접속 종료
conn.close()
