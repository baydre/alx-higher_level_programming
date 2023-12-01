#!/bin/bash
# script that sends a GET request to passed URL and displays body of response
curl -sX GET "$1" -H "X-School-User-Id:98"
