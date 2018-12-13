select * from v$database;

select * from v$instance;

select userenv('sid') from dual;

create table Prof(
  id number(5) not null,
  name varchar2(31) not null,
  likecnt number(5) default 0 not null,
  constraint pk_id primary key (id)
);

comment on column Prof.name is '������';
comment on column Prof.likecnt is '���ƿ��';


create table Subject(
  id number(5) not null primary key,
  name varchar2(31) not null,
  prof number(5),
  classroom number(5),
  constraint fk_prof foreign key (prof) references Prof(id),
  constraint fk_classroom foreign key (classroom) references Classroom(id)
);

create table Classroom( 
  id number(5) not null primary key,
  name varchar2(31)
);


select * from Countries;
select * from Regions;
select * from Locations;
select * from Departments;
select * from Employees;
select * from Jobs;
select * from Jobs_history;


-- 1번문제) 부서별 직원수

select emp.department_id, max(dept.department_name) department_name, count(distinct emp.employee_id) emp_cnt
  from Employees emp inner join Departments dept on emp.department_id = dept.department_id
  group by emp.department_id
  order by emp_cnt desc
  ;

-- 2번문제) 부서별 평균 급여(salary)

select max(dept.department_name), round(avg(emp.salary), -1) as avg_salary
  from Employees emp inner join Departments dept on emp.department_id = dept.department_id
  group by emp.department_id
  order by avg_salary desc
  ;

-- 3번문제) 직책별 평균 급여 (평균급여 기준 상위 7개 직책만) 

select max(emp.job_id), round(avg(emp.salary), 1) as avg_salary
  from Employees emp inner join Jobs jbs on emp.job_id = jbs.job_id
  group by emp.job_id
  ;


-- 4번문제) 자신의 매니저 보다 더 많은 급여를 받는 사람 목록
select * from Employees;

select employee_id, manager_id
  from Employees
  order by manager_id;
  
select sub.*
from(
select e.employee_id, e.salary, e.manager_id, 
      (select salary from Employees where employee_id = e.manager_id) mgr_sal
  from Employees e
  ) sub
  where sub.salary > sub.mgr_sal
  ;
  
 
  select e.*
    from Employees e, (select salary from Employees where employee_id = e.manager_id) ee
    where e.salary > mgr_sal.salary
    ;
 
  
  select e.*
   from Employees e inner join Employees es on e.manager_id = es.employee_id
   where e.salary > es.salary; -- self join
  



/* 5번문제) Job title이 Sales Representative인 직원 중에서,
급여가 9,000 ~ 10,000 인 직원들의 이름과 급여를 출력하시오. */
select * from Employees;
select * from Jobs;
select (first_name || ' ' || last_name) name, salary
  from Employees
  where job_id = 'SA_REP' and salary between 9000 and 10000
  ;

select e.first_name  "직원" , e.salary "직원급여", es.first_name "매니저 이름" , es.salary "매니저 급여" ,
(e.first_name || '_' || e.last_name) as "직원풀네임"
from Employees e inner join Employees es on e.manager_id = es.employee_id where e.salary > es.salary ;

select (e.first_name || '_' || e.last_name) as "직원 이름" , e.salary "급여"
from Employees e  where e.job_id = 'SA_REP' and e.salary between 9000 and 10000 order by salary desc;


/* 6번문제) 각 직급별로 급여의 총합을 구하고자 한다.
급여 총합이 가장 높은 직급순으로 급여 총합을 출력하시오.
(단, 급여총합이 30,000 이상인 직급만 출력할 것) */

select *
from
(select  sum(salary)"직급별 급여 총합"
from employees e inner join Jobs j on e.job_id = j.job_id group by e.Job_id  order by sum(salary) desc) sub
where sub."직급별 급여 총합" > 30000;


select max(j.job_title), sum(e.salary)
  from Employees e inner join Jobs j on e.job_id = j.job_id
  group by j.job_id
  having sum(e.salary) >= 30000
  order by sum(e.salary) desc
  ;

=============================================================
select max(j.job_title) job_title, sum(e.salary) sum_sal
  from Employees e inner join Jobs j on e.job_id = j.job_id
  group by e.job_id
  having sum(e.salary) >= 30000
  order by sum(e.salary) desc
;

select sub.*
  from 
  (
    select max(j.job_title) job_title, sum(e.salary) sum_sal
      from Employees e inner join Jobs j on e.job_id = j.job_id
      group by e.job_id
   ) sub
   where sub.sum_sal >= 30000
   order by sub.sum_sal desc
   ;

=======================================================================

-- 7번문제) 각 도시별 평균 연봉(급여)가 높은순으로 상위 3개 도시를 출력하시오.
select * from locations;

select rownum, sub.*
  from
(
select  max(l.city) city, round(avg(salary), -1) avg_salary
  from Employees e inner join Departments d on e.department_id = d.department_id
                   inner join locations l on l.location_id = d.location_id
       group by l.location_id
       order by avg_salary desc
) sub
where rownum < 4
       ;

=======================================================================
select sub.*
    from
    (
        select l.city, avg(e.salary) avg_sal
            from Employees e inner join Departments d on d.department_id = e.department_id
                             inner join Locations l on l.location_id = d.location_id
            group by l.city
            order by avg_sal
    ) sub
where rownum <= 3
;

=======================================================================

/* 8번문제) 직책(Job Title)이 'Sales Manager'인 사원들의 입사년도(hire_date)별 평균 급여를 출력하시오. 
	출력 시 년도를 기준으로 오름차순 정렬하시오. */
select *
  from Employees;

select concat('20', min(to_char(e.hire_date, 'YY'))) year, avg(e.salary) avg_salary
  from Employees e inner join Jobs j on e.job_id = j.job_id
  where j.job_title = 'Sales Manager'
  group by to_char(e.hire_date, 'YY')
  order by to_char(e.hire_date, 'YY')
  ;

=======================================================================

select to_char(e.hire_date, 'YYYY') hire_year, round(avg(e.salary)) avg_sal
    from Employees e inner join Jobs j on j.job_id = e.job_id
    where j.job_title = 'Sales Manager'
    group by to_char(e.hire_date, 'YYYY')
    order by to_char(e.hire_date, 'YYYY')
;



/* 9번문제) 각 도시(city)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다. 
	평균급여가 가장 낮은 도시부터 도시명(city)과 평균연봉, 해당 도시의 직원수를 
	출력하시오. 
	단, 도시에 근무하는 직원이 10명 이상인 곳은 제외하고 조회하시오.. */


select sub.city, sub.avg_salary, sub.cnt
 from
(
select max(l.city) city, avg(e.salary) avg_salary, count(*) cnt
  from Employees e inner join Departments d on e.department_id = d.department_id
                   inner join Locations l on l.location_id = d.location_id
        group by l.location_id
        order by avg_salary
) sub
where sub.cnt < 10
  ;



/* 10번문제) ‘Public Accountant’의 직책(job_title)으로 과거에 근무한 적이 있는 모든
	사원의 사번과 이름을 출력하시오. 
	(현재 ‘Public Accountant’의 직책(job_title)으로 근무하는 사원은 고려 하지
	 않는다)) */

select * from Jobs;

select e.employee_id, (e.first_name || ' ' || e.last_name) name
  from Job_history jh inner join Jobs j on jh.job_id = j.job_id
                      inner join Employees e on jh.employee_id = e.employee_id
  where j.job_title = 'Public Accountant' and e.job_id <> j.job_id;
  

/* 11번문제)	2007년에 입사(hire_date)한 직원들의 사번(employee_id),
	이름(first_name), 성(last_name), 
	부서명(department_name)을 조회합니다.  
	이때, 부서에 배치되지 않은 직원의 경우, ‘<Not Assigned>’로 출력하시오.�.*/
desc departments;

select concat('20', to_char(e.hire_date, 'YY')) year, e.employee_id, e.first_name, e.last_name, 
       nvl(department_name, '<Not Assigned>') department_name
  from Employees e left outer join Departments d on d.department_id = e.department_id
  where to_char(e.hire_date, 'YY') = '07'
  ;
  



/* 12번문제)	부서별로 가장 적은 급여를 받고 있는 직원의 이름, 부서이름, 급여를 출력하시오. 
	이름은 last_name만 출력하며, 부서이름으로 오름차순 정렬하고, 
	부서가 같은 경우 이름을 기준 으로 오름차순 정렬하여 출력합니다.. */
    
select last_name, sub.department_name, sub.salary  
from
Employees e,
(
select d.department_id, max(d.department_name) department_name, min(e.salary) salary
  from Employees e inner join Departments d on d.department_id = e.department_id
  group by d.department_id
) sub  
where e.salary = sub.salary
order by sub.department_name, e.last_name
;



/* 13번문제) EMPLOYEES 테이블에서 급여를 많이 받는 순서대로 조회했을 때
   6번째부터 10 번째까지 직원의 last_name, first_name, salary를 조회하는
   sql문장을 작성하시오. */
select sub1.last_name, sub1.first_name, sub1.salary
from 
    (
    select rownum rn, sub.last_name last_name, sub.first_name first_name, sub.salary salary
    from  
        (
        select e.last_name last_name, e.first_name first_name, e.salary salary
          from Employees e
          order by salary desc
        )sub
    )sub1
where sub1.rn between 6 and 10
;

select sub.last_name, sub.first_name, sub.salary
from
(
select e.last_name last_name, e.first_name first_name, e.salary salary,
      rank() over(order by salary desc) ranking
    from Employees e
) sub
where sub.ranking between 6 and 10
;


   

/* 14번문제) ‘Sales’ 부서에 속한 직원의 이름(first_name), 급여(salary), 
	부서이름(department_name)을 조회하시오. 
	단, 급여는 100번 부서의 평균보다 적게 받는 직원 정보만 출력되어야 한다. */

select *
  from Employees e inner join Departments d on d.department_id = e.department_id
  where d.department_name = 'Sales'
        and e.salary < (
                select round(avg(ee.salary), 0) salary
                  from Employees ee
                  where ee.department_id = 100
                  group by ee.department_id
        );
        

select round(avg(ee.salary), -1) salary
                  from Employees ee
                  where ee.department_id = 100
                  group by ee.department_id;


/* 15번문제) 부서별 입사월별 직원수를 출력하시오. 
	단, 직원수가 5명 이상인 부서만 출력되어야 하며 출력결과는 부서이름 순으로 한다.Ѵ�. */
    
select sub.department_name, sub.hire_month, sub.cnt
from
(
select d.department_id department_id, max(d.department_name) department_name, to_char(e.hire_date, 'MM') hire_month, count(*) cnt
  from Employees e inner join Departments d on d.department_id = e.department_id
  group by d.department_id, to_char(e.hire_date, 'MM')
  order by max(d.department_name), to_char(e.hire_date, 'MM')
) sub
where sub.cnt >= 5
;

select max(sub.department_name) department_name, to_char(sub.hire_date, 'MM') hire_month, count(*) cnt
from
(select d.department_id, d.department_name, e.hire_date   from Employees e inner join Departments d on d.department_id = e.department_id) sub,
(
select ee.department_id department_id, count(*) cnt
  from Employees ee
  group by ee.department_id
  having count(*) >= 5
) sub1
where sub.department_id =sub1.department_id
group by sub.department_id, to_char(sub.hire_date, 'MM')
order by  max(sub.department_name), to_char(sub.hire_date, 'MM')
  ;






/* 16번문제) 커미션(commission_pct)을 가장 많이 받은 상위 4명의 
	부서명(department_name), 직원명 (first_name), 급여(salary),
	커미션(commission_pct) 정보를 조회하시오. 
	출력결과는 커미션을 많이 받는 순서로 출력하되 동일한 커미션에 대해서는 급여가 높은
 	직원이 먼저 출력 되게 한다.. */
    
select *
  from Employees;
select sub1.department_name department_name,
       sub1.first_name first_name,
       sub1.salary salary,
       sub1.commission_pct commission_pct
from
(
    select sub.department_name department_name,
           sub.first_name first_name,
           sub.salary salary,
           sub.commission_pct commission_pct,
           rownum rn
        from
        (
            select d.department_name as department_name, 
                   e.first_name as first_name, 
                   e.salary as salary, 
                   e.commission_pct as commission_pct
              from Employees e inner join Departments d on d.department_id = e.department_id
              where e.commission_pct is not null
              order by e.commission_pct desc
         ) sub 
) sub1
where sub1.rn < 5
  ;

select sub.department_name, sub.first_name, sub.salary, sub.commission_pct
from
(
select d.department_name as department_name, 
                   e.first_name as first_name, 
                   e.salary as salary, 
                   e.commission_pct as commission_pct,
                   rank() over ( order by e.commission_pct desc ) ranking
              from Employees e inner join Departments d on d.department_id = e.department_id
              where e.commission_pct is not null
 ) sub
 where ranking < 5
;