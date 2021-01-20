# MYSQL 테이블 => 딕셔너리 리스트 => 데이타프레임  => csv

# 모듈 임포트
import pymysql
import pandas as pd
import csv
import os

# 데이타베이스 접속
conn = pymysql.connect( host = 'localhost',
                        port=3306, # mysql 포트
                        user='root', # 접속 계정
                        password = '1234', # 루트계정의 본인 비번
                        db = 'sqlDb',  # 접속하고자 하는 데이타베이스명
                        charset = 'utf8' )

# cursor 객체 생성
# 작업변수 커서 생성 (딕셔너리 리스트구조) => dict cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

# slq 명령 실행
cursor.execute('SELECT * FROM userTbl')

# 데이타 저장
userTbl_data = cursor.fetchall()

print(type(userTbl_data)) # <class 'list'>
print(type(userTbl_data[0])) # <class 'dict'>
print(userTbl_data[:5])
# mySQL 테이블안의 필드명 => 키
for row in userTbl_data[:3]:
    print(row)

# 접속 종료
conn.close()

# 데이타프레임으로 저장
df = pd.DataFrame(userTbl_data)
print(df)

# csv 저장
df.to_csv('output/userTbl_data.csv', index=False)
