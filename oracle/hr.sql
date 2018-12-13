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


-- 1������) �μ��� ������
select emp.department_id, max(dept.department_name) department_name, count(distinct emp.employee_id) emp_cnt
  from Employees emp inner join Departments dept on emp.department_id = dept.department_id
  group by emp.department_id
  order by emp_cnt desc
  ;

-- 2������) �μ��� ��� �޿�(salary)
select max(dept.department_name), round(avg(emp.salary), -1) as avg_salary
  from Employees emp inner join Departments dept on emp.department_id = dept.department_id
  group by emp.department_id
  order by avg_salary desc
  ;

-- 3������) ��å�� ��� �޿�
select max(emp.job_id), round(avg(emp.salary), 1) as avg_salary
  from Employees emp inner join Jobs jbs on emp.job_id = jbs.job_id
  group by emp.job_id
  ;


-- 4������) �ڽ��� �Ŵ������� �� ���� �޿��� �޴� ��� ��� *********************
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
  



-- 5������) job title�� sales represntative�� ���� �߿���, �޿��� 9,000 ~ 10,000�� �������� �̸��� �޿��� ����Ͻÿ�. **************
select * from Employees;
select * from Jobs;
select (first_name || ' ' || last_name) name, salary
  from Employees
  where job_id = 'SA_REP' and salary between 9000 and 10000
  ;
select e.first_name  "����" , e.salary "�����޿�", es.first_name "�Ŵ��� �̸�" , es.salary "�Ŵ��� �޿�" ,
(e.first_name || '_' || e.last_name) as "����Ǯ����"
from Employees e inner join Employees es on e.manager_id = es.employee_id where e.salary > es.salary ;

select (e.first_name || '_' || e.last_name) as "���� �̸�" , e.salary "�޿�"
from Employees e  where e.job_id = 'SA_REP' and e.salary between 9000 and 10000 order by salary desc;

select concat(concat(e.first_name, ' '), e.last_name) as "���� �̸�" , e.salary "�޿�"
from Employees e  where e.job_id = 'SA_REP' and e.salary between 9000 and 10000 order by salary desc;


-- 6������) �� ���޺��� �޿��� ������ ���ϰ��� �Ѵ�.�޿� ������ ���� ���� ���޼����� �޿� ������ ����Ͻÿ�. (��, �޿������� 30,000 �̻��� ���޸� ����� ��)

select *
from
(select  sum(salary)"���޺� �޿� ����"
from employees e inner join Jobs j on e.job_id = j.job_id group by e.Job_id  order by sum(salary) desc) sub
where sub."���޺� �޿� ����" > 30000;


select max(j.job_title), sum(e.salary)
  from Employees e inner join Jobs j on e.job_id = j.job_id
  group by j.job_id
  having sum(e.salary) >= 30000
  order by sum(e.salary) desc
  ;




-- 7������) �� ���ú� ��� ����(�޿�)�� ���������� ���� 3�� ���ø� ����Ͻÿ�.
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



-- 8������) ��å(Job Title)�� Sales Manager�� ������� �Ի�⵵(hire_date)�� ��� �޿��� ����Ͻÿ�. (��� �� �⵵�� �������� �������� �����Ͻÿ�.)
select *
  from Employees;

select concat('20', min(to_char(e.hire_date, 'YY'))) year, avg(e.salary) avg_salary
  from Employees e inner join Jobs j on e.job_id = j.job_id
  where j.job_title = 'Sales Manager'
  group by to_char(e.hire_date, 'YY')
  order by to_char(e.hire_date, 'YY')
  ;

/* 9������) �� ����(city)�� �ִ� ��� �μ� �������� ��ձ޿��� ��ȸ�ϰ��� �Ѵ�. 
	��ձ޿��� ���� ���� ���ú��� ���ø�(city)�� ��տ���, �ش� ������ �������� 
	����Ͻÿ�. 
	��, ���ÿ� �ٹ��ϴ� ������ 10�� �̻��� ���� �����ϰ� ��ȸ�Ͻÿ�. */


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



/* 10������) Public  Accountant���� ��å(job_title)���� ���ſ� �ٹ��� ���� �ִ� ���
	����� ����� �̸��� ����Ͻÿ�. 
	(���� ��Public Accountant���� ��å(job_title)���� �ٹ��ϴ� ����� ��� ����
	 �ʴ´�) */

select * from Jobs;

select e.employee_id, (e.first_name || ' ' || e.last_name) name
  from Job_history jh inner join Jobs j on jh.job_id = j.job_id
                      inner join Employees e on jh.employee_id = e.employee_id
  where j.job_title = 'Public Accountant' and e.job_id <> j.job_id;
  

/* 11)	2007�⿡ �Ի�(hire_date)�� �������� ���(employee_id),
	�̸�(first_name), ��(last_name), 
	�μ���(department_name)�� ��ȸ�մϴ�.  
	�̶�, �μ��� ��ġ���� ���� ������ ���, ��<Not Assigned>���� ����Ͻÿ�.*/
desc departments;

select concat('20', to_char(e.hire_date, 'YY')) year, e.employee_id, e.first_name, e.last_name, 
       nvl(department_name, '<Not Assigned>') department_name
  from Employees e left outer join Departments d on d.department_id = e.department_id
  where to_char(e.hire_date, 'YY') = '07'
  ;
  



/* 12)	�μ����� ���� ���� �޿��� �ް� �ִ� ������ �̸�, �μ��̸�, �޿��� ����Ͻÿ�. 
	�̸��� last_name�� ����ϸ�, �μ��̸����� �������� �����ϰ�, 
	�μ��� ���� ��� �̸��� ���� ���� �������� �����Ͽ� ����մϴ�. */
    
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



/* 13������) EMPLOYEES ���̺��� �޿��� ���� �޴� ������� ��ȸ���� ��
   6��°���� 10 ��°���� 5���� last_name, first_name, salary�� ��ȸ�ϴ�
   sql������ �ۼ��Ͻÿ�. */
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


   

/* 14������) ��Sales�� �μ��� ���� ������ �̸�(first_name), �޿�(salary), 
	�μ��̸�(department_name)�� ��ȸ�Ͻÿ�. 
	��, �޿��� 100�� �μ��� ��պ��� ���� �޴� ���� ������ ��µǾ�� �Ѵ�. */

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


/* 15������) �μ��� �Ի���� �������� ����Ͻÿ�. 
	��, �������� 5�� �̻��� �μ��� ��µǾ�� �ϸ� ��°���� �μ��̸� ������ �Ѵ�. */
    
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






/* 16������) Ŀ�̼�(commission_pct)�� ���� ���� ���� ���� 4���� 
	�μ���(department_name), ������ (first_name), �޿�(salary),
	Ŀ�̼�(commission_pct) ������ ��ȸ�Ͻÿ�. 
	��°���� Ŀ�̼��� ���� �޴� ������ ����ϵ� ������ Ŀ�̼ǿ� ���ؼ��� �޿��� ����
 	������ ���� ��� �ǰ� �Ѵ�. */
    
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