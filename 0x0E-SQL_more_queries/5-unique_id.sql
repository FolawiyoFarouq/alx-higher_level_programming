-- creates the table unique_id on your MySQL server.
-- F A R O U Q
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
  );
