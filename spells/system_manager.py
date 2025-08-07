#!/usr/bin/env python3

import subprocess
import gumpython

def refresh_waybar():
    """Refreshes the Waybar configuration."""
    print("Refreshing Waybar...")
    subprocess.run(["nmde-refresh-waybar"])

def refresh_walker():
    """Refreshes the Walker configuration."""
    print("Refreshing Walker...")
    subprocess.run(["nmde-refresh-walker"])

def refresh_plymouth():
    """Refreshes the Plymouth configuration."""
    print("Refreshing Plymouth...")
    subprocess.run(["nmde-refresh-plymouth"])

def refresh_swayosd():
    """Refreshes the SwayOSD configuration."""
    print("Refreshing SwayOSD...")
    subprocess.run(["nmde-refresh-swayosd"])
    
def refresh_applications():
    """Refreshes the application list."""
    print("Refreshing applications...")
    subprocess.run(["nmde-refresh-applications"])

def generate_logo():
    """Generates the nmde logo."""
    print("Generating logo...")
    subprocess.run(["nmde-generate-logo"])

def update_nmde():
    """Updates the nmde installation."""
    print("Updating nmde...")
    subprocess.run(["nmde-update"])

def main_menu():
    """Displays the main system management menu."""
    while True:
        choice = gumpython.choose([
            "Update nmde",
            "Refresh Waybar",
            "Refresh Walker",
            "Refresh Plymouth",
            "Refresh SwayOSD",
            "Refresh Desktop Apps",
            "Generate Logo",
            "Back"
        ])

        if not choice or choice == "Back":
            break
            
        if choice == "Update nmde":
            update_nmde()
        elif choice == "Refresh Waybar":
            refresh_waybar()
        elif choice == "Refresh Walker":
            refresh_walker()
        elif choice == "Refresh Plymouth":
            refresh_plymouth()
        elif choice == "Refresh SwayOSD":
            refresh_swayosd()
        elif choice == "Refresh Desktop Apps":
            refresh_applications()
        elif choice == "Generate Logo":
            generate_logo()
            
        gumpython.spin(title="Done!", spinner="globe", time=1)

if __name__ == "__main__":
    main_menu()
