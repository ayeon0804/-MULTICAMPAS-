import pymysql

conn = pymysql.connect( host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '1234',
                        db = 'sqldb',
                        charset = 'utf8')

cursor = conn.cursor()
cursor.execute('SELECT * FROM userTbl;')
userTbl_data = cursor.fetchall()

conn.close()

for row in userTbl_data:
    print(row)

print('=== 마지막 행만 출력')
print(userTbl_data[-1])

print('=== 2행의 3~4 컬럼만 출력')
print(userTbl_data[1][2:4])

# sql 변수를 별도 지정 1
# sql = 'SELECT * FROM userTbl;'
# cursor.execute(sql)

# sql 변수를 별도 지정2 - 다른 데이타베이스의 테이블 접근
# sql = 'SELECT * FROM world.city;'
# cursor.execute(sql)