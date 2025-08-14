"""Command-line interface for the nmde application."""

import argparse

def main():
    """Main entry point for the nmde CLI."""
    parser = argparse.ArgumentParser(description="NMDE main application.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Composes command
    composes_parser = subparsers.add_parser("composes", help="Manage docker-compose stacks.")
    composes_parser.set_defaults(func=run_composes)

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

if __name__ == "__main__":
    main()
