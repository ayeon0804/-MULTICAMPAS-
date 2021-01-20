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
cursor = conn.cursor()
# slq 명령 실행
cursor.execute('SELECT userID, prodName, groupName, price, amount FROM buyTbl')
# 데이타 저장
buyTbl_data = cursor.fetchall()
for row in buyTbl_data[:5]:
    print(row)
print(buyTbl_data)

# 데이타프레임으로 저장
df = pd.DataFrame(buyTbl_data,
                  columns=['userID', 'prodName', 'groupName', 'price', 'amount'])
print(df)

# 디렉토리 생성
try:
    os.mkdir('output')
except:
    pass

# csv 저장
df.to_csv('output/buyTbl.csv', index=False)

# 접속 종료
conn.close()
