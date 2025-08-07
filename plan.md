# Python Migration Plan

This document outlines the strategy for migrating the `nmde` scripting framework from Bash to Python.

## Phase 1: Project Setup & Restructuring

1.  **Rename `bin` to `spells`**:
    -   Use `git mv` to rename the `bin` directory to `spells` to preserve file history.
    -   Update any hardcoded references to `/bin/` in the existing codebase.
2.  **Establish Python Environment with `uv`**:
    -   Create a `requirements.txt` file for Python dependencies.
    -   Add initial core dependencies (e.g., `ruamel.yaml` as a `yq` replacement).
    -   Create a `.venv` using `uv venv`.
    -   Update the `.gitignore` file to include `.venv/`.
3.  **Update Installation Scripts**:
    -   Modify the installation process to use `uv` to set up the virtual environment and install the packages from `requirements.txt`.
    -   Remove the direct installation of packages that will be handled by Python libraries.

## Phase 2: Script Migration

I will migrate the scripts from Bash to Python one by one, ensuring all functionality is preserved.

**Migration Order (Tentative):**
1.  `nmde-env` & `nmde-env-rebuild-db` (Database interaction)
2.  `nmde-composes` (Core application logic)
3.  `nmde` (Main menu)
4.  Helper scripts (`nmde-refresh-*`, `nmde-theme-*`, etc.)

**For each script:**
1.  Translate the logic to Python, using libraries like `subprocess`, `pathlib`, and `argparse`.
2.  Refactor to use Python-native features where possible (e.g., string manipulation instead of `sed`).
3.  Ensure the new script is executable and uses the correct shebang to run in our `.venv`.
4.  Commit each migrated script individually.

## Phase 3: Integration and Cleanup

1.  Update all scripts to call their new Python counterparts.
2.  Remove the old Bash scripts once they are replaced.
3.  Perform a final review of the entire codebase for consistency.
