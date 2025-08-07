#!/usr/bin/env python3

import os
import shutil
import subprocess
from pathlib import Path
import gumpython
from git import Repo

# --- Configuration ---
HOME = Path.home()
NMDE_DIR = HOME / ".local/share/nmde"
THEMES_DIR = NMDE_DIR / "themes"
CURRENT_THEME_DIR = NMDE_DIR / "config/nmde/current/theme"

# --- Helper Functions ---
def get_available_themes():
    """Returns a list of available themes."""
    return [d.name for d in THEMES_DIR.iterdir() if d.is_dir()]

def set_theme(theme_name):
    """Sets the active theme by creating a symlink."""
    if theme_name not in get_available_themes():
        print(f"Error: Theme '{theme_name}' not found.")
        return

    theme_path = THEMES_DIR / theme_name
    if CURRENT_THEME_DIR.exists():
        CURRENT_THEME_DIR.unlink()
    
    CURRENT_THEME_DIR.symlink_to(theme_path)
    print(f"Theme set to '{theme_name}'.")
    
    # Restart waybar and set background
    subprocess.run(["nmde-restart-waybar"])
    subprocess.run(["nmde-theme-bg-next"])


# --- TUI Menus ---
def install_theme():
    """Prompts for a Git URL and installs a new theme."""
    url = gumpython.input(placeholder="Git repo URL for theme")
    if not url:
        return
    
    theme_name = url.split("/")[-1].replace(".git", "")
    theme_path = THEMES_DIR / theme_name
    
    if theme_path.exists():
        print(f"Theme '{theme_name}' already exists.")
        return
        
    try:
        Repo.clone_from(url, theme_path)
        print(f"Theme '{theme_name}' installed successfully.")
    except Exception as e:
        print(f"Error installing theme: {e}")

def remove_theme():
    """Prompts to select and remove a theme."""
    themes = get_available_themes()
    if not themes:
        print("No themes to remove.")
        return
        
    theme_to_remove = gumpython.choose(themes)
    if not theme_to_remove:
        return
        
    if gumpython.confirm(f"Are you sure you want to remove the theme '{theme_to_remove}'?"):
        shutil.rmtree(THEMES_DIR / theme_to_remove)
        print(f"Theme '{theme_to_remove}' removed.")
        
        # If the removed theme was the current one, set the next available theme
        if not CURRENT_THEME_DIR.exists():
            next_theme = get_available_themes()
            if next_theme:
                set_theme(next_theme[0])

def update_themes():
    """Updates all installed themes by pulling the latest changes."""
    for theme in get_available_themes():
        theme_path = THEMES_DIR / theme
        try:
            repo = Repo(theme_path)
            origin = repo.remotes.origin
            origin.pull()
            print(f"Theme '{theme}' updated.")
        except Exception as e:
            print(f"Error updating theme '{theme}': {e}")

def main_menu():
    """Displays the main theme management menu."""
    while True:
        os.system("clear")
        choice = gumpython.choose([
            "Pick", "Install", "Update", "Remove", "Back"
        ])

        if not choice or choice == "Back":
            break
            
        if choice == "Pick":
            themes = get_available_themes()
            if not themes:
                print("No themes available to pick.")
                gumpython.spin(spinner="points", time=2)
                continue
            
            selected_theme = gumpython.choose(themes)
            if selected_theme:
                set_theme(selected_theme)
                
        elif choice == "Install":
            install_theme()
        elif choice == "Update":
            update_themes()
        elif choice == "Remove":
            remove_theme()
            
        gumpython.spin(title="Done!", spinner="globe", time=1)

if __name__ == "__main__":
    main_menu()
