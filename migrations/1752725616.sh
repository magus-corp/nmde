echo "Make light themes possible"
if [[ -f ~/.local/share/applications/blueberry.desktop ]]; then
  rm -f ~/.local/share/applications/blueberry.desktop
  rm -f ~/.local/share/applications/org.pulseaudio.pavucontrol.desktop
  update-desktop-database ~/.local/share/applications/

  gsettings set org.gnome.desktop.interface color-scheme "prefer-dark"
  gsettings set org.gnome.desktop.interface gtk-theme "Adwaita-dark"

  nmde-refresh-waybar
fi

if [[ ! -L "~/.config/nmde/themes/rose-pine" ]]; then
  ln -snf ~/.local/share/nmde/themes/rose-pine ~/.config/nmde/themes/
fi
