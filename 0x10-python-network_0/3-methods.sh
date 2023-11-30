#!/bin/bash
# Displays HTTP method the server will accept
curl -sX OPTIONS -i "$1"
