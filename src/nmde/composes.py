"""Main entry point for the nmde-composes TUI application."""

import os
import json
import subprocess
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Checkbox, Button
from textual.containers import VerticalScroll


# Assuming the script is run from the project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
COMPOSES_DIR = PROJECT_ROOT / "composes"
STATE_FILE = COMPOSES_DIR / ".state"


class NmdeComposes(App):
    """A Textual app to manage docker-compose stacks."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self):
        super().__init__()
        self.compose_files = self.get_compose_files()
        self.compose_file_map = {Path(f).stem: f for f in self.compose_files}
        self.services_state = self.load_state()

    def get_compose_files(self) -> list[str]:
        """Scans the composes directory and returns a list of compose files."""
        files = []
        if not COMPOSES_DIR.exists():
            return []
        for file in os.listdir(COMPOSES_DIR):
            if file.endswith((".yml", ".yaml")) and os.path.isfile(COMPOSES_DIR / file):
                files.append(file)
        files.sort()
        return files

    def load_state(self) -> dict:
        """Loads the state of the services from the .state file."""
        if not STATE_FILE.exists():
            return {}
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_state(self, state: dict) -> None:
        """Saves the state of the services to the .state file."""
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with VerticalScroll(id="services-list"):
            for filename in self.compose_files:
                service_name = Path(filename).stem
                is_active = self.services_state.get(service_name, False)
                yield Checkbox(service_name, value=is_active, id=service_name)
        yield Button("Sync", variant="primary", id="sync")
        yield Button("Quit", id="quit")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "sync":
            self.run_sync()
        elif event.button.id == "quit":
            self.exit()

    def run_sync(self):
        """Runs the sync logic."""
        self.notify("Syncing services...")
        new_state = {}
        for checkbox in self.query(Checkbox):
            new_state[checkbox.id] = checkbox.value

        for service, is_active in new_state.items():
            was_active = self.services_state.get(service, False)
            
            if service not in self.compose_file_map:
                self.log(f"Compose file for service '{service}' not found. Skipping.")
                continue

            compose_file = COMPOSES_DIR / self.compose_file_map[service]

            if is_active and not was_active:
                self.log(f"Starting {service}...")
                self.run_compose_command(compose_file, "up -d")
            elif not is_active and was_active:
                self.log(f"Stopping {service}...")
                self.run_compose_command(compose_file, "down")

        self.save_state(new_state)
        self.services_state = new_state
        self.notify("Sync complete!")

    def run_compose_command(self, compose_file: Path, command: str):
        """Runs a docker-compose command."""
        try:
            subprocess.run(
                ["docker-compose", "-f", str(compose_file), command],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            self.log(f"Error with {compose_file} {command}: {e.stderr}")
            self.notify(f"Error with {compose_file.stem}!", severity="error")


    def action_quit(self) -> None:
        """An action to quit the app."""
        self.exit()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = NmdeComposes()
    app.run()
