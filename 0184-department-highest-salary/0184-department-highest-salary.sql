SELECT
   d.name as Department,
   e.name as Employee,
   e.salary as Salary
from Employee e
join Department as d
on e.departmentId = d.id
join(
    select
        departmentId,
        max(salary) as max_salary
    from Employee
    group by departmentId
)m
on e.departmentId = m.departmentId
And e.salary = m.max_salary;