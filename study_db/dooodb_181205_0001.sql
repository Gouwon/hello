create table Club(
	id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    createdate timestamp not null default current_timestamp,
    leader int unsigned,
    constraint foreign key fk_leader_student(leader) references Student(id)
    );
    
desc Student;
desc Club;
show create table Club;

create table Prof(
	id	smallint unsigned not null auto_increment primary key,
    name varchar(31),
    likecnt int default 0
    );

create table Subject( 
	id smallint unsigned not null auto_increment primary key,
    name varchar(31),
    prof smallint unsigned,
    constraint foreign key fk_prof_prof(prof) references Prof(id)
    on delete set null
);

create table Enroll( 
	id	int unsigned not null auto_increment primary key,
    subject smallint unsigned,
    student int(11) unsigned
);

alter table Enroll
	  change subject subject smallint unsigned not null;
alter table Enroll
	  change student student int(11) unsigned not null;

alter table Enroll
	  add constraint foreign key fk_subject_subject(subject) references Subject(id);
    
alter table Enroll
	  add constraint foreign key fk_student_student(student) references Student(id);
    

insert into Club(name, leader) values('미술부', 300);
select * from Club;

select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id;

select ceil(rand() * 10) from dual;
select * from Prof;
insert into Prof(name, likecnt) select name, ceil(rand() * 10) from Student order by rand() limit 100;

select * from Subject;
desc Subject;
insert into Subject(name, prof)
		select '국어', id from Prof order by rand() limit 10;
update Subject set name = '물리' where id =3;
update Subject set name = '가정' where name = '국어' and id != 10 limit 1;

select '국어', id from Prof order by rand() limit 10;

select * from Enroll;
desc Enroll;

select name from Subject order by rand();
-- insert into Enroll(subject, student) select sb.id, st.id from Subject sb, Student st order by rand();

insert into Enroll(subject, student) select 1, st.id from Subject sb, Student st order by rand();
insert into Enroll(subject, student) select sb.id, st.id from Subject sb, Student st order by rand() limit 1000;

select sb.id, st.id from Subject sb, Student st order by rand();

insert into Enroll(subject, student) 
		select sb.id, (case when st.id <= 501 then st.id else 1000 end) from Subject sb, Student st 
																  order by rand() limit 1000;

-- select sb.id, (case when st.id <= 501 then st.id else 1000 end) from Subject sb, Student st order by rand() limit 1000;
update Enroll set subject = (select id from Subject order by rand() limit 1) where id > 0;

----- select st.id, (select id from Subject order by rand() limit 1) from Student st order by rand();
insert into Enroll(student, subject)
select st.id, (select id from Subject order by rand() limit 1) from Student st;
-- 1000명이 1과목씩 듣고 있다.

-- 랜덤으로 뽑은 학생들이 랜덤으로 한 과목을 듣고 있다. 
insert into Enroll(student, subject)
select st.id, (select id from Subject order by rand() limit 1) 
from Student st order by rand()
on duplicate key update student = student;

-- insert into Enroll(subject, student) 

															
-- case when rand() <= 0.5 then 
-- when st.id <= 501 then st.id else 1000


select * from Enroll;
select count(distinct student) from Enroll;
select subject, count(*) from Enroll group by subject;
select subject, student, count(*) from Enroll group by subject, student having count(*) > 1;
truncate Enroll;

select count(*) from Student;
select * from Student order by birth limit 10;
select * from Student where name like '김%%' order by name limit 10;
select addr from Student group by addr having addr = '서울%' order by id; -- 잘못된것
select * from Student where addr like '서울%'order by id desc;
select * from Student where addr like '서울%' and birth >= '90_' order by id desc;
select * from Student where addr like '서울%' and (birth between '900101' and '991231' or birth between '000101' and '181231') order by id desc;

-- 이너조인
select Subject.*, Prof.name
from Subject
inner join Prof on Subject.prof = Prof.id;





select id from Student order by rand() limit 1;
select id from Subject order by rand() limit 1;
insert into Enroll set student = (select id from Student order by rand() limit 1), 
					   subject = (select id from Subject order by rand() limit 1);

insert into Enroll                       
select st.id, id = (select id from Subject sb order by rand() limit 1) from Student st;

select id, (select id from Subject order by rand() limit 1) sid from Student order by id;


insert into Enroll(subject, student)
select sbj.id, s.id
  from (select id from Subject where id not in (select distinct subject from Enroll) order by id limit 1) sbj, 
       (select id from Student order by rand() limit 100) s;

