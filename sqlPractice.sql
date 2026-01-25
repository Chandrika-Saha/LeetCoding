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