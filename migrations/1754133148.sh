echo "Update Waybar CSS to dim unused workspaces"

if ! grep -q "#workspaces button\.empty" ~/.config/waybar/style.css; then
  nmde-refresh-config waybar/style.css
  nmde-restart-waybar
fi
