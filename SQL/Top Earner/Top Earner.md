# Top Earners


We define an employee's total earnings to be their monthly SALARY x MONTHS worked, and the maximum total earnings to be the maximum total earnings 
for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees 
who have maximum total earnings. Then print these values as  space-separated integers.

## Input Format

The EMPLOYEE table table containing employee data for a company is described as follows:

|  Column | Type |
|-------|-----|
| employee_id    | INTEGER |
| name  | STRINGS  |
| months| INTEGER  |
| salary| INTEGER  |

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, 
and salary is their monthly salary.

## Sample Input

| employee_id | name | month | salary |
|-----------|-----|------|------|
|  12228  | Rose |   15   |  1968  |
|  33645  | Angela |   1   |  3433  |
|  45692  | Frank |   17   |  1608  |
|  56118  | Patrick |   7   |  1345  |
|  59725  | Lisa |   11   |  2330  |
|  74197  | Kimberly |   16   |  4312  |
|  78454  | Bonnie |   8   |  1771  |
|  83565  | Michael |   6   |  2017  |
|  98607  | Todd |   5   |  3396  |
|  99989  | Joe |   9   |  3573  |

## Sample Output
```
69952 1
```

## Explanation
The maximum earnings value is 69952. The only employee with earnings 69952 is Kimberly, so we print the maximum earnings value (69952) 
and a count of the number of employees who have earned 69952 (which is 1) as two space-separated values.

