-- # Write your MySQL query statement below
-- with damount as (
--     select visited_on,amount,sum(amount) as daily_amount
--     from customer
--     group by visited_on
-- ),
--  cte as (
--     select 
--     visited_on,
--     dense_rank() over(order by visited_on) as rnk,
--     sum(daily_amount) over(order by visited_on rows between 6 preceding and current row) as amount,
--     round(avg(daily_amount) over( order by visited_on rows between 6 preceding and current row),2) as average_amount 
--     from damount
-- )
-- select
-- visited_on,
-- amount,
-- average_amount
-- from cte
-- where rnk >= 7
-- group by visited_on
-- order by visited_on


SELECT
    c1.visited_on,
    SUM(c2.daily_amount) AS amount,
    ROUND(AVG(c2.daily_amount), 2) AS average_amount
FROM (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
) c1
JOIN (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
) c2
    ON c2.visited_on BETWEEN
       DATE_SUB(c1.visited_on, INTERVAL 6 DAY)
       AND c1.visited_on
GROUP BY c1.visited_on
HAVING COUNT(*) = 7
ORDER BY c1.visited_on;
