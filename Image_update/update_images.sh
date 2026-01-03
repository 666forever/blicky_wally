#!/bin/bash

echo ""
echo "========================================"
echo " Blicky Wally - Image Data Generator"
echo "========================================"
echo ""

# Check if Node.js is installed, if not try Python
if command -v node &> /dev/null; then
    node generate-image-data.js
elif command -v python3 &> /dev/null; then
    python3 generate-image-data.py
elif command -v python &> /dev/null; then
    python generate-image-data.py
else
    echo "❌ Error: Neither Node.js nor Python found!"
    echo "Please install Node.js or Python to use this script."
    exit 1
fi

echo ""
read -p "Press Enter to continue..."
