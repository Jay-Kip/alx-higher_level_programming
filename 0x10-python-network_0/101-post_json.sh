#!/bin/bash
# Sends a JSON post request passed as argumen
curl -s -H "Content-Type: application/json" -d @"$2"  "$1"
