echo "Add Catppuccin Latte light theme"
if [[ ! -L "~/.config/nmde/themes/catppuccin-latte" ]]; then
  ln -snf ~/.local/share/nmde/themes/catppuccin-latte ~/.config/nmde/themes/
fi
