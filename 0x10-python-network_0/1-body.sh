#!/bin/bash
#Displays ony body status code '-L'->follows redirects '-sf'->silences errors
curl -Lsf "$1"
