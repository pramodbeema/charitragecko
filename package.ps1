# CHARITRA for Firefox (Gecko) - AMO Package Builder
$ProgressPreference = 'SilentlyContinue'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptDir

$zipName = "CharitraGecko-v1.0.0-firefox.zip"
$xpiName = "CharitraGecko-v1.0.0-firefox.xpi"

# Remove existing builds
Remove-Item -Path $zipName, $xpiName -ErrorAction SilentlyContinue

# Files and folders to package for AMO submission
$itemsToPackage = @(
    "manifest.json",
    "LICENSE",
    "css",
    "icons",
    "js",
    "pages"
)

# Create zip archive
Compress-Archive -Path $itemsToPackage -DestinationPath $zipName -Force
Copy-Item -Path $zipName -Destination $xpiName -Force

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  CHARITRA Gecko MV3 Package Built Successfully!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " - Archive (ZIP): $zipName"
Write-Host " - Package (XPI): $xpiName"
Write-Host ""
Write-Host "Ready to test in Firefox:" -ForegroundColor Yellow
Write-Host " 1. Open Firefox and go to: about:debugging#/runtime/this-firefox"
Write-Host " 2. Click 'Load Temporary Add-on...'"
Write-Host " 3. Select manifest.json in this directory"
Write-Host ""
Write-Host "Ready to submit to AMO:" -ForegroundColor Yellow
Write-Host " https://addons.mozilla.org/en-US/developers/addon/submit/upload-listed"
Write-Host "==========================================================" -ForegroundColor Cyan
