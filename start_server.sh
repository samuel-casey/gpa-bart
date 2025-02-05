#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required but not installed. Please install Python3 and try again."
    exit 1
fi

# Start the server
python3 server.py 