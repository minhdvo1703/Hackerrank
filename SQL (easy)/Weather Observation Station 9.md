# Weather Observation Station 9

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

## Input Format

The STATION table is described as follows:

|  Field | Type |
|-------|-----|
| ID  | NUMBER |
| CITY | VARCHAR2(21)   |
| STATE| VARCHAR2(2)  |
| LAT_N |  NUMBER |
| LONG_W | NUMBER |

#### Solution (MySQL)
```sql
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT IN 
(SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR 
CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%');
```
