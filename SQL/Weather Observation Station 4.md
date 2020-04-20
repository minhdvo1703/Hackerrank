# Weather Observation Station 4

Let  be the number of CITY entries in STATION, and let  be the number of distinct CITY names in STATION; 
query the value of  from STATION. In other words, find the difference between the total number of CITY entries 
in the table and the number of distinct CITY entries in the table.

## Input Format

The STATION table is described as follows:

|  Field | Type |
|-------|-----|
| ID  | NUMBER |
| NAME | VARCHAR2(17)   |
| COUNTRY CODE  | VARCHAR2(3)  |
| DISTRICT |  VARCHAR2(20) |
| POPULATION | NUMBER |

#### Solution
```sql
    SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;
```
