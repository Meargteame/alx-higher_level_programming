USE sql_hr 

SELECT *
FROM employees e 
JOIN employees m
-- self join commited 

ON e.reports_to = m.employee_id 


