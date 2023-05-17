-- F A R O U Q
-- displays the top 3 of cities temp during July and August ordered by temp DESC
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

-- End of the task
