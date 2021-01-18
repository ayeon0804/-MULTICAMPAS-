-- 테이블의 레코드 CRUD (삽입, 삭제, 수정)

-- 기본 테이블 buytbl의 사본 테이블 생성
CREATE TABLE buytbl2
	(SELECT * FROM buytbl);
SHOW TABLES;
DESC buytbl;
DESC buytbl2; -- 키는 복사안됨

-- 레코드 삽입 1
-- INSERT INTO 테이블명 (컬럼명1, 컬럼명2... ) VALUES(값1, 값2 .. )
INSERT INTO buytbl2 (num, userid, prodName, groupName, price, amount)
	VALUES (13, 'TTT', '가습기', '생활가전', 90000, 1);
SELECT * FROM buytbl2 ORDER BY num DESC;

-- 특정필드와 값만 삽입
-- NULL 값 허용 필드 확인 - NULL이 YES인 값
-- NULL 값 허용 필드 => groupName
DESC buytbl2;
INSERT INTO buytbl2 (num, userid, prodName, price, amount)
	VALUES (14, 'TTT', '온풍기', 150000, 1);
SELECT * FROM buytbl2 ORDER BY num DESC;

-- 레코드 삽입 2 : 필드명 생략 방식 
-- 필드값이 삽입되는 순서 유의 
-- INSERT INTO 테이블명 VALUES(값1, 값2 .. )
INSERT INTO buytbl2 
	VALUES (15, 'BBK', '책상', '가구', 50000, 3);
SELECT * FROM buytbl2 ORDER BY num DESC;

-- 레코드 삽입 3
-- 다른 테이블의 레코드를 SELECT 문으로 삽입하기 
-- INSERT INTO 테이블명 (컬럼명1, 컬러명2 ... ) SELECT 문   
-- 테이블 구조(데이타형,필드명등)가 같아야한다.
-- buytbl 테이블에서 데이타 복사 X, 구조만 복사 
CREATE TABLE buytbl3
	(SELECT * FROM buytbl
		WHERE num=13);
SELECT COUNT(*) FROM buytbl3;
DESC buytbl3;

-- buyTbl 테이블에서 groupName 필드값이 전자 인 레코드만 복사해서 
-- buytbl3 테이블의 레코드로 삽입하기 
INSERT INTO buytbl3 
		(num, userid, prodName, groupName, price, amount) 
		SELECT num, userid, prodName, groupName, price, amount
				FROM buyTbl
                WHERE groupName = '전자';
SELECT COUNT(*) FROM buytbl3;
SELECT * FROM buytbl3;

-- 레코드 수정
-- UPDATE 테이블명 SET 컬럼명=값 WHERE 절;
SELECT * FROM buytbl2;
-- buytbl2의 userid 가 KBS 인 레코드에서 amount 값을 10으로 변경하여라 
UPDATE buytbl2 SET amount = 10 WHERE userid = 'KBS';
SELECT * FROM buytbl2 WHERE userid = 'KBS';        

-- WHERE 절이 생략된 경우에는 모든 레코드에서 업데이트가 진행   
-- buytbl2 테이블에서 레코드의 price 가격 모두를 150%로 변경하여라 
-- price*1.5
SELECT * FROM buytbl2; 
UPDATE buytbl2 SET price = price*1.5;
SELECT * FROM buytbl2; 
SELECT * FROM buytbl;         

-- 특정 레코드 삭제 
-- DELETE FROM 테이블명 WHERE 절 
-- WHERE 절 생략시 레코드 모두 삭제 
SELECT * FROM buytbl2; 

-- buytbl2 테이블에서 전자 종목의 레코드를 모두 삭제 
DELETE FROM buytbl2 WHERE groupName = '전자';
SELECT * FROM buytbl2; 

-- WHERE 절 생략시 레코드 모두 삭제 
DELETE FROM buytbl2;
SELECT * FROM buytbl2; 

-- 테이블 삭제 
-- DROP TABLE 테이블명;
DROP TABLE buytbl2;
SHOW TABLES;

-- 테이블 구조 제외 레코드만 삭제 
-- TRUNCATE TABLE 테이블명;
SELECT * FROM buytbl3;
TRUNCATE TABLE buytbl3;
SHOW TABLES;
SELECT * FROM buytbl3;

