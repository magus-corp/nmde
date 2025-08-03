echo "Start screensaver automatically after 1 minute and stop before locking"

if ! grep -q "nmde-launch-screensaver" ~/.config/hypr/hypridle.conf; then
  nmde-refresh-hypridle
  nmde-refresh-hyprlock
fi
