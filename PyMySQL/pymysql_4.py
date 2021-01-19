import pymysql

conn = pymysql.connect( host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '1234',
                        db = 'sampleDb',
                        charset = 'utf8')

cursor = conn.cursor()

def makeDb():
    sql = '''
            create table if not exists bookTbl
                (
                    id int PRIMARY KEY not null AUTO_INCREMENT,
                    title text not null,
                    writer varchar(30) not null,
                    page int not null,
                    price int not null
                );
            '''
    cursor.execute(sql)

# 퀴즈 : input() 문을 이용해서 값을 입력받아서
#       bookTbl 테이블의 레코드로 삽입하여 보세요
'''
레코드 삽입
----------
책이름 => ?
저자 => ?
페이지수 => ?
가격 => ?
----------
레코드 출력 (마지막에 삽입한 레코드가 첫번째 나오게한다)
?   ?   ?   ?   ?
'''
# 레코드 삽입함수 정의
def insertBook():
    print('-'*100)
    print('\t레코드 삽입')
    print('-'*100)
    title = input('책이름 => ')
    writer = input('저자 => ')
    page = input('페이지수 => ')
    price = input('가격 => ')

    sql = ''' INSERT INTO bookTbl (title, writer, page, price)
                VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()
    print('레코드가 삽입되었습니다.')

# 레코드 출력 함수 정의
def showBook():
    print('-'*50)
    print('\t레코드 출력')
    print('-' * 50)
    sql = 'SELECT * FROM bookTbl ORDER BY id DESC; '
    cursor.execute(sql)
    book_data = cursor.fetchall()
    for row in book_data:
        for item in row:
            print(item)

# 레코드 삭제함수 정의
def deleteBook():
    print('-'*50)
    print('\t레코드 삭제')
    print('-' * 50)
    sql = 'DELETE FROM  bookTbl  WHERE id = %s'
    cursor.execute(sql, (1))
    conn.commit()
    print('레코드가 삭제되었습니다.')

# 가격만 수정
def updateBook():
    print('-' * 50)
    print('\t레코드 수정')
    print('-' * 50)
    id = input('id => ')
    price = input('가격 => ')
    sql = 'UPDATE bookTbl SET price=%s  WHERE id=%s;'
    cursor.execute(sql, (price, id))
    conn.commit()
    print('레코드가 수정되었습니다.')

makeDb()
# insertBook()
updateBook()
showBook()

conn.close()
