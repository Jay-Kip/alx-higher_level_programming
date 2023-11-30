#!/usr/bin/env bash
# Displays size of the body of response

path=$1

curl -s  -w "%{size_download}\n" -o /dev/null path
