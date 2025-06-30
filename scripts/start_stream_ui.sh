#!/bin/bash
# Startskript f\u00fcr die Streamlit UI des GENXAIS-Frameworks
set -e

PROJECT_ROOT="$(dirname "$0")/.."
cd "$PROJECT_ROOT"

if [ -f ".venv311/bin/activate" ]; then
    source .venv311/bin/activate
fi

streamlit run genxais_stream_ui.py "$@"
