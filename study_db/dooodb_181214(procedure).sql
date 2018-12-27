/*
drop procedure if exists sp_stu_cnt;

delimiter //
create procedure sp_stu_cnt
				(in _subject_name varchar(31),
				 out _stucnt smallint)
		begin
			select count(*) into _stucnt from Enroll
				where subject = (select id from Subject where name = _subject_name);
        
        end //
delimiter ;
		
        
call sp_stu_cnt('역사', @cnt);
select @cnt;        
*/
/*
start transaction;

call sp_club_memberinfo('요트부', @cnt);
desc Club;

select sub.club_name, sub.stu_name,
		(case sub.cm_level when 2 then '회장'
						   when 1 then '간부'
                           else '평회원' end) as cm_level
from
			(select c.name as club_name, c.id as club_id, stu.name as stu_name, cm.level as cm_level
				from ClubMember cm inner join Club c on c.id = cm.club
									inner join Student stu on stu.id = cm.student
				where c.name = '요트부') sub;

commit;
*/
/*
delimiter //
create procedure sp_club_memberinfo
				(in agvinp_clubname varchar(31))
		begin
			select sub.club_name, sub.stu_name,
					(case sub.cm_level when 2 then '회장'
									   when 1 then '간부'
                                       else '평회원' end) as cm_level
				from
					(select c.name as club_name, c.id as club_id, stu.name as stu_name, cm.level as cm_level
						from ClubMember cm inner join Club c on c.id = cm.club
										   inner join Student stu on stu.id = cm.student
						where c.name = agvinp_clubname) sub
                        order by sub.cm_level desc;
        end //
delimiter ;

call sp_club_memberinfo('요트부');
*/
/*
delimiter //
create procedure sp_club_memberinfo2
				(in agvinp_clubname varchar(31))
		begin
			declare var_club_id smallint default 0;
            set var_club_id = (select id from Club where name = agvinp_clubname);
			select sub.club_name, sub.stu_name,
					(case sub.cm_level when 2 then '회장'
									   when 1 then '간부'
                                       else '평회원' end) as cm_level
				from
					(select c.name as club_name, c.id as club_id, stu.name as stu_name, cm.level as cm_level
						from ClubMember cm inner join Club c on c.id = cm.club
										   inner join Student stu on stu.id = cm.student
						where c.id = var_club_id) sub
                        order by sub.cm_level desc;
        end //
delimiter ;

call sp_club_memberinfo2('요트부');

select * from Prof;
*/

-- 학생수, 성적, likecnt 을 이용하여 가장 인기있는 교수(=과목)를 구하라. --프로시저

select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
       count(*) as stu_cnt, avg(g.midterm + g.finalterm) as avg_score, 
       avg(pr.likecnt) prof_likecnt
	from Enroll e inner join Subject sbj on sbj.id = e.subject
				  inner join Prof pr on pr.id = sbj.prof
                  inner join Grade g on e.id = g.enroll
	group by sbj.id
    order by count(*) desc, avg((g.midterm + g.finalterm) / 2) desc, avg(pr.likecnt) desc
;


select count(distinct ee.student) from Enroll ee ;

select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
       (count(*)) as stu_cnt, (avg((g.midterm + g.finalterm) / 2)) as avg_score, 
       (avg(pr.likecnt))  prof_likecnt,
       ( (count(*)/(select count(distinct ee.student) from Enroll ee) * 50) + 
         (avg((g.midterm + g.finalterm) / 200) * 30) +
		(avg(pr.likecnt) * 0.2)) estimation
	from Enroll e inner join Subject sbj on sbj.id = e.subject
				  inner join Prof pr on pr.id = sbj.prof
                  inner join Grade g on e.id = g.enroll
	group by sbj.id
    order by estimation desc limit 3
;


delimiter //
create procedure sp_popular_prof()
        begin
			select sbj.id as sbj_id, max(sbj.name) as sbj_name, max(pr.name) as prof_name, 
				   count(*) as stu_cnt, avg((g.midterm + g.finalterm) / 2) as avg_score, avg(pr.likecnt) prof_likecnt
				from Enroll e inner join Subject sbj on sbj.id = e.subject
							  inner join Prof pr on pr.id = sbj.prof
							  inner join Grade g on e.id = g.enroll
				group by sbj.id
				order by count(*) desc, avg((g.midterm + g.finalterm) / 2) desc, avg(pr.likecnt) desc;
            
        end //
delimiter ;


call sp_club_memberinfo2('요트부');


-- 과목명을 입력받아, 성적의 분포를 Stem-and-Leaf display로 표현하는 프로시저를 작성하시오.
-- 결과 화면
-- 5 | 1257
-- 6 | 359
-- 7 | 45578
select * from v_grade_enroll;


delimiter //
create procedure sp_grade_stem_leaf(arg_subject_name varchar(31))
	begin 
		declare _isdone boolean default false;
        declare _avr tinyint;
        declare _stem tinyint;
        declare _leaf tinyint;
        
		declare cur_avrs cursor for
			select avr
				from v_grade_enroll
                where subject = (select id from Subject where name = arg_subject_name)
                order by avr;
		declare continue handler
			for not found set _isdone := True;
            
		drop table if exists t_grade;
		create temporary table t_grade(
			stem tinyint default 0,
            leaf varchar(1024) default '',
            cnt smallint default 0,
            primary key(stem)
            );
            
		open cur_avrs;
			loop1 : loop
				fetch cur_avrs into _avr;
				
                set _stem = floor(_avr / 10);
                set _leaf = mod(_avr,10);
                
                if exists(select * from t_grade where stem = _stem) 
					then update t_grade set leaf = concat(leaf, _leaf),
							cnt = cnt + 1
							where stem = _stem;
					
				else
					insert into t_grade(stem, leaf, cnt) value(_stem, _leaf, 1);
                    
                end if;
                
                if _isdone then
					leave loop1;
				end if;
                
            end loop loop1;
        close cur_avrs;
		select * from t_grade;
    end //
delimiter ;

select * from t_grade;
select * from v_grade_enroll;
call sp_grade_stem_leaf('역사');


select * from v_grade_enroll order by subject, avr desc;

select instr('123,456,789', ',');



