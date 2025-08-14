"""Main entry point for the nmde-composes TUI application."""

import os
import json
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

# Assuming the script is run from the project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
COMPOSES_DIR = PROJECT_ROOT / "composes"
STATE_FILE = COMPOSES_DIR / ".state"


class NmdeComposes(App):
    """A Textual app to manage docker-compose stacks."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.compose_files = self.get_compose_files()
        self.services_state = self.load_state()

    def get_compose_files(self) -> list[str]:
        """Scans the composes directory and returns a list of compose files."""
        files = []
        for file in os.listdir(COMPOSES_DIR):
            if file.endswith((".yml", ".yaml")) and os.path.isfile(COMPOSES_DIR / file):
                files.append(file)
        files.sort()
        return files

    def load_state(self) -> dict:
        """Loads the state of the services from the .state file."""
        if not STATE_FILE.exists():
            return {}
        with open(STATE_FILE, "r") as f:
            return json.load(f)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = NmdeComposes()
    app.run()
