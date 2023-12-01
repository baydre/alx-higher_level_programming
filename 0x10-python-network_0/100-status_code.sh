#!/bin/bash
# Script that sends a request to URL passed and displays status code of response
curl -s "$1" -o /dev/null -w "%{http_code}"
