#!/bin/bash
#F A R O U Q
# Send a POST request with the data "user_id=98" to the target URL
curl -s -X PUT -d "user_id=98" "http://0.0.0.0:5000/catch_me" -o /dev/null

