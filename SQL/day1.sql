-- 데이타베이스 목록확인
SHOW DATABASES;

-- 데이타베이스 접속하기
USE employees;

-- 접속중인 데이타베이스의 테이블 목록 확인하기 
SHOW TABLES;

-- 특정 테이블의 정보 확인하기 
-- DESCRIBE 테이블명;
-- DESC 테이블명;
-- DESCRIBE(/DESC) 데이타베이스명.테이블명;
DESC employees;
DESC salaries;
-- 다른 데이타베이스의 특정 테이블 정보 확인
DESC world.city;

-- 테이블 레코드 출력하기
SHOW TABLES;
-- salaries 테이블 목록 확인
SELECT * FROM salaries;
SELECT emp_no, salary FROM salaries;
SELECT * FROM salaries LIMIT 5; -- 5개의 데이타만 출력

-- wolrd 데이타베이스의 city 테이블 목록 확인
SELECT * FROM world.city LIMIT 5;

SELECT COUNT(*) FROM salaries;
SELECT COUNT(*) FROM employees;
SELECT COUNT(*) FROM dept_emp;

USE sqldb;
SHOW TABLES;
SELECT * FROM buytbl;
SELECT * FROM buytbl LIMIT 3;

-- 필터링 : 조건에 맞는 레코드 출력하기 
-- SELECT */필드명나열 FROM 테이블명 WHERE 절;
-- SELECT */필드명나열 FROM 데이타베이스명.테이블명 WHERE 절;
-- WHERE 조건절의 연산자는? 
-- 관계연산자(>, =...),
-- 논리연산자(AND, OR, NOT)

SELECT * FROM usertbl WHERE name = '김경호';
SELECT * FROM usertbl WHERE height < 170;
SELECT * FROM usertbl WHERE height > 175 AND height < 180;


