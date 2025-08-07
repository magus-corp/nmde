#!/usr/bin/env python3

import sqlite3
import os
from pathlib import Path
import gumpython

# --- Configuration ---
HOME = Path.home()
NMDE_DIR = HOME / ".local/share/nmde"
ENV_DIR = NMDE_DIR / "composes/env_files"
DB_FILE = ENV_DIR / "envs.db"

# --- Database Functions ---
def get_db_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DB_FILE)

def list_services():
    """Returns a list of all distinct services in the database."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT service FROM envs ORDER BY service;")
        return [row[0] for row in cursor.fetchall()]

def list_vars(service):
    """Returns a dictionary of environment variables for a given service."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM envs WHERE service = ? ORDER BY key;", (service,))
        return {row[0]: row[1] for row in cursor.fetchall()}

def edit_var(service):
    """Opens a TUI to edit or add a new environment variable."""
    key = gumpython.input(placeholder="Variable Name")
    if not key:
        return

    current_vars = list_vars(service)
    current_value = current_vars.get(key, "")
    
    new_value = gumpython.input(placeholder="Variable Value", value=current_value)

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO envs (service, key, value) VALUES (?, ?, ?);", (service, key, new_value))

def delete_var(service):
    """Opens a TUI to delete an environment variable."""
    variables = list_vars(service).keys()
    if not variables:
        gumpython.spin(title="No variables to delete!", spinner="points", time=1)
        return

    var_to_delete = gumpython.choose(list(variables))
    if not var_to_delete:
        return

    if gumpython.confirm(f"Delete '{var_to_delete}' from '{service}'?"):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM envs WHERE service = ? AND key = ?;", (service, var_to_delete))

def rebuild_db():
    """Deletes the existing database and rebuilds it from example .env files."""
    if not gumpython.confirm("This will delete the existing environment database and rebuild it from the example files. Are you sure?"):
        print("Rebuild cancelled.")
        return

    if DB_FILE.exists():
        DB_FILE.unlink()
    print("Old database removed.")

    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS envs (service TEXT, key TEXT, value TEXT, PRIMARY KEY(service, key));")
    print("New database created.")

    for example_file in ENV_DIR.glob("example.*.env"):
        service_name = example_file.name.replace("example.", "").replace(".env", "")
        print(f"Migrating {service_name}...")

        with open(example_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.split("#")[0].strip()
                value = value.strip("\"'")

                with get_db_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT OR REPLACE INTO envs (service, key, value) VALUES (?, ?, ?);", (service_name, key, value))

    gumpython.spin(title="Database rebuild complete!", spinner="globe", time=1)

# --- TUI Menus ---
def service_menu(service):
    """Displays the menu for managing a specific service's environment."""
    while True:
        os.system("clear")
        gumpython.style(f"Managing Environment for: {service}", border="normal", margin="1", padding="1")
        
        variables = list_vars(service)
        for key, value in variables.items():
            print(f"{key:<40} = {value}")

        choice = gumpython.choose(["Edit/Add Variable", "Delete Variable", "Back"])
        if not choice or choice == "Back":
            break
        
        if choice == "Edit/Add Variable":
            edit_var(service)
        elif choice == "Delete Variable":
            delete_var(service)

def main_menu():
    """Displays the main menu."""
    while True:
        os.system("clear")
        services = list_services()
        services.extend(["", "[Rebuild Database]", "[Exit]"])
        
        choice = gumpython.choose(services, header="Select a service to manage")

        if not choice or choice == "[Exit]":
            break
        elif choice == "[Rebuild Database]":
            rebuild_db()
        elif choice:
            service_menu(choice)

if __name__ == "__main__":
    main_menu()
