# CHARITRA for Firefox (Gecko) - AMO Package Builder
# Invokes package.py to guarantee POSIX forward slash (/) separators for AMO validation
$ProgressPreference = 'SilentlyContinue'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptDir

python package.py
