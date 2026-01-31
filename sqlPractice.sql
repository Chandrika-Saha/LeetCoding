SELECT * 
FROM Parks_and_Recreation.employee_demographics;

SELECT first_name, 
last_name, 
birth_date,
age,
age + 10
FROM Parks_and_Recreation.employee_demographics;

#PEMDAS -> Order of operations in SQL
# Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction

SELECT DISTINCT first_name, gender
FROM Parks_and_Recreation.employee_demographics;

SELECT * 
FROM employee_salary
WHERE first_name = 'Leslie';

SELECT * 
FROM employee_salary
WHERE salary >= 50000;

SELECT * 
FROM employee_demographics
WHERE gender != 'Female';

SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01';

-- AND, OR, NOT -> Logical operators
SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
AND NOT gender = 'Female';

SELECT *
FROM employee_demographics
WHERE (first_name = 'Leslie' AND age = 44) OR age > 55;

-- Like operator to find similar items
-- % and _
-- % means anything can be after or before that part
-- 
SELECT *
FROM employee_demographics
WHERE first_name LIKE 'Jer%'; # Any name that starts with Jer

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a__'; # 2 underscore, exactly two characters

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a__%'; # 2 underscore, two chars followed by any number of char

SELECT *
FROM employee_demographics
WHERE birth_date LIKE '1989%'; # Works for dates as well

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender;

SELECT occupation, salary 
FROM employee_salary
GROUP BY occupation, salary;

SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM employee_demographics
GROUP BY gender;

-- Order by
SELECT *
FROM employee_demographics
ORDER BY first_name; # Default is ASC order

SELECT *
FROM employee_demographics
ORDER BY first_name DESC;

SELECT *
FROM employee_demographics
ORDER BY gender, age;

SELECT *
FROM employee_demographics
ORDER BY gender, age DESC; -- Change the order for the age only

-- Can also use the column position to order
SELECT * 
FROM employee_demographics
ORDER BY 5, 4; -- Column numbering starts at 1

-- Having vs Where
SELECT gender, AVG(age)
FROM employee_demographics
WHERE AVG(age) > 40 -- This is invalid because group has not yet formed, use having in this instance
GROUP BY gender;

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;

SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE '%manager%'
GROUP BY occupation;

SELECT *
FROM Parks_and_Recreation.employee_demographics
LIMIT 3;

SELECT *
FROM Parks_and_Recreation.employee_demographics
ORDER BY age
LIMIT 5;

SELECT *
FROM Parks_and_Recreation.employee_demographics
ORDER BY age
LIMIT 2, 3;

-- Aliasing
SELECT gender, AVG(age)
FROM Parks_and_Recreation.employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;

SELECT gender, AVG(age) as avg_age
FROM Parks_and_Recreation.employee_demographics
GROUP BY gender
HAVING avg_age > 40;

-- Joining
SELECT * 
FROM Parks_and_Recreation.employee_demographics;

SELECT *
FROM Parks_and_Recreation.employee_salary;

SELECT * 
FROM Parks_and_Recreation.employee_demographics
INNER JOIN Parks_and_Recreation.employee_salary -- The default join operation is inner join, however, we can specify the join type if we want to
	ON Parks_and_Recreation.employee_demographics.employee_id = Parks_and_Recreation.employee_salary.employee_id;
    
SELECT *
FROM Parks_and_Recreation.employee_demographics as ed
INNER JOIN Parks_and_Recreation.employee_salary as es
		ON ed.employee_id = es.employee_id
;

SELECT ed.employee_id, age, dept_id
FROM Parks_and_Recreation.employee_demographics as ed
INNER JOIN Parks_and_Recreation.employee_salary as es
		ON ed.employee_id = es.employee_id
;

SELECT *
FROM Parks_and_Recreation.employee_demographics as ed
LEFT JOIN Parks_and_Recreation.employee_salary as es
	ON ed.employee_id = es.employee_id
;

SELECT *
FROM Parks_and_Recreation.employee_demographics as ed
RIGHT JOIN Parks_and_Recreation.employee_salary as es
	ON ed.employee_id = es.employee_id
;

SELECT *
FROM Parks_and_Recreation.employee_demographics as ed
RIGHT JOIN Parks_and_Recreation.employee_salary as es
	ON es.employee_id = ed.employee_id
;

-- SELF JOIN
SELECT es1.employee_id as secret_santa_id,
es1.first_name as secret_santa, 
es2.employee_id as employee_id,
es2.first_name as employee_name
FROM Parks_and_Recreation.employee_salary as es1
INNER JOIN Parks_and_Recreation.employee_salary as es2
	ON es1.employee_id + 1 = es2.employee_id;
;

-- JOIN Multiple tables
SELECT ed.employee_id, occupation, department_name
FROM Parks_and_Recreation.employee_demographics as ed
INNER JOIN Parks_and_Recreation.employee_salary as es
	ON ed.employee_id = es.employee_id
INNER JOIN Parks_and_Recreation.parks_departments as pd
	ON es.dept_id = pd.department_id
;

-- Unions
-- JOINs join the columns, Unions joins the rows together.
-- For unions to make sense, the colum types of both tables should be similar.
SELECT age, gender
FROM Parks_and_Recreation.employee_demographics
UNION
SELECT first_name, last_name
FROM Parks_and_Recreation.employee_salary;

SELECT	first_name, last_name
FROM Parks_and_Recreation.employee_demographics
UNION DISTINCT
SELECT first_name, last_name
FROM Parks_and_Recreation.employee_salary;

SELECT	first_name, last_name
FROM Parks_and_Recreation.employee_demographics
UNION ALL
SELECT first_name, last_name
FROM Parks_and_Recreation.employee_salary;

SELECT first_name, last_name, 'old man' AS Label
FROM Parks_and_Recreation.employee_demographics
WHERE age > 40 AND gender = 'Male'
UNION
SELECT first_name, last_name, 'old lady' AS Label
FROM Parks_and_Recreation.employee_demographics
WHERE age > 40 AND gender = 'Female'
UNION
SELECT first_name, last_name, 'High paying peeps' AS Label
FROM Parks_and_Recreation.employee_salary
WHERE salary > 70000
;

-- String functions
SELECT LENGTH('Skyfall');

SELECT first_name, LENGTH(first_name) AS first_name_length
FROM Parks_and_Recreation.employee_demographics
ORDER BY 2 DESC
;

SELECT UPPER('sky'), LOWER('SkY');

SELECT first_name, UPPER(first_name)
FROM Parks_and_Recreation.employee_demographics;

-- Left and right trims
SELECT TRIM('           sky         '), 
LTRIM('           sky                 '),
RTRIM('           sky         ');

-- Substrings
-- Can be a bit confusing. Just remember the index starts with 1 here
-- The second argument is the number of characters starting the first argument index

SELECT first_name,
LEFT(first_name, 4) AS first_four,
RIGHT(first_name, 4) AS last_four,
SUBSTRING(first_name, 2, 3) AS Middle_tree,
birth_date,
SUBSTRING(birth_date, 6, 2) AS Birth_month 
FROM Parks_and_Recreation.employee_demographics;

SELECT *
FROM Parks_and_Recreation.employee_demographics;

INSERT INTO Parks_and_Recreation.employee_demographics
VALUES (14, 'aaala', 'Smith', 333, 'Male', '1999-09-30');


SELECT first_name,
REPLACE(first_name, 'a', 'zz') -- This one is case sensitive, and replace replaces all similar char sequence in the string
FROM Parks_and_Recreation.employee_demographics;

SELECT LOCATE('x', 'Alexander');

SELECT first_name, LOCATE('An', first_name) -- For the locate, the first argument is the thing you want to locate, the second argument is the full string
FROM Parks_and_Recreation.employee_demographics;

SELECT CONCAT(first_name, ' ', last_name) AS name, first_name, last_name
FROM Parks_and_Recreation.employee_demographics
;

-- CASE statements
-- Kinda like if else statements
SELECT first_name,
last_name,
age,
CASE
	WHEN age <= 30 THEN 'Young'
    WHEN age BETWEEN 31 AND 50 THEN 'Old'
    WHEN age >= 50 THEN 'On death\'s door'
END AS Age_bracket
FROM Parks_and_Recreation.employee_demographics
;

SELECT first_name, last_name, salary,
CASE
	WHEN salary < 50000 THEN salary * 1.05
    WHEN salary > 50000 THEN salary * 1.07
END AS New_salary,
CASE
	WHEN dept_id = 6 THEN salary * 1.10
END AS Bonus
FROM Parks_and_Recreation.employee_salary;

-- Subquries
SELECT * 
FROM Parks_and_Recreation.employee_demographics
WHERE employee_id IN (SELECT employee_id
						FROM Parks_and_Recreation.employee_salary
                        WHERE dept_id = 1)
;

-- This one is wrong, not the average of the groups
SELECT first_name, salary, AVG(salary)
FROM Parks_and_Recreation.employee_salary
GROUP BY first_name, salary;

SELECT first_name, salary,
(SELECT AVG(salary) 
FROM Parks_and_Recreation.employee_salary)
FROM Parks_and_Recreation.employee_salary;

SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM Parks_and_Recreation.employee_demographics
GROUP BY gender;

SELECT gender, AVG(avg_age), AVG(max_age)
FROM 
(SELECT gender, 
AVG(age) AS avg_age,
MAX(age) AS max_age, 
MIN(age), 
COUNT(age)
FROM Parks_and_Recreation.employee_demographics
GROUP BY gender) AS agg_table
GROUP BY gender;

-- Window functions
SELECT gender, AVG(salary) as avg_salary
FROM Parks_and_Recreation.employee_demographics AS dem
JOIN Parks_and_Recreation.employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
;

-- Basically this lets us keep the column values which we have to lose because of lack of aggregation with group by
SELECT dem.first_name, dem.last_name, AVG(salary) OVER(PARTITION BY gender) AS avg_salary
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    

SELECT dem.first_name, dem.last_name, SUM(salary) OVER(PARTITION BY gender) AS sum_salary
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
SELECT dem.first_name, 
dem.last_name, 
salary,
SUM(salary) OVER(PARTITION BY gender ORDER BY dem.employee_id) AS rolling_tota
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- Simply adding a serial number column
SELECT dem.employee_id,
dem.first_name, 
dem.last_name, 
salary,
ROW_NUMBER() OVER()
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;

-- This will add serial numbers based on the gender
SELECT dem.employee_id,
dem.first_name, 
dem.last_name, 
salary,
ROW_NUMBER() OVER(PARTITION BY gender)
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- Add serial number based on the gender and sort by the salary
SELECT dem.employee_id,
dem.first_name, 
dem.last_name, 
salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC)
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- The rank will do something like the ROW_NUMBER but, rank duplicate the same id for the similar value of the order by columns
-- the normal rank will, add the same id to all same values, but it will skip to the right number in the sequence for the next item   
SELECT dem.employee_id,
dem.first_name, 
dem.last_name, 
salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- DENSE_RANK simply breaks this "keeping the sequence" and assign the next number to the next value
SELECT dem.employee_id,
dem.first_name, 
dem.last_name, 
salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num,
DENSE_RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS desne_rank_num
FROM employee_demographics as dem
JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id;
    
-- CTEs (Common Table expressions)
WITH CTE_example AS
(
SELECT gender, AVG(salary) AS avg_sal, MAX(salary) AS max_sal, MIN(salary) AS min_sal, COUNT(salary) AS count_sal
FROM Parks_and_Recreation.employee_demographics as dem
JOIN Parks_and_Recreation.employee_salary as sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
SELECT AVG(avg_sal)
FROM CTE_example;

-- The CTE (Common Table expression) can only be used right after defining it, cannot be used outside this scope
-- A more appropriate use case of Common Table Expression is when we have multiple conditions
-- and we want to make the thing neat and clean. Common Table Expression will help to identify the 
-- common parts of the overall calculations and write them cleanly
WITH CTE_example AS
(
SELECT employee_id, gender, birth_date
FROM Parks_and_Recreation.employee_demographics
WHERE employee_demographics.birth_date > '1985-01-01'
),
CTE_example2 AS
(
SELECT employee_id, salary
FROM Parks_and_Recreation.employee_salary
WHERE salary > 50000
)
SELECT *
FROM CTE_Example AS ct1
JOIN CTE_Example2 AS ct2
	ON ct1.employee_id = ct2.employee_id
;

-- We can specify the name of the columns in the Common table expression headers
-- Whatever we put in the header will be forced as the column names
WITH CTE_example (G, AvgS, MS, MinS, CS) AS
(
SELECT gender, AVG(salary) AS avg_sal, MAX(salary) AS max_sal, MIN(salary) AS min_sal, COUNT(salary) AS count_sal
FROM Parks_and_Recreation.employee_demographics as dem
JOIN Parks_and_Recreation.employee_salary as sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
SELECT *
FROM CTE_example;

-- Temporary Tables
-- Store intermideate results for a complex query

CREATE TEMPORARY TABLE temp_table
(
first_name VARCHAR(50),
last_name VARCHAR(50),
fav_movies VARCHAR(100)
);

INSERT INTO temp_table
Values ("alu", "kopi", "The Matrix");


SELECT * 
FROM temp_table;

CREATE TEMPORARY TABLE salary_over_50k
SELECT * 
FROM Parks_and_Recreation.employee_salary
WHERE salary > 50000;

SELECT * 
FROM salary_over_50k;

-- Stored procedure
-- To store complex queries in the same place

-- This is a very simple stored procedure
-- Sometimes it's better to add the database you are using right now.
USE Parks_and_Recreation;

CREATE PROCEDURE large_salaries()
SELECT *
FROM Parks_and_Recreation.employee_salary
WHERE salary > 50000;

-- To call a stored procedure
CALL large_salaries();

-- This will end up not working as expected since the ; denotes the delimeter, we need to fix the delineter
USE Parks_and_Recreation;
DROP PROCEDURE IF EXISTS large_salaries_2;
CREATE PROCEDURE large_salaries_2()
SELECT *
FROM employee_salary
WHERE salary > 50000;
SELECT *
FROM employee_salary
WHERE salary > 10000;

CALL large_salaries_2();

-- The fixed version
USE Parks_and_Recreation;
DROP PROCEDURE IF EXISTS large_salaries_2;
DELIMITER $$
CREATE PROCEDURE large_salaries_2()
BEGIN
	SELECT *
	FROM employee_salary
	WHERE salary > 50000;
	SELECT *
	FROM employee_salary
	WHERE salary > 10000;
END$$
DELIMITER ;

CALL large_salaries_2();

-- Triggers and Events
SELECT * 
FROM Parks_and_Recreation.employee_demographics;

SELECT *
FROM Parks_and_Recreation.employee_salary;

DELIMITER $$
CREATE TRIGGER employee_insert
	AFTER INSERT ON Parks_and_Recreation.employee_salary
    FOR EACH ROW --  These few lines are just the setup for the trigger
BEGIN 
	INSERT INTO Parks_and_Recreation.employee_demographics (employee_id, first_name, last_name)
    VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
END $$
DELIMITER ;

INSERT INTO employee_salary (employee_id, first_name, last_name, occupation, salary, dept_id)
VALUES (15, 'X', 'Y', 'lala', 100000, 3);

SELECT *
FROM employee_salary;

SELECT *
FROM employee_demographics;

-- Events
-- This is more of a scheduled workflow, trigger on the other hand, gets triggered when something happens
DELIMITER $$
CREATE EVENT delete_retirees
ON SCHEDULE EVERY 30 SECOND
DO
BEGIN
	DELETE
    FROM employee_demographics
    WHERE age >= 60;
END $$
DELIMITER ;

SELECT * 
FROM Parks_and_Recreation.employee_demographics;

-- You can view the configuration variables here
-- Sometimes the event scheduler can be turned off, you have to turn it on
-- Sometimes the safe delete settings could also be turned off in the tables settings
-- we simply need to turn it back up and try again
SHOW VARIABLES;
SHOW VARIABLES LIKE 'event%';

-- Data cleaning



