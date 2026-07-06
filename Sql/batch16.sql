create database student_management1;
show databases;
use student_management;

drop database student_management1;


create table student_details1(id INT  NOT NULL auto_increment,
	student_name varchar(250),
    course varchar(100),
    status int default 1,
    created_at timestamp  default current_timestamp,
    primary key (id)
    );
drop table student_details;    


alter table stud_det rename to stud_details;
alter table stud_details rename column active_status to status;
select * from stud_det where id = 1;
select * from stud_det where course="python";
select * from stud_det where id in(1,9);
select * from student_details1;
select * from stud_details;
alter table stud_details change course course bigint ;
select course,count(*) as student_count from stud_det group by course;
select * from stud_details order by student_name ASC;
insert into stud_det (student_name,course) values("Azar","JAVA"),("Nagaraj","Python");
update stud_details set course="1"  where id<=6  and student_name="RR";
delete from stud_details where id=7;

-- create index index_name on stud_details(id);
-- drop index index_name on stud_details;

create table course_details (
id int not null auto_increment,
course_name varchar(250),
fees decimal(12,2),
status boolean default true,
primary key(id)
);

insert into course_details (course_name,fees) values ("python",200),("java",300);
select * from stud_details;
select * from course_details;
alter table stud_details add constraint course_det foreign key(course) references course_details(id);

select s.student_name,c.course_name from stud_details as s join course_details as c on s.course =c.id ;
select * from course_details as c right join stud_details as s on c.id=s.course;

-- 2 tables create 
-- create Database employee_management
-- 1 department  id , depart_name 
-- 2. employess , id,employee_name,department,salary

create database employee_management;
use employee_management;

create table department 
(
id int not null auto_increment,
depart_name varchar(120),
primary key (id)
);

create table employess (
	id int not null,
    employee_name varchar(250),
    department int,
    salary decimal(12,2),
    active_status Boolean default True,
    create_at timestamp default current_timestamp,
    primary key (id)
);
alter table employess change id id int not null auto_increment;

select * from department;
insert into department (depart_name) values ('accounts'),('sales');
select * from employess limit 10;
insert into employess (employee_name,department,salary) values ('Monuis',1,2500000),('prem',1,1213333);

select department,count(*) as cnt from employess group by department;
select department,count(*) as cnt from employess group by department having  cnt<5;

select * from employess as e where not exists( select 1 from department d where  d.id=e.department and d.depart_name='it');

-- join 
-- inner join ,left,right,cross
select * from employess e   join department as d on e.department = d.id  ;
select * from employess e   left join department as d on e.department = d.id  ;
select * from employess e   right join department as d on e.department = d.id  ;
select * from employess e  cross join department as d on e.department = d.id  ;

create index idx_employee_name on employess(employee_name);
-- drop index idx_employee_name
show index from employess;
show errors;

create view  emp_salry_list as 
select e.id,e.employee_name,d.depart_name,e.salary from employess as e 
join department as d 
on e.department = d.id  ;

select * from emp_salry_list order by depart_name limit 2,5; 

























  

