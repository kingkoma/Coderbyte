'''
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
'''

# Solution 1
SELECT Email 
from Person 
GROUP BY Email 
HAVING Count(Email)>1
;

# Solution 2
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;
