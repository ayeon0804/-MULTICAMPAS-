--  퀴즈1
--  다음과 같은 형태로  movieTbl 테이블을 생성하여라. 
--  movieNum int  -- 번호(기본키, 자동증감, 필수 속성) 
--  movieName varchar(30) -- 무비명(필수 속성) 
--  kind varchar(30) -- 장르명(필수 속성) 
--  price int, -- 대여 가격(필수 속성) 
--  period int -- 대여 기간(필수 속성) 

--   1 토이스토리 애니메이션 3000 5 
USE sqldb;
CREATE TABLE movieTbl
(
	movieNum int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    movieName varchar(30) NOT NULL,
	kind varchar(30) NULL,
    price int NOT NULL,
    period int NOT NULL
 );
INSERT INTO movieTbl 
		VALUES 
			(NULL, '토이스토리', '애니메이션', 3000, 5), 
            (NULL, '극한직업', '액션', 1000, 5),
            (NULL, '안녕 자두야', NULL, 1000, 8), 
            (NULL, '설국 열자', '액션', 3000, 1),
            (NULL, '엽기적인 그녀', '코메디', 1500, 5);

SELECT * FROM movieTbl;
--  퀴즈3 
--   다음과 같은 형태로  memberTbl 테이블을 생성하여라. 
--     userNum int  -- 번호(기본키, 자동증감, 필수 속성) 
--     name varchar(20)  -- 회원명
--     grade int  -- 회원 등급(필수 속성) 
--     tel varchar(15)  -- 연락처(필수 속성) 
--     address varchar(300) -- 주소(널 허용)
--     money int  -- 예치금(필수 속성) 

-- 1 박수찬 3  010-6666-9999  삼광빌라905호  10000
CREATE TABLE memberTbl
(
	userNum int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    name varchar(20) NOT NULL,
	grade int NOT NULL,
    tel varchar(15) NOT NULL,
    address varchar(300) NULL, 
    money int NOT NULL
 );
DESC memberTbl;

-- 퀴즈4.  퀴즈3의 memberTbl 테이블의 자료형에 맞추어 7개 이상 레코드를 삽입하여라. 
INSERT INTO memberTbl
	VALUES 
		(NULL, '박수찬', 3,  '010-6666-9999',  '삼광빌라905호', 10000),
        (NULL, '홍길동', 2,  '010-1111-8888',  '푸른빌라102호', 20000),
        (NULL, '김철수', 4,  '010-2222-7777',  '삼광빌라603호', 30000),
        (NULL, '김미희', 3,  '010-3333-6666',  '푸른빌라801호', 40000),
        (NULL, '강수지', 5,  '010-4444-5555',  '녹색빌라1103호', 50000),
        (NULL, '김선호', 2,  '010-5555-4444',  '녹색빌라608호', 60000),
        (NULL, '이제훈', 5,  '010-7777-3333',  '푸른빌라1203호', 70000);
SELECT * FROM memberTbl;
--  퀴즈5 
--   다음과 같은 형태로  rentTbl 테이블을 생성하여라. 

--    rentNum int  -- 대여번호(PK)(기본키, 자동증감, 필수 속성)
--    userNum int -- 대여한 회원번호(FK) (필수 속성, memberTbl의 키 참조)
--    movieNum int  --대여한 비디오번호(FK) (필수 속성, movieTbl의 키 참조)

-- 1  1  1
CREATE TABLE rentTbl
(
	rentNum int PRIMARY KEY AUTO_INCREMENT,
    userNum int NOT NULL,
    movieNum int NOT NULL,
    FOREIGN KEY(userNum) REFERENCES memberTbl(userNum),
    FOREIGN KEY(movieNum) REFERENCES movieTbl(movieNum)
);

-- 퀴즈6.  퀴즈5의 rentTbl 테이블의 자료형에 맞추어 7개 이상 레코드를 삽입하여라. 
INSERT INTO rentTbl
	VALUES
		(NULL, 4, 1), (NULL, 1, 2), (NULL, 4, 2), (NULL, 2, 3), (NULL, 3, 5), (NULL, 3, 1), (NULL, 6, 1);

-- 퀴즈7.  3개의 테이블 (movietbl, rentTbl, memberTbl)을 이너조인하여라. 
SELECT * FROM movietbl M
	INNER JOIN renttbl R
	ON M.movieNum = R.movieNum
		INNER JOIN membertbl MB
        ON R.userNum = MB.userNum;

-- 퀴즈8.  대여를 하지 않는 회원 목록을 출력하여라.
SELECT name FROM membertbl MB
	LEFT OUTER JOIN renttbl R
	ON R.userNum = MB.userNum
		LEFT OUTER JOIN movietbl M
        ON M.movieNum = R.movieNum
			WHERE rentNum IS NULL;

-- 퀴즈9.  대여가 한번도 되지않은 영화 목록을 출력하여라.
SELECT movieName FROM movietbl M
	LEFT OUTER JOIN renttbl R
	ON M.movieNum = R.movieNum
		LEFT OUTER JOIN membertbl MB
        ON R.userNum = MB.userNum
			WHERE rentNum IS NULL;
			
-- 퀴즈10.  회원별로 구매 횟수를 출력하여라.
SELECT name, COUNT(rentNum) FROM membertbl MB
	LEFT OUTER JOIN renttbl R
	ON R.userNum = MB.userNum
		LEFT OUTER JOIN movietbl M
        ON M.movieNum = R.movieNum
			GROUP BY(name)
				ORDER BY COUNT(rentNum) DESC;

SELECT * FROM booktbl;