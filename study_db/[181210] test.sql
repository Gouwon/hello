-- 181210 SQL 시험

-- 1번문제) 학생, 과목, 교수, 수강내역 테이블을 관계를 고려하여 생성하는 DDL을 작성하시오.

CREATE TABLE `Student` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `addr` varchar(30) NOT NULL,
  `birth` varchar(6) NOT NULL,
  `gender` tinyint(4) DEFAULT NULL,
  `tel` varchar(15) NOT NULL,
  `email` varchar(31) NOT NULL,
  `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '등록일시',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;
desc Student;


CREATE TABLE `Enroll` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subject` smallint(5) unsigned NOT NULL,
  `student` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_enroll` (`subject`,`student`),
  KEY `Enroll_ibfk_2` (`student`),
  CONSTRAINT `Enroll_ibfk_1` FOREIGN KEY (`subject`) REFERENCES `Subject` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Enroll_ibfk_2` FOREIGN KEY (`student`) REFERENCES `Student` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2929 DEFAULT CHARSET=utf8;
desc Enroll;
show index from Enroll;

CREATE TABLE `Subject` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) DEFAULT NULL,
  `prof` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_subject_name` (`prof`),
  CONSTRAINT `Subject_ibfk_1` FOREIGN KEY (`prof`) REFERENCES `Prof` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
desc Subject;
show index from Subject;

CREATE TABLE `Prof` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) DEFAULT NULL,
  `likecnt` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
desc Prof;
select * from Prof;




-- 2번문제) 학생테이블과 과목테이블을 활용하여, 수강내역테이블에 테스트용 데이터를 구성하는 DML을 절차적으로 작성하시오.


/* 3번문제) 동아리(Club)별 회원테이블(ClubMember)을 다음과 같이 만들고, 동아리별 50명 내외로 가입시키시오.
(단, Club 테이블의 leader 컬럼을 삭제하고, 리더를 회원테이블의 레벨(level) 2로 등록하시오.) */


start transaction;

select * from Club;
desc Club;
/*
회원테이블을 만들면서 학생테이블(id)과 동아리(id) 테이블 외래키. 
조인해서 leader 가지고오고나서 leader삭제.
가지고온 leader에게 level2 
*/


create table ClubMember(
	id int(10) unsigned not null auto_increment,
    club smallint(5) unsigned comment '클럽번호',
    student int(11) unsigned comment '학번',
    level smallint default 0,
    primary key(id),
    constraint foreign key fk_club(club) references Club(id) on delete cascade,
    constraint foreign key fk_student(student) references Student(id) on delete cascade
    ) charset=utf8;
    
select * from Club;
select * from ClubMember;

-- 기등록된 리더 등록
insert into ClubMember(club, student, level)
select id, leader, 2 from Club;
select * from ClubMember;

-- 기존의 외래키 및 leader 칼럼 삭제
show index from Club;
ALTER TABLE `dooodb`.`Club` 
DROP FOREIGN KEY `Club_ibfk_1`;
ALTER TABLE `dooodb`.`Club` 
DROP COLUMN `leader`,
DROP INDEX `fk_leader_student` ;
show index from Club;
desc Club;


insert into ClubMember(club, student)
select clm.id, s.id
  from (select id from Club where id = 1) clm, 
       (select id from Student order by rand() limit 50) s;
       
select level, count(*) from ClubMember group by level;

select club, count(*) from ClubMember group by club;
truncate ClubMember;

select * from ClubMember where level = 0;

update ClubMember
set level = (case when rand() < 0.5 then 0 else 1 end) where level = 0;



/* 4번문제) 학과(Dept)테이블을 만들고 5개 학과 이상 샘플 데이터를 등록하고, 학생 테이블에 학과 컬럼(dept)을 추가한 후 모든 학생에 대해 랜덤하게 과 배정을 시키시오.
pk(id) 학과명(name) 지도교수(prof) 과대표(student)
*/


start transaction;


create table Dept(
	id smallint(5) unsigned not null auto_increment,
    name varchar(31) comment '학과명',
    prof smallint(5) unsigned comment '교수명',
    student int(11) unsigned comment '과대표',
    primary key(id),
    constraint foreign key fk_prof(prof) references Prof(id),
    constraint foreign key fk_student(student) references Student(id)
    ) charset=utf8;
    
desc Dept;
show index from Dept;
select * from Dept;

insert into Dept(name) value('물리학과');
insert into Dept(name) value('경제학과');
insert into Dept(name) value('체육학과');
insert into Dept(name) value('국문학과');
insert into Dept(name) value('통계학과');
select * from Dept;

update Dept
set prof = (select id from Prof order by rand() limit 1) where id > 0;
select * from Dept;

desc Student;
select * from Student;

-- 학생 테이블에 학과열 추가
ALTER TABLE `dooodb`.`Student` 
ADD COLUMN `dept` SMALLINT(5) unsigned NULL AFTER `regdt`;
-- 학생 테이블 외래키 추가
ALTER TABLE Student 
add FOREIGN KEY fk_dept(dept) references Dept(id);
-- 학과 배정
update Student
set dept = (select id from Dept order by rand() limit 1) where id > 0;
select * from Student;
-- 과대표 선정

update Dept
set student = (
select id from Student where dept = 1 order by rand() limit 1
);
update Dept
set student = (
select id from Student where dept = 2 order by rand() limit 1
);
update Dept
set student = (
select id from Student where dept = 3 order by rand() limit 1
);
update Dept
set student = (
select id from Student where dept = 4 order by rand() limit 1
);
update Dept
set student = (
select id from Student where dept = 5 order by rand() limit 1
);
select * from Dept;

commit;


/* 5번문제) 강의실 테이블(Classroom)을 만들고, 샘플강의실 10개를 등록하고, 과목별 강의실 배치를 위해 과목(Subject) 테이블에 강의실 칼럼(classroom) 추가한 후 배정하시오.*/

create table Classroom(
	id smallint unsigned not null auto_increment,
    name varchar(10) comment '강의실호수',
    primary key(id)
	) charset=utf8;
    
desc Classroom;
select * from Classroom;


insert into Classroom(name) value('101호');
insert into Classroom(name) value('102호');
insert into Classroom(name) value('103호');
insert into Classroom(name) value('104호');
insert into Classroom(name) value('201호');
insert into Classroom(name) value('202호');
insert into Classroom(name) value('203호');
insert into Classroom(name) value('204호');
insert into Classroom(name) value('301호');
insert into Classroom(name) value('302호');
select * from Classroom;

desc Subject;
alter table Subject
  add column classroom smallint unsigned;
desc Subject;

show index from Subject;
alter table Subject
  add constraint foreign key fk_classroom(classroom) references Classroom(id);
show index from Subject;

select * from Classroom;
select * from Subject;

start transaction;

update Subject
set classroom = (select id from Classroom order by rand() limit 1);

select * from Subject;
select classroom, count(*) from Subject group by classroom;
 
select id from Classroom
where id not in (select distinct classroom from Subject)
;
 
update Subject
set classroom = 2
where id = 4;


update Subject
set classroom = 10
where id = 5;


update Subject
set classroom = 5
where id = 7;

select classroom, count(*) from Subject group by classroom;


commit;


/* 6번문제) */

desc Enroll;
show index from Enroll;
