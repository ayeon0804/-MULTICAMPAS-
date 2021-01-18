-- 퀴즈 : 함수

-- Q1. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 7의 레코드만 정렬시켜 출력하여라.
-- 정렬 기준은 emp_no 기준이다.   
/*
사원번호   이름                   생년월일   
499999	Sachin  Tsukuda			1958-05-01
499998	Patricia  Breugel		1956-09-05
499997	Berhard  Lenart			1961-08-03
499996	Zito  Baaz				1953-03-07
499995	Dekang  Lichtner		1958-09-24
499994	Navin  Argence			1952-02-26
499993	DeForest  Mullainathan	1963-06-04
*/        
USE employees;
DESC employees;      
SELECT emp_no AS '사원번호', CONCAT(first_name, ' ', last_name) AS '이름', birth_date AS '생년월일'
	FROM employees
		ORDER BY emp_no DESC
			LIMIT 7;

-- Q2. employees 테이블에서 문자열 함수를 이용하여 birth_date 필드값이 
-- ????년 ??-?? 형태로 출력되도록 하여라. 
-- 정렬 기준은 first_name 기준이다. 
/*
emp_no  first_name	last_name    	birth_date        
11935	Aamer		Jayawardene		1963년  03-23
12160	Aamer		Garrabrants		1954년  12-11
15332	Aamer		Slutz			1961년  12-29
11800	Aamer		Fraisse			1958년  12-09
13011	Aamer		Glowinski		1955년  02-25
*/
SELECT emp_no, first_name, last_name, CONCAT(LEFT(birth_date,4), '년 ', RIGHT(birth_date, 5))
	FROM employees
		ORDER BY first_name;

-- Q3. employees 테이블에서 문자열 함수를 이용하여 hire_date 필드값에서
-- '-'를 '__'으로 교체하여 출력되도록 하여라.  
-- REPLACE(문자열, 원래문자열, 교체문자열)
/*
emp_no  first_name	last_name   hire_date 	         
10001	Georgi		Facello		1986__06__26
10002	Bezalel		Simmel		1985__11__21
10003	Parto		Bamford		1986__08__28
*/
SELECT emp_no, first_name, last_name, REPLACE(hire_date, '-', '__')
	FROM employees;

-- Q4. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--     입사년도의 경우 년도만 출력되도록한다. 
/*
사원명           성별  입사년도
Georgi Facello	M	1986 년
Bezalel Simmel	F	1985 년
Parto Bamford	M	1986 년
...
*/
SELECT CONCAT(first_name, ' ', last_name) AS '사원명', gender AS '성별', 
	CONCAT(LEFT(hire_date,4),'년') AS '입사년도'
		FROM employees;

-- Q5. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--  first_name 필드값의 경우  첫글자 외에서 '*' , 
--  last_name 필드값의 경우 모든 글자를 '*'로 표시한다. 
/*
emp_no  first_name  last_name  gender  	hire_date

10001	G*****		*******		M		1986-06-26
10002	B******		******		F		1985-11-21
10003	P****		*******		M		1986-08-28

*/
SELECT emp_no, CONCAT(LEFT(first_name,1),REPEAT('*',LENGTH(first_name)-1)) AS 'first_name',
	REPEAT('*',LENGTH(last_name)) AS 'last_name', gender, hire_date
		FROM employees;

-- Q6. employees 테이블에서 문자열 함수를 이용하여 다음과 같이 출력되도록 하여라. 
--  성별(gender) 필드값을 M,F를 남자,여자 로 표시한다.

-- IF(조건식, 값1, 값2)
-- 조건식이 True 이면 값1, False 이면 값2 반환 
/*
사원번호   생년월일        사원명          성별    입사일 
10001	1953-09-02	Georgi Facello	남자	 1986-06-26
10002	1964-06-02	Bezalel Simmel	여자	 1985-11-21
10003	1959-12-03	Parto Bamford	남자	 1986-08-28
*/
SELECT emp_no AS '사원번호', birth_date AS '생년월일', CONCAT(first_name, ' ', last_name) AS '사원명',
	IF(gender = 'M', '남자', '여자') AS '성별', hire_date AS '입사일'
		FROM employees;

-- Q7. employees 테이블에서 가장 최근에 입사한 사람 3명만 출력하시오
SELECT * FROM employees
	ORDER BY hire_date DESC
		LIMIT 3;

-- Q8. employees 테이블에서  1999년에 입사한 직원 중 여자 직원(GENDER='F') 리스트를 구하시오.
SELECT * FROM employees
	WHERE YEAR(hire_date) = 1999 AND gender = 'F';

-- Q9. employees 테이블에서  1999년에 입사한 직원 중 남자 직원(M)은 몇 명인가?
SELECT COUNT(*) FROM employees
	WHERE YEAR(hire_date) = 1999 AND gender = 'M';

-- Q10. employees 테이블에서   1998년이나 1999년에 입사한 직원의 수를 구하시오.
SELECT COUNT(*) FROM employees
	WHERE YEAR(hire_date) IN (1998, 1999);

-- worldDb 데이타베이스 이용 
-- Q11. country 테이블에서 독립년도(IndepYear)가 NULL인 경우 '알수없음' 으로 표시하여라.
/*
  국가      독립년도
  ?        알수없음'
  ?          ?
  ?          ?
*/
USE world;
SELECT * FROM country;
SELECT Continent AS '국가', IFNULL(IndepYear, '알수없음') AS '독립년도'
	FROM country;
    
-- worldDb 데이타베이스 이용 
-- Q12.  country 테이블에서 독립년도(IndepYear)가 음수로 표시된 레코드의 필드값을
-- 'BC' 와 함께 연도를 표시하여라
/*
  국가         독립년도
  China     BC.1523
    ?            ?
    ?            ?
*/
SELECT Continent AS '국가', 
	IF(LEFT(IndepYear,1) = '-', 
		CONCAT('BC',SUBSTRING(IndepYear,2,length(IndepYear))), 
		IndepYear) AS '독립년도'
			FROM country;

-- ##################################
-- 퀴즈 : 조인
-- 1. 현재 근무 중인 직원 정보를 출력하시오.(employees 테이블과 dept_emp 테이블 조인 )
-- 현재 근무 중은? to_date='9999-01-01'
/*
사원번호  이름  성별   입사일(hire_date)  현재 근무중
  ?      ?   ?           ?       9999-01-01
*/
USE employees;
SELECT E.emp_no AS '사원번호', CONCAT(first_name, ' ', last_name) AS '이름', gender AS '성별',
	hire_date AS '입사일', to_date AS '현재 근무중'
		FROM employees E
			INNER JOIN dept_emp D
			ON E.emp_no = D.emp_no
				WHERE to_date = '9999-01-01';

-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 title 테이블 조인
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
/*
사원번호  이름   직무(title)  현재 근무중
  ?      ?        ?     9999-01-01
*/
SELECT E.emp_no AS '사원번호', CONCAT(first_name, ' ', last_name) AS '이름', 
	title AS '직무', to_date AS '현재 근무중'
		FROM employees E
			INNER JOIN titles T
			ON E.emp_no = T.emp_no
				WHERE to_date = '9999-01-01';

-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)
-- 3개의 테이블 조인
-- Step1 : dept_emp , employees, departments 테이블에서
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
/*
사원번호  사원명  부서코드(dept_no)  부서명(dept_name)  현재 근무중
  ?      ?        ?               ?         9999-01-01
*/
SELECT E.emp_no AS '사원번호', CONCAT(first_name, ' ', last_name) AS '사원명', 
	D.dept_no AS '부서코드', dept_name AS '부서명', to_date AS '현재 근무중'
		FROM employees E
			INNER JOIN dept_emp DE
            ON E.emp_no = DE.emp_no
				INNER JOIN departments D
                ON DE.dept_no = D.dept_no
					WHERE to_date = '9999-01-01';
                    
-- 4. 가장오래 근무한 직원 10명의 현재 부서를 출력하시오.
-- 3개의 테이블 조인
-- Step1 : dept_emp , employees, departments 테이블에서
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
-- Step3 : ORDER BY hire_date 정렬 옵션과 LIMIT 10 출력레코드 수 추가
/*
사원번호  사원명  부서명(dept_name)  입사일(hire_date)
  ?      ?        ?               ?
*/
SELECT E.emp_no AS '사원번호', CONCAT(first_name, ' ', last_name) AS '사원명', 
	dept_name AS '부서명', hire_date AS '입사일'
		FROM employees E
			INNER JOIN dept_emp DE
            ON E.emp_no = DE.emp_no
				INNER JOIN departments D
                ON DE.dept_no = D.dept_no
					WHERE to_date = '9999-01-01'
						ORDER BY hire_date
							LIMIT 10;

-- 5. 현재 근무중인 부서별로 직원수와 부서 이름도 함께 출력하시오.
-- 2개의 테이블 조인
-- Step1 : dept_emp , departments 테이블에서
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
-- Step3 : group by, count() 이용
/*
부서명(dept_name)  직원수
        ?           ?
*/
SELECT dept_name AS '부서명', COUNT(emp_no) AS '직원수'
	FROM dept_emp DE
		INNER JOIN departments D
		ON DE.dept_no = D.dept_no
			WHERE to_date = '9999-01-01'
				GROUP BY dept_name;

-- 6. 현재 근무중인 사원을 기준으로 부서별로 성별 인원수를 표시하여라. 이때 부서 이름도 함께 출력한다.
-- 2개의 테이블 조인
-- Step1 : dept_emp , departments 테이블에서
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
-- Step3 : group by, count() 이용
/*
  부서명    성별   직원수
  Sales    M     ?
  Sales    F     ?
  ...
*/
SELECT dept_name AS '부서명', gender AS '성별', COUNT(E.emp_no) AS '직원수'
	FROM employees E
		INNER JOIN dept_emp DE
		ON E.emp_no = DE.emp_no
			INNER JOIN departments D
			ON DE.dept_no = D.dept_no
				WHERE to_date = '9999-01-01'
					GROUP BY dept_name, gender;
SELECT * FROM employees;                
SELECT * FROM dept_emp;
SELECT * FROM departments;

--  7. 현재 근무중인 사원을 기준으로 급여 평균이 가장 높은 부서 3개만 출력하여라
-- Step1 : dept_emp + departments + salaries 테이블에서
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가
-- Step3 : group by , avg() 이용
/*
부서명              평균급여
   ?                ?
   ?                ?
   ...
*/
SELECT * FROM dept_emp; -- emp_no dept_no 
SELECT * FROM departments; -- dept_no
SELECT * FROM salaries; -- emp_no
SELECT dept_name AS '부서명', AVG(salary) AS '평균급여'
	FROM departments D
		INNER JOIN dept_emp DE
        ON DE.dept_no = D.dept_no
			INNER JOIN salaries S
            ON DE.emp_no = S.emp_no
				WHERE DE.to_date = '9999-01-01'
					GROUP BY dept_name
						ORDER BY AVG(salary) DESC
							LIMIT 3;

