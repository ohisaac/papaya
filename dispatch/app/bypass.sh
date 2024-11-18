#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

# Activate virtual environment
source myenv/bin/activate

# Install requirements if needed
pip install -r requirements.txt

# Run the bypass proxy server
python3 bypass.py
