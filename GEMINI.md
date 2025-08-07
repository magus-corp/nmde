# Gemini Project Brief: `nmde` Python Migration

This document outlines the core mission for the Gemini agent.

## Primary Objective: Migrate from Bash to Python

The entire `nmde` scripting framework will be migrated from Bash to Python to improve robustness, maintainability, and developer experience. All existing functionality must be preserved.

### Core Migration Tasks:

1.  **Rename `bin` to `spells`**: The script directory will be renamed to `spells`.
2.  **Adopt `uv` for Environment Management**:
    -   A local virtual environment (`.venv`) will be created and managed by `uv`.
    -   All Python dependencies will be installed into this `.venv`.
3.  **Migrate All Scripts**: Every script in the `bin` (soon to be `spells`) directory will be rewritten in Python.
4.  **Integrate `spells`**: Existing `spells` scripts will be integrated into the new Python framework.

## Developpment Loop

1) Evaluate: Always think in what you will do, how you will do it and the conseguences
- Commit-
2) Plan: After thinking, write your plan.
- Commit-
3) Reevaluate: After planing think again. Remember the wisdom of michelangelo and the marble stone:
      Every block of stone has a statue inside it and it is the task of the sculptor to discover it.
      I saw the angel in the marble and carved until I set him free.
  We are chiseling away the raw caos of creation, take your time in the planning because in life and war usually we only need a good or few good strikes.
- Commit-
4) Implement: Do the work with purpuse and with the gods by your side.
- Commit-
5) Reevaluate.
- Commit-
OBS: You always commit.

## Development Operational
We use for versioning:
git add -A .
git commit -m "Commit(put your significant commit here)"
We use for packages:
uv add packages
uv sync


## DONT'S!

You dont try to run the code, the Tester will run and test the code. You only plan and implement the features.
DONT RUN THE CODE
DONT RUN DOCKER COMPOSE OR DOCKER COMMANDS
