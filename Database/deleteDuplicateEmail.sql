# Write your MySQL query statement below
delete 
from Person
where 
Id not in (Select Id from
           (Select min(id) as Id
            From person
            Group by email
           )p
           );
