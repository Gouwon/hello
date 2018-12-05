select * from Student;
select count(*) from Student;

alter table Student
add column gender tinyint(0) not null after birth;

update Student 
	set gender = (case when rand() > 0.5 then 1  
						else 0 end)
	where id > 0;

update Student set gender = (case when name like '%혜%' or name like '%솔%' then 0 else 1 end);
update Student set gender = 1 where not (case when name like '%혜%' or name like '%솔%' then 0 else 1 end) and id > 0;
update Student set gender = mod(id, 2);

alter table Student
change column gender gender tinyint(4) null;

select rand();

select gender, count(*) from Student group by gender;

