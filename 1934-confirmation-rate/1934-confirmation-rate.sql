-- # Write your MySQL query statement below
-- select
-- user_id,
-- round(ifnull(avg(is_confirmed) /count(is_action) , 0) ,  2) as confirmation_rate
-- from (
--     select
--     s.user_id,
--     case when c.action = 'confirmed' then 1 else 0  end as  is_confirmed,
--     c.action as is_action
--     from Signups as s
--     left join Confirmations as c
--     on s.user_id = c.user_id
-- )t
--  group by user_id

-- SELECT 
--     s.user_id,
--     ROUND(IFNULL(AVG(c.action = 'confirmed'), 0), 2) AS confirmation_rate
-- FROM Signups s
-- LEFT JOIN Confirmations c 
--     ON s.user_id = c.user_id
-- GROUP BY s.user_id;

-- select
-- user_id,
-- round(ifnull(avg(is_confirmed), 0) ,  2) as confirmation_rate
-- from (
--     select
--     s.user_id,
--     case when c.action = 'confirmed' then 1 else 0  end as  is_confirmed
--     from Signups as s
--     left join Confirmations as c
--     on s.user_id = c.user_id
-- )t
--  group by user_id

SELECT 
    s.user_id,
    ROUND(
        IFNULL(
            avg(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END), 
            0
        ), 
        2
    ) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c 
    ON s.user_id = c.user_id
GROUP BY s.user_id;