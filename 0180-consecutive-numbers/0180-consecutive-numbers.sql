# Write your MySQL query statement below
-- select Distinct
-- l1.num as ConsecutiveNums
-- from Logs as l1
-- join Logs as l2
-- on l1.id = l2.id-1
-- join Logs  as l3
-- on l2.id = l3.id-1
-- where l1.num= l2.num
-- And l2.num = l3.num

select distinct num as ConsecutiveNums
from(
    select
    num ,
    lag(num,1) over(order by id) as prev1,
    lag(num,2) over(order by id) as prev2
    from Logs
)t
where num = prev1
and num = prev2