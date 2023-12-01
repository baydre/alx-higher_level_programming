#!/bin/bash
# script that displays all HTTP methods the server will accept of URL passed
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
