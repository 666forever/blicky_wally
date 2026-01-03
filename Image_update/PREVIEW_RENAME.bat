@echo off
echo.
echo ========================================
echo  One-Time Image Renaming Tool
echo ========================================
echo.
echo This will show you a preview of how your
echo images will be renamed.
echo.
echo Pattern: --bg-{category}-{number}.{ext}
echo Example: --bg-anime-01.png
echo.
echo NO FILES WILL BE CHANGED YET!
echo (This is a preview only)
echo.
echo ========================================
echo.

node rename-images.js

echo.
echo.
echo To actually rename files:
echo 1. Edit rename-images.js
echo 2. Change DRY_RUN = true to DRY_RUN = false
echo 3. Run this script again
echo.
pause
