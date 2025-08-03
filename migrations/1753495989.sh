echo "Allow updating of timezone by right-clicking on the clock (or running nmde-cmd-tzupdate)"
if ! command -v tzupdate &>/dev/null; then
  bash ~/.local/share/nmde/install/config/timezones.sh
  nmde-refresh-waybar
fi
