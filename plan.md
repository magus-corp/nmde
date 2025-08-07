# Python Migration Plan

This document outlines the strategy for migrating the `nmde` scripting framework from Bash to Python.

## Phase 1: Project Setup & Restructuring - COMPLETE

1.  **[DONE]** Rename `bin` to `spells`.
2.  **[DONE]** Establish Python Environment with `uv`.
3.  **[DONE]** Update Installation Scripts to use `uv`.

## Phase 2: Script Migration - COMPLETE

The core application logic has been migrated to Python. The following modules have been created:

-   `spells/nmde-tui`: The main application entry point.
-   `spells/nmde-env`: Environment variable manager.
-   `spells/nmde-composes`: Docker Compose manager.
-   `spells/theme_manager.py`: Theme manager.
-   `spells/system_manager.py`: System update and refresh manager.
-   `spells/setup_manager.py`: Setup manager.

## Phase 3: Integration and Cleanup - COMPLETE

1.  **[DONE]** The main TUI now calls the new Python modules.
2.  **[DONE]** The old Bash scripts for core functionality have been removed.
3.  **[ONGOING]** The remaining standalone utility scripts in the `spells` directory can be migrated to Python over time.

## Next Steps

-   Continue migrating the remaining standalone Bash scripts to Python as needed.
-   Refactor the new Python scripts to improve code quality and add new features.