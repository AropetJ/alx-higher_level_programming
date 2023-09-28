#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s -w "\n%{http_code}" "$1" | awk 'END{if($1 == "200") print $0}' RS='\n\n'
