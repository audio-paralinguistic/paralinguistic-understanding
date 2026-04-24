#!/bin/bash
# Start a simple static file server for the ParA-LLM project page.
if [ ! -f "index.html" ]; then
  echo "Run this script from the my-paper-website directory."
  exit 1
fi
echo "http://localhost:8000  (python3 -m http.server 8000)"
python3 -m http.server 8000
