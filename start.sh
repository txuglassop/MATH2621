#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: ./start.sh [line|circle]"
    exit 1
fi

# Determine which script to run based on the argument
if [ "$1" == "l" ]; then
    python3 plot_line.py
elif [ "$1" == "c" ]; then
    python3 plot_circles.py
else
    echo "Invalid argument. Use 'l' for 'line' or 'c' for 'circle'."
    exit 1
fi
