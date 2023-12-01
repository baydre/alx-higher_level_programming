#!/bin/bash
# Script that sends a JSON post to the passed URL and displays the body of response
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
