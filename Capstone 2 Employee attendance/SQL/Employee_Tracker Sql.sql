CREATE DATABASE employee_tracker;
USE employee_tracker;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10,2)
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    attendance_date DATE,
    clock_in DATETIME,
    clock_out DATETIME,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    task_name VARCHAR(100),
    tasks_completed INT,
    task_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees VALUES
(101,'Amit Sharma','IT','Developer',50000),
(102,'Priya Reddy','HR','HR Manager',45000),
(103,'Rahul Kumar','Finance','Analyst',55000);

INSERT INTO attendance(employee_id,attendance_date,clock_in,clock_out,status)
VALUES
(101,'2026-05-10','2026-05-10 09:00:00','2026-05-10 18:00:00','Present'),
(102,'2026-05-10','2026-05-10 09:30:00','2026-05-10 17:30:00','Present'),
(103,'2026-05-10',NULL,NULL,'Absent');

INSERT INTO tasks(employee_id,task_name,tasks_completed,task_date)
VALUES
(101,'Bug Fixing',8,'2026-05-10'),
(102,'Recruitment',5,'2026-05-10'),
(103,'Report Analysis',0,'2026-05-10');


SELECT * FROM employees;

UPDATE employees
SET salary = 60000
WHERE employee_id = 101;

DELETE FROM tasks
WHERE task_id = 3;

INSERT INTO attendance(employee_id,attendance_date,clock_in,status)
VALUES
(101,CURDATE(),NOW(),'Present');

UPDATE attendance
SET clock_out = NOW()
WHERE employee_id = 101
AND attendance_date = CURDATE();

DELIMITER //

CREATE PROCEDURE total_working_hours(IN empid INT)
BEGIN
    SELECT employee_id,
           SUM(TIMESTAMPDIFF(HOUR, clock_in, clock_out)) AS total_hours
    FROM attendance
    WHERE employee_id = empid
    GROUP BY employee_id;
END //

DELIMITER ;

CALL total_working_hours(101);

CREATE INDEX idx_employee_id
ON attendance(employee_id);

CREATE INDEX idx_department
ON employees(department);