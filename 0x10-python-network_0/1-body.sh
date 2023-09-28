#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s "$1" | awk 'NR==1 {if ($2 == 200) print}' | sed '1d'
