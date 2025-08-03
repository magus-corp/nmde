echo "Add the new ristretto theme as an option"

if [[ ! -L ~/.config/nmde/themes/ristretto ]]; then
  ln -nfs ~/.local/share/nmde/themes/ristretto ~/.config/nmde/themes/
fi
