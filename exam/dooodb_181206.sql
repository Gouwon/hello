-- 2. 수강내역(Enroll)에 의미 있는 데이터 입력하기

-- 1000명이 1과목씩 수강 (1)
insert into Enroll(student, subject)
select st.id, (select id from Subject order by rand() limit 1) from Student st;

-- Mapping Table인 Enroll에 들어가는 학생과 과목을 하나의 unique index로 묶어줘 있어야 한다.
ALTER TABLE `dooodb`.`Enroll` 
ADD UNIQUE INDEX `uk_enroll` (`subject` ASC, `student` ASC);
;

-- 500명이 1과목을 추가 수강 (2)
insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;
 
 -- 참고. 학생들 중 n개의 과목을 수강하는 학생을 만들고 싶다면, (2)를 n번 실행.