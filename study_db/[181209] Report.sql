-- report1 작업
start transaction;

create table Grade(
    id smallint unsigned auto_increment primary key,
   subject mediumint not null ,
   student  int(10) unsigned NOT NULL,
   midterm smallint unsigned not null default 0,
   finalterm smallint unsigned not null default 0,
    constraint foreign key fk_stusbj_enroll(student, subject) references Enroll(student, subject) on delete cascade
);

select * from Grade;
desc Grade;

insert into Grade(student, subject) select student, subject from Enroll;

update Grade set midterm = ceil((0.5 + rand() / 2) * 100) where id > 0;
update Grade set finalterm = ceil((0.5 + rand() / 2) * 100) where id > 0;


select g.*, sbj.name, stu.name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id;
                                   
 
 
 
 
 select report1.*, (case when report1.avg_score = 100 then 'A+'
                                 when report1.avg_score >= 90 then 'A'
                                when report1.avg_score >= 80 then 'B'
                                when report1.avg_score >= 70 then 'C'
                                when report1.avg_score >= 60 then 'D'
                                else 'F' end) grade
   from
(                                   
select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
) report1;



-- report1 ( 과목, 학생명, 중간, 기말, 총점, 평균, 학점, 석차 (과목, 성적, 이름순))




select report1.sbj_name, report1.stu_name, 
          report1.midterm, report1.finalterm, report1.total_score, report1.avg_score, report1.rating
from
(
 select report.*, (case when report.avg_score = 100 then 'A+'
								  when report.avg_score >= 90 then 'A'
                                  when report.avg_score >= 80 then 'B'
                                  when report.avg_score >= 70 then 'C'
                                  when report.avg_score >= 60 then 'D'
                                  else 'F' end) rating
   from
(                                   
select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
) report
) report1
order by report1.sbj_name asc, report1.avg_score desc
;


commit;



-- report2 작업


start transaction;



select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
;



-- 최고 득점자만 뽑은 면 된다.


select report.sbj_name, max(report.avg_score), (if(report.avg_score = max(report.avg_score), report.stud  count(*)
from
(
select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
)report

group by report.subject asc
having max(report.avg_score)
order by report.sbj_name limit 10
;






select report.sbj_name, report.stu_name, report.*
from
(
select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
)report
where report.subject = report.subject
order by report.sbj_name asc, report.avg_score desc

;








commit;








-- report3 작업 



start transaction;


select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
;






 select report1.*, (case when report1.avg_point = 100 then 'A+'
                                 when report1.avg_point >= 90 then 'A'
                                when report1.avg_point >= 80 then 'B'
                                when report1.avg_point >= 70 then 'C'
                                when report1.avg_point >= 60 then 'D'
                                else 'F' end) rating
   from
(           
select  report.stu_name, count(*), sum(report.total_score) total_point, avg(report.avg_score) avg_point
from 
(
select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 
						((g.midterm + g.finalterm) / 2) avg_score
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id
) report
group by report.student
order by report.stu_name asc
)report1
;


commit;


