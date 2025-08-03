echo "Adding nmde version info to fastfetch"
if ! grep -q "nmde" ~/.config/fastfetch/config.jsonc; then
  cp ~/.local/share/nmde/config/fastfetch/config.jsonc ~/.config/fastfetch/
fi

