#!/bin/bash

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.cargo/env"

# Create the virtual environment and install packages
uv venv
uv pip install -r requirements.txt
