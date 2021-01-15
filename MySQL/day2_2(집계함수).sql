-- GROUP BY
-- 그룹을 묶어주는 역할. 집계함수와 함께 사용 
-- SELECT .. FROM 테이블명 GROUP BY 컬럼명;

-- 갯수 구하기 COUNT(*|컬럼명)
-- 합계 구하기 SUM(컬럼명)
-- 평균 구하기 AVG(컬럼명)

-- buytbl 테이블에서 price의 전체 합계와 평균구하기
USE sqldb;
DESC buytbl;

SELECT SUM(price), AVG(price), COUNT(price) FROM buytbl;

-- 각 종목의 가격(price) 합계, 평균을 groupName을 기준으로 정렬하여 표시하기
SELECT  groupName, SUM(price), AVG(price) FROM buytbl 
	GROUP BY groupName 
    ORDER BY groupName;

-- AS 별칭이름;
-- 컬럼명을 대신하는 별칭 이름 표시
-- SELECT 컬럼명 AS 별칭명 FROM 테이블명;  
SELECT groupName AS '종목', SUM(price) AS '가격 합계', AVG(price) AS '가격 평균' 
	FROM buytbl
    GROUP BY groupName 
    ORDER BY groupName DESC
    LIMIT 2;
    
-- 퀴즈 : buytbl 테이블에서 사용자별로 구매합계 구하기 
/*
사용자아이디별 총구매액 표시 - GROUP BY, SUM(), AS
총구매액은? SUM(price*amount)

출력양식 

사용자아이디    총구매액  
BBK 		?
EJW			?
..
*/
DESC buytbl;
SELECT userID AS '사용자아이디', SUM(price*amount) AS '총구매액' FROM buytbl
	GROUP BY userID;
    
-- 가격 필드의 최댓값, 최솟값, 수량 표시
SELECT 	MAX(price) AS '최대값',  MIN(price) AS '최소값', COUNT(price) AS '갯수' FROM buytbl;


-- buytbl 테이블에서 각 사용자별로 물건을 몇개 사는지 평균 구하기 
SELECT userID, AVG(amount) AS '평균 물건 구입 갯수' FROM buytbl GROUP BY userID;

-- userTbl 테이블에서 가장 큰키와 가장 작은 키의 레코드를 출력하여라 
-- 서브쿼리를 사용하지 않은 경우 
SELECT MAX(height), MIN(height) FROM usertbl; -- 186, 166
SELECT * FROM usertbl WHERE height IN (186 , 166);

-- 서브쿼리를 사용한 경우
SELECT * FROM usertbl
	WHERE height = (SELECT MAX(height) FROM usertbl) 
		OR height = (SELECT MIN(height) FROM usertbl);

-- NULL과 COUNT() 테스트 : NULL은 COUNT에 포함이 안됨. 
SELECT COUNT(*) AS '전체 레코드수' FROM usertbl; -- 10
SELECT COUNT(mobile1) AS 'mobile1 필드 레코드수' FROM usertbl; -- 8

SELECT COUNT(*) AS '전체 사용자수', COUNT(mobile1) AS '휴대폰이 있는 사용자수', 
		COUNT(*) - COUNT(mobile1) AS '휴대폰이 없는 사용자수'
			FROM usertbl;

-- buyTbl 테이블에서 총구매액이 
-- 1000 이상 조건으로 사용자(userID)별 총 구매액 표시 
-- GROUP BY 기준 : 사용자(userID)
-- 구매액 : SUM(price*amount) 
SELECT userID, SUM(price*amount) AS '총 구매액' FROM buytbl
	GROUP BY userID
		HAVING SUM(price*amount) >= 1000;
        
-- 퀴즈
-- buyTbl 테이블에서 userID 별 
-- 평균 구매 횟수(AVG(amount))가 
-- 1~3 사이인 레코드만 출력하여라
SELECT * FROM buytbl
	GROUP BY userID
		HAVING AVG(amount) BETWEEN 1 AND 3;
        
-- WITH ROLLUP
-- 중간 합계 
-- 순서 주의 
-- SELECT .. FROM 테이블명 
-- GROUP BY 컬럼명1, 컬럼명2 HAVING 조건 
-- WITH ROLLUP
-- ORDER BY 컬럼명 LIMIT 숫자;

-- 종목(groupName), 주문번호(num)를 기준으로 총구매액 표시             
SELECT num, groupName, SUM(price*amount) 
	FROM buytbl
    GROUP BY groupName, num;     

-- groupName 별로 부분합계가 표시    
SELECT num, groupName, SUM(price*amount) 
	FROM buytbl
    GROUP BY groupName, num
    WITH ROLLUP;