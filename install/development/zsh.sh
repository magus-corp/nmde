#!/bin/bash

# Ensure zsh is installed (it should be handled by packages_to_install.txt, but good to check)
if ! command -v zsh &> /dev/null
then
    echo "zsh is not installed. Please ensure it's in your packages_to_install.txt and installed."
    exit 1
fi

echo "Setting up Zsh and Powerlevel10k..."

# Install Oh My Zsh
echo "Installing Oh My Zsh..."
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
else
  echo "Oh My Zsh is already installed."
fi

# Install Powerlevel10k
echo "Installing Powerlevel10k..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
else
  echo "Powerlevel10k is already installed."
fi

# Install zsh-autosuggestions
echo "Installing zsh-autosuggestions..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
else
  echo "zsh-autosuggestions is already installed."
fi

# Install zsh-syntax-highlighting
echo "Installing zsh-syntax-highlighting..."
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
else
  echo "zsh-syntax-highlighting is already installed."
fi

# Link .zshrc and .p10k.zsh
echo "Linking .zshrc and .p10k.zsh..."
ln -sf "/home/magus/projects/magus/nmde/default/zsh/.zshrc" "$HOME/.zshrc"
ln -sf "/home/magus/projects/magus/nmde/default/zsh/.p10k.zsh" "$HOME/.p10k.zsh"

# Set zsh as default shell
echo "Setting zsh as default shell..."
if [ "$(basename "$SHELL")" != "zsh" ]; then
  chsh -s $(which zsh)
  echo "Default shell set to zsh. Please log out and log back in for changes to take effect."
else
  echo "Zsh is already the default shell."
fi

echo "Zsh and Powerlevel10k setup complete. Remember to run 'p10k configure' after logging into zsh for the first time."
