-- 데이타베이스 CRUD
-- 테이블 CRUD
-- 레코드 CRUD

-- 테이블 생성과 삭제 관련 명령어
-- DROP/DELETE TABLE  <IF EXISTS> 테이블명; -- 테이블 삭제 

-- CREATE TABLE 테이블명 (필드명 자료형 옵션);
-- 옵션 : NULL/ NOT NULL / AUTO INCREMENT 
-- PRIMARY KEY / FOREIGN KEY(필드명) REFERENCES 테이블명(필드명)

-- SHOW TABLES; -- 테이블 목록 표시 
-- DESC 테이블명; -- 테이블 구조 표시 
USE sqldb;
SHOW TABLES;

-- MYSQL의 자료형 :
-- 숫자형 (정수, 실수...) smallint, int, float, decimal ... 
-- 문자형 char(n), varchar(n), binary(n), text, longtext,  blob...
-- 날짜형 ????-??-?? ??:??:?? date, time, datetime ...
-- 기타  lob, json ... 

-- 회원가입테이블 userTbl2
-- 이름 userName -- char(5) not  null 
-- 아이디 userId -- char(8) not   null  PRIMARY KEY 
-- 연락처 mobile -- varchar(16)   not null 
-- 이메일 email -- varchar(20)    null
-- 생년월일 birth -- date         null 
CREATE TABLE userTbl2 (
	userName char(5) NOT NULL, -- 이름 
	userId char(8)  PRIMARY KEY NOT NULL, -- 아이디 8글자 이내 
	mobile VARCHAR(16)  NOT NULL, -- 연락처 
	email VARCHAR(30)  NULL, -- 이메일 널허용
	birth DATE NOT NULL -- 생년월일  ????-??-??
);

SHOW TABLES;
DESC userTbl2;

-- 레코드 삽입 테스트 
-- INSERT INTO 테이블명 VALUES (..,..,..,..);
-- INSERT INTO 테이블명 (필드명....)VALUES (..,..,..,..);
-- INSERT INTO 테이블명 VALUES (...), (...), (...), ....;

-- 필드명 생략방식 
INSERT INTO userTbl2 
	VALUES ('박지민','PJM','010-1234-8888','ABC@naver.com','1995-01-01');

-- 필드명 지정방식
INSERT INTO userTbl2 (userName, userId, mobile, birth)
	VALUES ('박지민','BJM','010-3333-0000','1998-01-01');

-- 2개 이상의 레코드 삽입 
INSERT INTO userTbl2 
	VALUES 
		('최지민','CJM','010-3333-8888',NULL,'1997-01-01'),
        ('윤지민','YJM','010-2222-8888','YJM@naver.com','1999-01-01'),
        ('김지민','KJM','017-1234-8888','KJM@naver.com','2000-06-01');
  
SELECT * FROM userTbl2;    

-- 기본키(Primary Key) 테스트 
-- Error Code: 1062. Duplicate entry 'BJM' for key 'PRIMARY'
INSERT INTO userTbl2 
	(userName, userId, mobile, birth)
	VALUES ('박지민','BJM','010-3333-0000','1998-01-01');

-- ALTER TABLE 테이블명
-- 	ADD 컬럼명 데이터형( CHAR(), INT, VARCHAR(), DATE, DATETIME ... )
-- 		[DEFAULT 디폴트값] -- 기본값 설정 
-- 		[NULL/NOT NULL]; -- Null 허용함

-- 새로운 컬럼 추가 1  - 기본값 지정방식 
ALTER TABLE userTbl2 ADD homepage VARCHAR(30)  -- 열추가
	DEFAULT 'http://google.com' -- 디폴트값
    NULL; -- Null 허용함

DESC userTbl2;
SELECT * FROM userTbl2;

-- 디폴트값 테스트 
INSERT INTO userTbl2 
	(userName, userId, mobile, email, birth, homepage)
	VALUES ('김철수','KCS','011-3333-0000',NULL, '2001-01-01', 'http://naver.com');  
INSERT INTO userTbl2 
	(userName, userId, mobile, birth)
	VALUES ('박철수','PCS','019-3333-0000', '2001-01-01');    
INSERT INTO userTbl2 
	(userName, userId, mobile, birth, homepage)
	VALUES ('최철수','CCS','018-3333-0000','2001-01-01', NULL);    

DESC userTbl2;
SELECT * FROM userTbl2;

-- 새로운 컬럼 추가 2        
ALTER TABLE userTbl2 ADD age INT(3) -- 나이 
	NULL; -- Null 허용함 

DESC userTbl2;
SELECT * FROM userTbl2;

-- 기존 컬럼 삭제  - 키가 없는 경우 
-- ALTER TABLE 테이블명
-- 	DROP COLUMN 컬럼명;
ALTER TABLE userTBL2 DROP COLUMN age;

DESC userTbl2;
SELECT * FROM userTbl2;    
    
-- 컬럼 수정 
-- 컬럼명1을 컬럼명2로 수정 
-- ALTER TABLE 테이블명 
-- 	CHANGE COLUMN 컬럼명1 컬럼명2 데이타형 [NULL 또는 NOT NULL] ;    
DESC userTbl2;

-- 컬럼명, 자료형, NULL 형식 변경 
-- 문자열(char) => 문자열(varcher) 
ALTER TABLE userTbl2
	CHANGE COLUMN userName uName VARCHAR(20) NULL;
    
DESC userTbl2;  
SELECT * FROM userTbl2; 

-- birth(date) => birth_date(int) 가능 
ALTER TABLE userTbl2
	CHANGE COLUMN birth birth_date INT;
    
DESC userTbl2;  
SELECT * FROM userTbl2; 

-- mobile(varchar) => contact(int) ?
-- Error Code: 1265. Data truncated for column 'contact' at row 1
ALTER TABLE userTbl2
	CHANGE COLUMN mobile contact INT;
    
-- 외래키(FOREIGN KEY)란?
-- 다른 테이블의 특정 필드의 값을 참조한다. 
-- 외래키 설정은?
-- 테이블 생성시 
-- FOREIGN KEY(외래키설정필드명) REFERENCES 외래키가있는테이블명(외래키필드명)

-- 외래키 테스트 
-- demo_people (name, phone, pid(PK))
-- demo_property (spid(PK), pid(FK), selling)
-- demo_property 테이블의 pid 필드는 demo_people 테이블의 pid를 참조한다. 

USE sqldb;
CREATE TABLE demo_people
(
	pid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL, 
    phone VARCHAR(10) NULL
);
    
DESC demo_people;

-- demo_property (spid(PK), pid(FK), selling)
CREATE TABLE demo_property (
	spid INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- 기본키 
    pid INT NOT NULL, 
    selling VARCHAR(30) NOT NULL, 
    FOREIGN KEY(pid) REFERENCES demo_people(pid)
);
DESC demo_property;

-- 외래키가 있는 테이블에서 레코드 삽입 테스트 
-- pid 기본키가 autoincrement 인경우에는 NULL 로 값 지정 
INSERT INTO demo_people 
  VALUES 
	(NULL, '선우미란', '02-123-123'), 
    (NULL, '박미란', NULL), 
    (NULL, '최미란', '02-567-123');

SELECT * FROM demo_people;

-- demo_property (spid(PK-AUTOINCREMENT), pid(FK), selling)
INSERT INTO demo_property VALUES (NULL, 1, '노트북');     

SELECT * FROM demo_property;    

-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`sqldb`.`demo_property`, CONSTRAINT `demo_property_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `demo_people` (`pid`))    
INSERT INTO demo_property VALUES (NULL, 5, '테이블');     
    
INSERT INTO demo_property 
	VALUES (NULL, 1, '테이블'), (NULL, 3, '공기청정기'), (NULL, 2, '사과');     
            
SELECT * FROM demo_property;           

-- 이너조인 
SELECT * FROM demo_people D1
    INNER JOIN demo_property D2
    ON D1.pid = D2.pid;   
    
-- 기본키 추가하기 
--  ALTER TABLE 테이블명
-- 		ADD CONSTRAINT PK_테이블명_기본키필드명
--  	PRIMARY KEY (기본키필드명);    

-- userTbl => userCopy    
CREATE TABLE userCopy (
	SELECT * FROM userTbl
);    

SELECT * FROM  userCopy;
DESC userCopy;   
DESC userTbl;   

-- userCopy  테이블에서 userID 필드를 기본키로 설정 
--  ALTER TABLE 테이블명
-- 		ADD CONSTRAINT PK_테이블명_기본키필드명
--  	PRIMARY KEY (기본키필드명);  

 ALTER TABLE userCopy 
	ADD CONSTRAINT PK_userCopy_userID
 	PRIMARY KEY (userID); 
    
DESC userCopy;

-- 기본키 삭제하기 
-- ALTER TABLE 테이블명 DROP PRIMARY KEY; 
 ALTER TABLE userCopy 
	DROP PRIMARY KEY; 

 DESC userCopy;    
 
 -- 외래키 추가하기 
-- ALTER TABLE 테이블명
-- 	ADD CONSTRAINT 테이블명_ibfk_1
--  FOREIGN KEY (외래키필드명)
--  REFERENCES 참조테이블명(참조테이블의 외래키필드명);

-- ALTER TABLE buyTbl
-- 	ADD CONSTRAINT buyTbl_ibfk_1
-- 	FOREIGN KEY (userID)
-- 	REFERENCES userTbl(userID);
    
USE sqldb;	
-- usertbl => usertbl_a
-- userId(PK)

-- buytbl => buytbl_a
-- num(PK) 
-- userId(FK) 

CREATE TABLE usertbl_a (
	SELECT * FROM usertbl
);     
    
CREATE TABLE buytbl_a (
	SELECT * FROM buytbl
);      
    
DESC usertbl_a;    
DESC buytbl_a;    


-- usertbl_a 테이블에서 userID 필드를 기본키로 설정 
--  ALTER TABLE 테이블명
-- 		ADD CONSTRAINT PK_테이블명_기본키필드명
--  	PRIMARY KEY (기본키필드명); 

ALTER TABLE usertbl_a
	ADD CONSTRAINT PK_usertbl_a_userId
	PRIMARY KEY (userId); 

DESC usertbl_a;

-- buyTbl_a 테이블에서 num 필드를 기본키로 설정 
ALTER TABLE buyTbl_a
	ADD CONSTRAINT PK_buyTbl_a_num
	PRIMARY KEY (num); 

DESC buyTbl_a;

-- buyTbl_a 테이블에서 userID 필드를 외래키로 설정 
ALTER TABLE buyTbl_a
	ADD CONSTRAINT buyTbl_a_ibfk_1
	FOREIGN KEY (userID)
	REFERENCES userTbl_a(userID);    

DESC buyTbl_a;

--  외래키 삭제하기 
-- ALTER TABLE 테이블명 
-- 		DROP FOREIGN KEY 외래키명; 

-- 외래키명은 [SCHEMAS] 테이블 정보에서 확인 
-- 삭제 결과는 [SCHEMAS] 테이블에서 Foreign Keys 에서 확인 
ALTER TABLE buyTbl_a
	DROP FOREIGN KEY buyTbl_a_ibfk_1; 