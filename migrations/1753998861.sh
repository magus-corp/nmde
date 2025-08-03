echo "Update Walker config to include . as the leader key for the finder"
if ! grep -q 'prefix = "\."' ~/.config/walker/config.toml; then
  nmde-refresh-walker
fi
