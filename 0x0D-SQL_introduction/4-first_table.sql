#!/bin/bash

DB_NAME="$1"
mysql -h localhost -u root -p "$DB_NAME" <<EOF
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
EOF

