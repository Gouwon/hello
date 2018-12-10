
start transaction;

select * from report1;
select * from t_report1;
desc t_report1;


select sbj_name, sum(avg_score) sbj_total_score, 
	   (select stu_name from t_report1 where max(avg_score) limit 1) stus_name,
        count(*) as total_stu
  from t_report1
		where if(stu.name
	   group by sbj_name
	   
       ;
       
       
select addr, group_concat(name) as 'student names' from Student group by addr;

select sbj_name, group_concat(stu_name) as 'student names'
  from t_report1
  group by sbj_name;
  
select group_concat(stu_name) as 'student names'
  from t_report1
  group by sbj_name;
 

select *, (sub_sbj.sbj_total_score / sub_sbj.total_stu) sbj_avg
  from(
select sbj_name, count(*) total_stu, sum(avg_score) sbj_total_score
  from t_report1
	    group by sbj_name
) sub_sbj
;







