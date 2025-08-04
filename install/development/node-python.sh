#!/bin/bash

# This script handles the installation of Node.js and Python tooling.

echo "Installing uv (Python package manager)..."
if ! command -v uv &> /dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # The installer script should add uv to the path, but we can ensure it for the current session.
    source "$HOME/.cargo/env"
else
    echo "uv is already installed."
fi

echo "Installing nvm (Node Version Manager)..."
if [ ! -d "$HOME/.config/nvm" ]; then
    # Set NVM_DIR before running the installer
    export NVM_DIR="$HOME/.config/nvm"
    mkdir -p "$NVM_DIR"
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
else
    echo "nvm is already installed."
fi

echo "Node.js and Python tool setup complete."
