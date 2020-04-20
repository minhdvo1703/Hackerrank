# Weather Observation Station 1 

Query a list of CITY and STATE from the STATION table.

## Input Format

The STATION table is described as follows:
|  Field | Type |
|-------|-----|
| ID  | NUMBER |
| NAME | VARCHAR2(17)   |
| COUNTRY CODE  | VARCHAR2(3)  |
| DISTRICT |  VARCHAR2(20) |
| POPULATION | NUMBER |

### Solution
```sql
  SELECT CITY,STATE FROM STATION;
```
