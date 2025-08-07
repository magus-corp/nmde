#!/usr/bin/env python3

import subprocess
import gumpython

def setup_dropbox():
    """Runs the Dropbox setup script."""
    print("Setting up Dropbox...")
    subprocess.run(["nmde-setup-dropbox"])

def setup_steam():
    """Runs the Steam setup script."""
    print("Setting up Steam...")
    subprocess.run(["nmde-setup-steam"])

def setup_docker_dbs():
    """Runs the Docker DB setup script."""
    print("Setting up Docker DBs...")
    subprocess.run(["nmde-setup-docker-dbs"])

def setup_fingerprint():
    """Runs the fingerprint setup script."""
    print("Setting up fingerprint sensor...")
    subprocess.run(["nmde-setup-fingerprint"])

def setup_fido2():
    """Runs the FIDO2 setup script."""
    print("Setting up FIDO2 device...")
    subprocess.run(["nmde-setup-fido2"])

def main_menu():
    """Displays the main setup menu."""
    while True:
        choice = gumpython.choose([
            "Dropbox",
            "Steam",
            "Docker DBs",
            "Fingerprint sensor",
            "Fido2 device",
            "Back"
        ])

        if not choice or choice == "Back":
            break
            
        if choice == "Dropbox":
            setup_dropbox()
        elif choice == "Steam":
            setup_steam()
        elif choice == "Docker DBs":
            setup_docker_dbs()
        elif choice == "Fingerprint sensor":
            setup_fingerprint()
        elif choice == "Fido2 device":
            setup_fido2()
            
        gumpython.spin(title="Done!", spinner="globe", time=1)

if __name__ == "__main__":
    main_menu()
