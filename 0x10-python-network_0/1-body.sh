#!/bin/bash
# Displays ony body status code
curl -s -w "%{http_code}\n" -o /dev/null "$1"
