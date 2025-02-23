#!/bin/bash
PYTHON_INTERPRETER="python3"
SCRIPT="main.py"
LOG_FILE="script.log"
log() {
    local MESSAGE="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $MESSAGE" >> "$LOG_FILE"
}
if ! command -v $PYTHON_INTERPRETER &> /dev/null; then
    log "Error: Python interpreter '$PYTHON_INTERPRETER' is not installed."
    exit 1
fi
if [[ ! -f $SCRIPT ]]; then
    log "Error: Script '$SCRIPT' not found."
    exit 1
fi
log "Starting the Python script '$SCRIPT'..."
if $PYTHON_INTERPRETER $SCRIPT >> "$LOG_FILE" 2>&1; then
    log "Python script '$SCRIPT' executed successfully."
else
    log "Error: Python script '$SCRIPT' failed."
    exit 1
fi
log "Script completed."
