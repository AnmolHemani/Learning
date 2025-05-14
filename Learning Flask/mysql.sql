create database job_form;
use job_form;
drop table job_application;
create table job_application (
    id int auto_increment primary key,
    name varchar(100),
    email varchar(100),
    phone varchar(20),
    address varchar(100),
    college_name varchar(100),
    graduation_year varchar(100),
    stream varchar(100),
    position varchar(100),
    resume_path VARCHAR(255)
);
select * from job_application;