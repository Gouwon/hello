show table status;

select * from Student;

select count(*);

truncate table dooodb.Student;

CREATE TABLE `Student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `addr` varchar(30) NOT NULL,
  `birth` date NOT NULL,
  `tel` varchar(15) NOT NULL,
  `email` varchar(31) NOT NULL,
  `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '등록일시',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

select birth, replace(substring(birth, 3)m '-', '') from Student;
update Student set birth = replace(substring(birth, 3), '-', '')
	where id> 0 and birth is not null;
alter table dooodb.Student change column birth birth varchar(11) not null;
alter table dooodb.Student change column birth birth varchar(6) not null;

select * from Test;

insert into Test(name) value('김이수');
insert into Test(name) values(select name from Student where id > 23 and id < 30);
	
insert into Test(name) select name from Student where id > 10 and id < 20;

delete from Test where id >= 10;

select * from Student;
select * from Student where name like '김__';
select * from Student where id not in (10, 20, 30);
select * from Student where id = 10 or id = 20 or id = 30;
select * from Student where id >= 15 and id <= 20;
select * from Student where id between 10 and 15;
select * from Student where id in (select * from Student where id between 10 and 990) ;
select * from Student where name between '바' and '빟';

select * from Student where email between 'a' and 'b';

select * from Student where substring(email, 1) = 'a';
select * from Student where email having 'a%';


select * from Student where email like 'a%' and tel like '010-9%';


select distinct(birth) from Student where birth='700601';
select count(distinct birth) from Student where birth = '700601';

select * from Student order by rand();

select * from Student limit 100;


select * from Student order by addr, birth desc limit 10, 5;

select * from Student where addr like '경%' order by birth desc limit 10, 5;


select addr, count(*) as cnt, avg(id) from Student group by addr order by cnt desc;
select addr, count(*) as cnt, avg(id) from Student group by addr order by cnt desc;


