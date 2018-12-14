select * from Test;

insert ignore Test(id, name) values(9, '김상생');

insert ignore Test(name) values('김상생');

select addr, group_concat(name) as 'student names' from Student group by addr;
select addr, concat_ws(',',name) as 'student names' from Student group by addr;
select addr, concat(name) as 'student names' from Student group by addr;

-- 과목을 1row로 나타내기
select group_concat(name) as 'subject_name'
  from Subject;

-- 과목을 1row로 sort로 나타내기 (1) 클러스터 인덱스로 인해서 sort가 안 됨.  
select group_concat(s.name)
  from
  (select name
  from Subject
  order by name) s;

-- 과목을 1row로 sort로 나타내기 (2) 클러스터 인덱스에 안 걸리기 위해서 임시 테이블을 생성.
create temporary table t_table(
	nm varchar(31));

insert into t_table select name
  from Subject
  order by name;

select group_concat(nm) from t_table;

select * from Subject;
show index from Subject;
desc Subject;
  
-- 서울 거주 중인 과목별 성별을 1줄로 나타내기
select sbj.name, stu.name
  from Enroll e inner join Subject sbj on e.subject = sbj.id
				inner join Student stu on e.student = stu.id
  where stu.addr like '서울시%'
  group by sbj.id
  ;
  
