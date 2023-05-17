-- F A R O U Q
-- lists the number of records with the same score in the table second_table of the database named hbtn_0c_0 in your MySQL server.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
