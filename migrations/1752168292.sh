echo "Enable battery low notifications for laptops"

if ls /sys/class/power_supply/BAT* &>/dev/null && [[ ! -f ~/.local/share/nmde/config/systemd/user/nmde-battery-monitor.service ]]; then
  mkdir -p ~/.config/systemd/user

  cp ~/.local/share/nmde/config/systemd/user/nmde-battery-monitor.* ~/.config/systemd/user/

  systemctl --user daemon-reload
  systemctl --user enable --now nmde-battery-monitor.timer || true
fi
