
start transaction;

select * from report1;
select * from t_report1;

select sbj_name, sum(avg_score) sbj_total_score, count(*) total_stu
  from t_report1
	   group by sbj_name;

select *, (sub_sbj.sbj_total_score / sub_sbj.total_stu) sbj_avg
  from(
select sbj_name, count(*) total_stu, sum(avg_score) sbj_total_score
  from t_report1
	    group by sbj_name
) sub_sbj
;

