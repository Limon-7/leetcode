
-- Write your PostgreSQL query statement below
Select e.name as Employee from Employee as e
join Employee se on e.managerId=se.Id
where e.salary>se.salary

Employee:
| id | name  | salary | managerId |
| -- | ----- | ------ | --------- |
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | null      |
| 4  | Max   | 90000  | null      |

Output:
| employee |
| -------- |
| Joe      |