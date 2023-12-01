#!/bin/bash
# script that sends a POST request to the URL passed and displays body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
