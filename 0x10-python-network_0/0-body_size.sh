#!/usr/bin/bash
# Displays size of the body of response

# path=$1

curl -sI  "$1" | awk '/Content-Length/{print $2}'
