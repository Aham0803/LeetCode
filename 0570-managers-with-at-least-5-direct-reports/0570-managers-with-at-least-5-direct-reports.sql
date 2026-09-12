-- # Write your MySQL query statement below
-- -- select
-- -- e.name
-- -- from Employee as e
-- -- join Employee as m
-- -- on e.id = m.managerId
-- -- group by e.id 
-- -- Having count(*)>=5;

select
name
from Employee 
where id in (
    select managerID 
    from Employee 
    where managerId is not null
    group by managerId
    having count(*) >= 5
)


















