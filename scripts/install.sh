#!/usr/bin/env bash
# Set up the development environment: install uv if it is missing, then create .venv and
# install the package plus the dev group from uv.lock.
#
#   ./scripts/install.sh            # from anywhere inside the repo
#
# Afterwards: `uv run pytest`, `uv run python -m elevator_sim ...`, or `source .venv/bin/activate`.
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v uv >/dev/null 2>&1; then
    echo "uv not found; installing it (https://docs.astral.sh/uv/)"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # The installer puts uv in ~/.local/bin (or $XDG_BIN_HOME); make it visible to this shell.
    export PATH="${XDG_BIN_HOME:-$HOME/.local/bin}:$HOME/.cargo/bin:$PATH"
    command -v uv >/dev/null 2>&1 || { echo "uv installed but not on PATH; open a new shell" >&2; exit 1; }
fi

echo "uv $(uv --version | cut -d' ' -f2)"
# Uses the interpreter pinned in .python-version, downloading it if needed.
uv sync
echo
echo "Ready: .venv uses $(uv run python --version)"
echo "Try:   uv run pytest --cov"
