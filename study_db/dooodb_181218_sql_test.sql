-- 1번문제) 학번, 학생명, 수강과목수, 전과목 평균점수 칼럼을 갖는 View를 작성하시오.

select stu.id as '학번', max(stu.name) as '학생명', count(*) as '수강과목수', round((avg(g.midterm + g.finalterm) / 2), 1) as '전과목 평균점수'
	from Enroll as e inner join Grade as g on e.id = g.enroll
					 inner join Student as stu on stu.id = e.student
	group by stu.id
;

create view v_stu_grade
	as select stu.id as '학번', max(stu.name) as '학생명', count(*) as '수강과목수', round((avg(g.midterm + g.finalterm) / 2), 1) as '전과목 평균점수'
		from Enroll as e inner join Grade as g on e.id = g.enroll
						 inner join Student as stu on stu.id = e.student
		group by stu.id;
select * from v_stu_grade;



-- 2번문제) 학번을 주면 해당 학생의 전과목 평균을 반환하는 Stored Function을 작성하시오.

select round(avg(g.midterm + g.finalterm), 1) as '전과목 평균점수'
	from Enroll as e inner join Grade as g on e.id = g.enroll
	where e.student = 1;
    
desc Student;
desc v_stu_grade;

delimiter //
create function f_stu_grade(agv_stuid int unsigned) returns mediumint
    begin
		return (select round(avg(g.midterm + g.finalterm), 1) as '전과목 평균점수'
					from Enroll as e inner join Grade as g on e.id = g.enroll
					where e.student = agv_stuid);
    end //
delimiter ;

select f_stu_grade(2);



-- 3번문제) 클럽(Club)을 하나 추가하면 클럽회원(ClubMember)으로 임의의 한 학생(Student)을 회장으로 자동 등록하는 Trigger를 작성하시오.
/* 
	클럽(on Club)이 인서트 된 후(after insert), 클럽회원 칼럼에 한 명의 학생을 insert하는 데, level을 2로 주자.
    한 명의 학생은 전체 학생들 중에서 이미 기존 클럽의 level이 1, 2가 아닌 사람 중에서 뽑아야 한다.
    따라서 먼저 이 학생들을 찾아보자.
*/

desc Student;
select count(*) from Student;
desc Club;
select * from Club;
desc ClubMember;
select * from ClubMember;

-- 한 명의 학생은 전체 학생들 중에서 이미 기존 클럽의 level이 1, 2가 아닌 사람 중에서 뽑아야 한다.
select stu.*
	from Student as stu
    where stu.id not in (select cm.student from ClubMember as cm where cm.level = 1 or cm.level = 2);
    
select cm.student, cm.level from ClubMember as cm where cm.level = 1 or cm.level = 2;

select cm.level, count(*) from ClubMember as cm group by cm.level;


-- 클럽 한 개 만들기
insert into Club(name) value('신문부');



insert into ClubMember(club, studnet, level)
	values (
			(select id from Club where name = new.name), 
			(select stu.id
				from Student as stu
				where stu.id not in (select cm.student from ClubMember as cm where cm.level = 1 or cm.level = 2)
				order by rand() limit 1), 
			2);

select subject, count(*) from Enroll group by subject;
select * from Subject;

-- 트리거 만들기
drop trigger tr_club_leader;


delimiter //
create trigger tr_club_leader
	after insert
    on Club for each row
    begin
		insert into ClubMember(club, student, level)
			values ((select id from Club where name = new.name), 
					(select stu.id from Student as stu
						where stu.id not in (select cm.student from ClubMember as cm where level = 1 or level = 2)
						order by rand() limit 1), 
					2)    
;
    end //
delimiter ;


-- 트리거 확인하기

select * from ClubMember
	where club = (select max(id) from Club);
    
    
    
-- 4번문제) 지난 학기 데이터(수강학생수, 성적 등)를 기준으로 인기 교수(강좌) Top 3을 추천하는 Stored Procedure을 작성하시오. 단, 데이터의 가중치는 자유롭게 부여하시오.
-- 학생수, 성적, likecnt 을 이용하여 가장 인기있는 교수(=과목)를 구하라. --프로시저

select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
       count(*) as stu_cnt, avg((g.midterm + g.finalterm) / 2) as avg_score, 
       avg(pr.likecnt) prof_likecnt
	from Enroll e inner join Subject sbj on sbj.id = e.subject
				  inner join Prof pr on pr.id = sbj.prof
                  inner join Grade g on e.id = g.enroll
	group by sbj.id
    order by count(*) desc, avg((g.midterm + g.finalterm) / 2) desc, avg(pr.likecnt) desc
;


select count(distinct ee.student) from Enroll ee ;

select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
       (count(*)) as stu_cnt, avg((g.midterm + g.finalterm) / 2) as avg_score, 
       (avg(pr.likecnt))  prof_likecnt,
       ( (count(*)/(select count(distinct ee.student) from Enroll ee) * 0.15) + 
         (avg((g.midterm + g.finalterm) / 2) * 0.4) +
		(avg(pr.likecnt) * 0.45)) estimation
	from Enroll e inner join Subject sbj on sbj.id = e.subject
				  inner join Prof pr on pr.id = sbj.prof
                  inner join Grade g on e.id = g.enroll
	group by sbj.id
    order by estimation desc
;


delimiter //
create procedure sp_popular_prof()
        begin
			select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
				   (count(*)) as stu_cnt, (avg((g.midterm + g.finalterm) / 2)) as avg_score, 
				   (avg(pr.likecnt))  prof_likecnt,
				   ( (count(*)/(select count(distinct ee.student) from Enroll ee) * 1.5) + 
					 (avg((g.midterm + g.finalterm) / 200) * 0.4) +
					(avg(pr.likecnt) * 0.45)) estimation
				from Enroll e inner join Subject sbj on sbj.id = e.subject
							  inner join Prof pr on pr.id = sbj.prof
							  inner join Grade g on e.id = g.enroll
				group by sbj.id
				order by estimation desc limit 3;
            
        end //
delimiter ;

select * from Prof;
call sp_popular_prof();

-- 5번문제) 오라클 문제
/* 'Marketing’ 부서에 속한 직원의 이름(last_name), 급여(salary), 
	부서이름(department_name)을 조회하시오. 
	단, 급여는 80번 부서의 평균보다 적게 받는 직원 정보만 출력되어야 한다. */

select *
  from Employees e inner join Departments d on d.department_id = e.department_id
  where d.department_name = 'Marketing'
        and e.salary < (
                select round(avg(ee.salary), 0) salary
                  from Employees ee
                  where ee.department_id = 80
                  group by ee.department_id
        );
        

select round(avg(ee.salary), -1) salary
                  from Employees ee
                  where ee.department_id = 80
                  group by ee.department_id;



-- 6번문제) 과목별 Top3 학생의 이름과 성적을 한줄로 표현하는 리포트를 아래와 같이 작성하시오.(성적은 중간, 기말 평균이며, 과목명 오름차순으로 정렬하시오.)

drop procedure if exists sp_subject_ranking;

delimiter //

create procedure sp_subject_ranking()
	begin
		declare _isdone boolean default false;
        declare _subject varchar(31); 
        declare _student varchar(45); 
        declare _avr varchar(45);
        declare local_i smallint default 1;
        
        declare _ttt int; -- QQQ
                
        declare cursor_1 cursor
			for select * from T_table0;
		
        declare continue handler 
			for not found set _isdone = True;

		drop table if exists T_table0;
        create temporary table T_table0(
			subject varchar(31),
			student varchar(45),
			avr varchar(45)
			);

		drop table if exists T_table1;
        create temporary table T_table1(
			subject varchar(31),
            student1 varchar(31),
            score1 varchar(31),
            student2 varchar(31),
            score2 varchar(31),
            student3 varchar(31),
            score3 varchar(31),
            isdone boolean default false
            );
            

		while (local_i <= 10) do
			insert into T_table0(subject, student, avr)
            select max(sub.subject), group_concat(sub.student) as student, group_concat(sub.avr) as avr
				from (select sbj.name as subject, stu.name as student, vge.avr as avr
								from v_grade_enroll as vge inner join Subject as sbj on sbj.id = vge.subject
																	        inner join Student as stu on stu.id = vge.student
                                where vge.subject = local_i order by avr desc limit 3) sub;
				
			set local_i = local_i + 1;
		end while;            
            
		select * from T_table0;
        
        open cursor_1;
            
			loop1 : loop
                
				fetch cursor_1 into _subject, _student, _avr;
                
                if _isdone then
					leave loop1;
				end if;
                
				insert into T_table1 value(_subject, substring_index(_student, ',', 1), substring_index(_avr, ',', 1),
															substring_index(substring_index(_student, ',', 2),',',-1),
                                                            substring_index(substring_index(_avr, ',', 2),',',-1),
                                                            substring_index(substring_index(_student, ',', 3),',',-1),
                                                            substring_index(substring_index(_avr, ',', 3),',',-1), _isdone);                
            
				
                
            end loop loop1;
            
        close cursor_1;
        
        select * from T_table1 order by subject;
        
    end //

delimiter ;

call sp_subject_ranking();


select subject_name, student_name, max(avr)
		from v_grade_enroll 
		group by subject_name, student_name 
		order by 1, 3 desc;