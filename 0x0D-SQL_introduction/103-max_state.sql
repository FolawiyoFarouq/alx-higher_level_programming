-- F A R O U Q
-- displays the max temprature of each state ordered by statename
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
