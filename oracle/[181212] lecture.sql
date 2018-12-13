select sysdate, CURRENT_TIMESTAMP from dual;

create table Test(
  ts timestamp, -- default timestamp
  tsz timestamp with time zone,
  ts0 timestamp(0) -- GMT �������� ���ʿ��� ���� ���� ����.
);

insert into Test(ts, tsz, ts0)
  values(SYSDATE, SYSDATE, SYSDATE);
  
select ts, tsz, ts0, lengthb(ts), lengthb(tsz), lengthb(ts0) from Test;

select to_char(sysdate, 'YYYY-MM-DD HH:MI:SS') from dual; -- GMT �ð����� ��µ�
select to_char(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH:MI:SS') from dual; -- �����ð����� ��µ�

select to_char(CURRENT_TIMESTAMP, 'WW W DDD RM DY AM TZD')from dual; -- 1���� ���°��,???,����,����/����,Ÿ����

select to_char(tsz, 'J'), to_char(tsz, 'YY-MM-DD HH24:MI:SS') from Test; -- Julian Day (�����콺 ����, BC4713�� 1�� 1�Ϻ����� �ϼ�)

select lpad('abc', 5, '0') from dual;

select replace('��ǿ�', '�ǿ�', '00') from dual;

select power(2, 3), sqrt(2) from dual;

select manager_id, NVL(manager_id, '12'), uid, user
  from Employees;

select decode(employee_id, 100, 'one', 200, 'two' , 150, 'ten', 'none') from Employees;
select (case when employee_id < 200 then 'one' else 'nnnnn' end) from Employees;

select to_date('2018-12-25 12:22:44', 'YYYY-MM-DD HH24:MI:SS') from dual; -- �ð����� �൵ ��¥�� �̾ƿ´�.

select salary, count(*) cnt from Employees group by salary order by cnt desc;
select stats_mode(salary) from Employees;   -- �ֺ�

select Employees.*, rowid, rownum from Employees where rownum < 10 order by salary desc; -- limit ���




