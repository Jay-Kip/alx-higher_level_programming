#!/bin/bash
# Displays size of the body of response
curl -s -w "%{size_download}\n" -o /dev/null "$1"
