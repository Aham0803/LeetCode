-- SELECT
--    d.name as Department,
--    e.name as Employee,
--    e.salary as Salary
-- from Employee e
-- join Department as d
-- on e.departmentId = d.id
-- join(
--     select
--         departmentId,
--         max(salary) as max_salary
--     from Employee
--     group by departmentId
-- )m
-- on e.departmentId = m.departmentId
-- And e.salary = m.max_salary;

select
Department,
Employee,
Salary
from(
    select
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    dense_rank() over(partition by e.departmentId order by e.salary desc) as rnk
    from Employee e
    join Department d
        on e.departmentID = d.id
)t
where rnk = 1;