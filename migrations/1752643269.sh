echo "Add new matte black theme"

if [[ ! -L "~/.config/nmde/themes/matte-black" ]]; then
  ln -snf ~/.local/share/nmde/themes/matte-black ~/.config/nmde/themes/
fi
