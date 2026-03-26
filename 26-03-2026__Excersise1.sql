create database company_training;

use company_training;

create table employees(
				emp_id int primary key ,
                emp_name varchar(100),
                department varchar(50),
                city varchar(50));
                
create table projects(
				project_id int primary key,
                emp_id int,
                project_name varchar(100),
                project_budget decimal(10,2),
                project_status varchar(50));
                
INSERT INTO employees VALUES 
					(1, 'Rohan Mehta', 'IT', 'Hyderabad'), 
					(2, 'Sneha Iyer', 'IT', 'Bangalore'), 
					(3, 'Kiran Patel', 'Finance', 'Mumbai'), 
					(4, 'Ananya Das', 'HR', NULL), 
					(5, 'Rahul Sharma', 'IT', 'Delhi'), 
					(6, NULL, 'Marketing', 'Chennai');
                    
INSERT INTO projects VALUES 
					(101, 1, 'AI Chatbot', 120000, 'Active'), 
					(102, 1, 'ML Prediction', 90000, 'Active'), 
					(103, 2, 'Data Warehouse', 150000, 'Active'), 
					(104, 3, 'Financial Dashboard', 80000, 'Completed'), 
					(105, NULL, 'Website Revamp', 60000, 'Pending'), 
					(106, 8, 'Mobile App', 100000, 'Active');
                    
select employees.emp_name,projects.project_name,projects.project_budget 
										from employees inner join projects 
										on employees.emp_id=projects.emp_id;
                                        
select employees.emp_name,projects.project_name 
										from employees left join projects 
										on employees.emp_id=projects.emp_id;                                        

select projects.project_name,employees.emp_name  
										from employees right join projects 
										on employees.emp_id=projects.emp_id;         
       
(select employees.emp_name,projects.project_name 
								from employees left join projects 
								on employees.emp_id=projects.emp_id)                                        
union
(select projects.project_name,employees.emp_name  
								from employees right join projects 
								on employees.emp_id=projects.emp_id);         
       
       
select employees.emp_name,projects.project_name,projects.project_budget 
										from employees cross join projects 
										on employees.emp_id=projects.emp_id;        
                                        
select projects.project_name,employees.emp_name 
										from employees inner join 
                                        projects on employees.emp_id=projects.emp_id
                                        where department = "IT";
                    
                    
select employees.emp_name,projects.project_name,projects.project_budget 
										from employees inner join projects 
										on employees.emp_id=projects.emp_id
                                        where projects.project_budget>100000;
                                        
select employees.emp_name,projects.project_name 
										from employees inner join projects 
										on employees.emp_id=projects.emp_id
                                        where city="Hyderabad";
                                        
select employees.emp_name,count(projects.project_name) as no_of_project from 
													employees left join projects on 
                                                    employees.emp_id=projects.emp_id
                                                    group by employees.emp_name;
                                                  
                                                           
select employees.emp_name,sum(projects.project_budget) as total_budget from 
													employees left join projects on
                                                    employees.emp_id=projects.emp_id
                                                    group by employees.emp_name;

select employees.department,avg(projects.project_budget) as avg_per_department from 
													employees inner join projects on 
                                                    employees.emp_id=projects.emp_id
                                                    group by employees.department;  
                                                    
select employees.department , count(projects.project_name) as total_project_per_dept from 
													employees left join projects on 
                                                    employees.emp_id=projects.emp_id
                                                    group by employees.department;
                                                    
select employees.department , sum(projects.project_budget) as total_budget_per_dept from 
													employees left join projects on 
                                                    employees.emp_id=projects.emp_id
                                                    group by employees.department;
																							
select city,count(emp_name) as employee_per_city from
												employees group by city;		
      
select employees.emp_name,count(projects.project_name) from employees 
															inner join projects on 
                                                            employees.emp_id=projects.emp_id
                                                            group by employees.emp_name
                                                            having count(projects.project_name)>1;
                                                            
                                                            
select employees.department, sum(projects.project_budget) as tot_budget from employees
																inner join projects on 
                                                                employees.emp_id=projects.emp_id
                                                                group by department 
                                                                having sum(projects.project_budget)>150000;
                                                    
select employees.emp_name, sum(projects.project_budget) as tot_budget from employees
																inner join projects on 
                                                                employees.emp_id=projects.emp_id
                                                                group by emp_name 
                                                                having sum(projects.project_budget)>100000;
                                                                
select employees.emp_name,employees.department,sum(projects.project_budget) as total_budget from employees
																inner join projects on 
                                                                employees.emp_id=projects.emp_id
                                                                group by employees.emp_name,employees.department
                                                                having sum(projects.project_budget)>100000
                                                                order by total_budget desc;
                                                                                                                              