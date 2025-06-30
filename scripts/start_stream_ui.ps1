# Startskript f\u00fcr die Streamlit UI des GENXAIS-Frameworks
$ErrorActionPreference = "Stop"

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$projectRoot = Join-Path $scriptPath ".."
Set-Location $projectRoot

if (Test-Path ".\.venv311\Scripts\Activate.ps1") {
    . .\.venv311\Scripts\Activate.ps1
}

streamlit run genxais_stream_ui.py @args
