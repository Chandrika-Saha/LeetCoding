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

SELECT length('Hello');