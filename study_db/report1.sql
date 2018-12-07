start transaction;

create table Grade(
	id int not null auto_increment,
    subject smallint unsigned not null,
    student int unsigned not null,
    midterm smallint not null default 0,
    finalterm smallint not null default 0,
    primary key(id),
    constraint foreign key fk_grade_enroll (subject, student) references Enroll (subject, student)
	)
    ;

desc Grade;
show index from Grade;
select count(*) from Grade;
select * from Grade;

insert into Grade(subject, student)
select subject, student
  from Enroll;
  
update Grade set midterm = ceil((0.5 + rand() / 2) * 100), 
				finalterm = ceil((0.5 + rand() / 2) * 100) 
			 where id > 0;
    


select sbj.name as sbj_name, stu.name as stu_name, g.midterm, g.finalterm, 
	   (g.midterm + g.finalterm) as total_score,
       ((g.midterm + g.finalterm) / 2) as avg_score
  from Grade g inner join Subject sbj on g.subject = sbj.id
			   inner join Student stu on g.student = stu.id;


USE `dooodb`;
CREATE  OR REPLACE VIEW report1 AS
select sbj.name as sbj_name, stu.name as stu_name, g.midterm, g.finalterm, 
	   (g.midterm + g.finalterm) as total_score,
       ((g.midterm + g.finalterm) / 2) as avg_score
  from Grade g inner join Subject sbj on g.subject = sbj.id
			   inner join Student stu on g.student = stu.id;
    

select *, (case when report1.avg_score = 100 then 'A+'
								 when report1.avg_score >= 90 then 'A'
                                 when report1.avg_score >= 80 then 'B'
                                 when report1.avg_score >= 70 then 'C'
                                 when report1.avg_score >= 60 then 'D'
                                 else 'F' end) grade
 from report1;

desc report1;
 
 create temporary table t_report1(
	sbj_name varchar(31) DEFAULT NULL,
    stu_name varchar(31) not null,
    midterm smallint unsigned not null default 0,
    finalterm smallint unsigned not null default 0,
    total_score int(7) not null default 0,
    avg_score decimal(10, 4)
 );
 
alter table t_report1 add column grade varchar(10);

select * from t_report1;

insert into t_report1(sbj_name, stu_name, midterm, finalterm, total_score, avg_score, grade)
select * from 
(
select *, (case when report1.avg_score = 100 then 'A+'
								 when report1.avg_score >= 90 then 'A'
                                 when report1.avg_score >= 80 then 'B'
                                 when report1.avg_score >= 70 then 'C'
                                 when report1.avg_score >= 60 then 'D'
                                 else 'F' end) grade
 from report1
) sub_rp1
order by sub_rp1.sbj_name, sub_rp1.avg_score desc, sub_rp1.stu_name;
 
 
