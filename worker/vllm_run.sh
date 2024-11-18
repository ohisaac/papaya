#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

# Activate virtual environment
source myenv/bin/activate

# Install vLLM if not installed
pip install vllm

# Run vLLM server with Qwen2-VL-2B-Instruct model
vllm serve Qwen/Qwen2-VL-2B-Instruct \
    --dtype auto \
    --api-key token-abc123 \
    --port 8000
