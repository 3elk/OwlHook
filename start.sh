#!/bin/bash
set -euo pipefail
LOG_FILE="script.log"
log() {
    local MESSAGE="$1"
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $MESSAGE" >> "$LOG_FILE"
}
if ! command -v python &> /dev/null; then
    log "Python is not installed. Exiting."
    exit 1
fi
log "Starting the Python script..."
if python main.py >> "$LOG_FILE" 2>&1; then
    log "Python script executed successfully."
else
    log "Python script failed with an error."
    exit 1
fi
log "Script completed."
