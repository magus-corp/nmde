"""Command-line interface for the nmde application."""

import argparse

def main():
    """Main entry point for the nmde CLI."""
    parser = argparse.ArgumentParser(description="NMDE main application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Composes command
    composes_parser = subparsers.add_parser("composes", help="Manage docker-compose stacks.")
    composes_parser.set_defaults(func=run_composes)

    # Generate logo command
    generate_logo_parser = subparsers.add_parser("generate-logo", help="Generate the NMDE logo.")
    generate_logo_parser.set_defaults(func=run_generate_logo)

    # Power Menu command
    power_menu_parser = subparsers.add_parser("menu-power", help="Show the power menu.")
    power_menu_parser.set_defaults(func=run_power_menu)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

def run_composes(args):
    """Runs the nmde-composes TUI application."""
    from .composes import NmdeComposes
    app = NmdeComposes()
    app.run()

def run_generate_logo(args):
    """Runs the logo generation script."""
    from .logo import generate_logo
    generate_logo()

def run_power_menu(args):
    """Shows the power menu."""
    from .menu import show_power_menu
    show_power_menu()

if __name__ == "__main__":
    main()
