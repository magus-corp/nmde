"""Main entry point for the nmde-composes TUI application."""

import os
import json
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
            # Placeholder for sync logic
            pass
        elif event.button.id == "quit":
            self.exit()

    def action_quit(self) -> None:
        """An action to quit the app."""
        self.exit()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = NmdeComposes()
    app.run()
