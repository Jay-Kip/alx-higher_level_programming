#!/bin/bash
# Sends a JSON post request passed as argumen
curl -s -X POST -F "file=@$2" "$1"
