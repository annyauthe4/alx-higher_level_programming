#!/usr/bin/bash
# Takes a URL, sends a request to that URL and displays
# the size of the body of the response.
# The size must be displayed in bytes

# Check if the URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and display the response body size in bytes
curl -s -w '%{size_download}\n' -o /dev/null "$1"
