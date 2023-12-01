#!/bin/bash
# description
curl -sLX PUT 0:5000/catch_me "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
