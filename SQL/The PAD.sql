SELECT CONCAT(NAME,'(',SUBSTR(occupation,1,1),')') FROM OCCUPATIONS ORDER BY NAME ASC;
SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation),'s.') FROM OCCUPATIONS GROUP BY occupation ORDER BY COUNT(occupation)
