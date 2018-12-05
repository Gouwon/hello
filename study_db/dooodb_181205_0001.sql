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

insert into Enroll(student, subject) values 1, select id from Subject order by rand();
insert into Enroll(subject, student) select sb.id, st.id = default(1) from Subject sb, Student st order by rand();
insert into Enroll(subject, student) select sb.id, (case when st.id = 1 then st.id else 1 end) from Subject sb, Student st order by rand();

select subject, count(*) from Enroll group by subject;
truncate Enroll;

select * from Student;