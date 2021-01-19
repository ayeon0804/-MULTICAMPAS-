# sampleDb 데이타베이스 생성
# sampleDb 데이타베이스 사용
# movieTbl 테이블 생성
# 레코드 삽입

import pymysql

conn = pymysql.connect( host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '1234',
                        charset = 'utf8')

cursor = conn.cursor()

# 테이타베이스 생성
sql = 'CREATE DATABASE IF NOT EXISTS sampleDb;'
cursor.execute(sql)

# 테이타베이스 사용
sql = 'USE sampleDb;'
cursor.execute(sql)

# 테이블 생성
sql = '''
        CREATE TABLE IF NOT EXISTS movieTbl
        (
            movieNum int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
            movieName varchar(30) NOT NULL,
            kind varchar(30) NULL,
            price int NOT NULL,
            period int NOT NULL
        );
        '''
cursor.execute(sql)

# 레코드 삽입 1 : 필드명 지정 X
sql = '''INSERT INTO movieTbl VALUES (NULL, '토이스토리', '애니메이션', 3000, 5);'''
cursor.execute(sql)

# 데이타 베이스 반영(레코드 삽입, 삭제, 수정 후에는 적용과정 필요)
conn.commit()

# 레코드 삽입 2 : 필드명 지정 O
# sql변수 = '''  INSERT INTO 테이블명 (필드명1,...)
#                   VALUES(%s, .... ); '''
# cursor.execute(sql변수, (값1, ... ))
sql = ''' INSERT INTO movieTbl (movieName, kind, price, period)
            VALUES (%s, %s, %s, %s);'''
cursor.execute(sql, ('원더우먼','액션', 3000, 2))
conn.commit()

# 레코드 삽입 3 : 필드명 지정 O, 다중 레코드 삽입 방식
# sql변수 = '''  INSERT INTO 테이블명 (필드명1,...)
#                   VALUES(%s, .... ); '''

# 레코드 데이타를 2차원 튜플로 저장
# data = ( (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...), (값1, 값2 ...) ...)
# cursor.executemany( sql변수, data )
sql = ''' INSERT INTO movieTbl (movieName, kind, price, period)
            VALUES (%s, %s, %s, %s);'''
data = (('찰리채플린','코미디', 2000, 2),
        ('엔드게임','액션', 1000, 1),
        ('슈퍼맨 리턴즈','액션', 1500, 2))
cursor.executemany(sql, data)
conn.commit()

conn.close()