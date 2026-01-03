@echo off
echo.
echo ========================================
echo  Blicky Wally - Complete Update
echo ========================================
echo.
echo This will:
echo 1. Rename any new images to --bg-{category}-{number} format
echo 2. Update your website with all images
echo.
echo ========================================
echo.

echo Step 1: Renaming images...
node rename-images.js

echo.
echo Step 2: Updating website...
node generate-image-data.js

echo.
echo ========================================
echo  All Done!
echo ========================================
echo.
echo Your website is now up to date.
echo.
pause
