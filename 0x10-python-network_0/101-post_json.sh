#!/bin/bash
# Sends a JSON post request passed as argumen
curl -s -H "$1" "Content-Type: application/json" -d @"$2"
