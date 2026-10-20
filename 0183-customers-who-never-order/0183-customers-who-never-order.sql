# Write your MySQL query statement below
-- select 
-- c.name as Customers
-- from Customers as c
-- where c.id not in (
--     select 
--     o.customerId
--     from Orders as o
-- )

# Write your MySQL query statement below
-- select
-- c.name as Customers
-- from Customers as c
-- left join Orders as o
-- on c.id = o.customerId
-- where c.id not in (
--     select
--     customerId
--     from Orders 
-- )


SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id=o.customerId
-- WHERE o.customerId IS NULL;
where o.id is null








