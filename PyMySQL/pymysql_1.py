# MySQL 연동

import pymysql

# mysql의 계정의 특정 데이타베이스에 접속해서 연결 객체(conn) 생성
conn = pymysql.connect( host = 'localhost',
                        port = 3306, # mysql 포트
                        user = 'root', # 접속 계정
                        password = '1234', # 루트계정의 본인 비번
                        db = 'world', # 접속하고자 하는 데이타베이스명
                        charset = 'utf8')
print(conn)

# 커서(cursor) 객체 생성
cursor = conn.cursor()
print(cursor)

# sql 명령을 실행
# 커서(cursor)객체.execute(sql명령문)
# 테이블 조회
cursor.execute('SELECT * FROM city LIMIT 10;')

# sql 실행 결과 저장
# 변수명 = cursor.fetchall() / cursor.fetchone() / cursor.fetchmany(n)
result = cursor.fetchall()
print(result) # 2차원 튜플로 저장
for item in result:
    print(item)

# 데이타베이스 종료
# conn.close()

# =========================
# cursor.fetchone() => 튜플
# cursor.fetchall() => 2차원 튜플구조
# cursor.fetchmany(size) => 2차원 튜플구조

cursor.execute('''SELECT Code, Name, Continent, Population 
                    FROM country
                        ORDER BY Population DESC
                            LIMIT 20;''')
result1 = cursor.fetchone()
result2 = cursor.fetchall()
result3 = cursor.fetchmany(5)

print('-'*100); print(result1)
print('-'*100); print(result2)
print('-'*100); print(result3)

conn.close()
