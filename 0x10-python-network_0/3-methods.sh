#!/bin/bash
# Displays HTTP method the server will accept
curl -sI -X HEAD -s "$1" | awk "/Allow:/ {print $2}"
