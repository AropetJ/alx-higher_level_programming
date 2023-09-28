#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -sX GET "$1" -L 200
