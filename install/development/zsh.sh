#!/bin/bash

# This script sets up Zsh without Oh My Zsh for a faster, minimal configuration.

# Ensure zsh is installed
if ! command -v zsh &> /dev/null; then
    echo "Zsh is not installed. Installing it now..."
    sudo pacman -S --noconfirm zsh
fi

echo "Setting up a minimal Zsh configuration..."

# Define directories for plugins and config
ZSH_CONFIG_DIR="$HOME/.config/zsh"
ZSH_PLUGINS_DIR="$ZSH_CONFIG_DIR/plugins"
mkdir -p "$ZSH_PLUGINS_DIR"

# --- Plugin Installation ---

# 1. Powerlevel10k
echo "Installing Powerlevel10k..."
if [ ! -d "$ZSH_PLUGINS_DIR/powerlevel10k" ]; then
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "$ZSH_PLUGINS_DIR/powerlevel10k"
else
    echo "Powerlevel10k is already installed."
fi

# 2. zsh-autosuggestions
echo "Installing zsh-autosuggestions..."
if [ ! -d "$ZSH_PLUGINS_DIR/zsh-autosuggestions" ]; then
    git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions "$ZSH_PLUGINS_DIR/zsh-autosuggestions"
else
    echo "zsh-autosuggestions is already installed."
fi

# 3. zsh-syntax-highlighting
echo "Installing zsh-syntax-highlighting..."
if [ ! -d "$ZSH_PLUGINS_DIR/zsh-syntax-highlighting" ]; then
    git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_PLUGINS_DIR/zsh-syntax-highlighting"
else
    echo "zsh-syntax-highlighting is already installed."
fi

# --- Symlinking Configuration Files ---

echo "Linking .zshrc and .p10k.zsh..."
# Ensure the target directory for the symlink exists
mkdir -p "$HOME"
ln -sf "$HOME/.local/share/nmde/default/zsh/zshrc" "$HOME/.zshrc"
ln -sf "$HOME/.local/share/nmde/default/zsh/p10k.zsh" "$HOME/.p10k.zsh"

# --- Set zsh as default shell ---
if [ "$SHELL" != "$(which zsh)" ]; then
    echo "Setting zsh as the default shell for user $USER..."
    sudo usermod --shell "$(which zsh)" "$USER"
    echo "Default shell has been set to Zsh. Please log out and log back in for the change to take effect."
else
    echo "Zsh is already the default shell."
fi

echo "Minimal Zsh setup complete."
echo "Run 'p10k configure' if you need to customize the prompt."