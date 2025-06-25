-- Count number of records per score and order descending by count
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;