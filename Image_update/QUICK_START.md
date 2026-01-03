# Quick Start Guide

## 🚀 Easiest Method (Double-Click)

### Windows Users:
1. Double-click `UPDATE_IMAGES.bat`
2. Type `y` when prompted
3. Done!

### Mac/Linux Users:
1. Make the script executable (first time only):
   ```bash
   chmod +x update_images.sh
   ```
2. Double-click `update_images.sh` (or run `./update_images.sh` in terminal)
3. Type `y` when prompted
4. Done!

---

## 📝 Manual Method

If the batch/shell scripts don't work, run directly:

**Node.js:**
```bash
node generate-image-data.js
```

**Python:**
```bash
python generate-image-data.py
```

---

## 📂 Workflow

### Adding New Wallpapers:

1. **Add images** to any category folder:
   ```
   Images/anime/new_wallpaper.jpg
   Images/gradients/cool_gradient.png
   ```

2. **Run the script:**
   - Double-click `UPDATE_IMAGES.bat` (Windows)
   - Double-click `update_images.sh` (Mac/Linux)
   - OR run manually: `node generate-image-data.js`

3. **Confirm update:**
   - Review the statistics
   - Type `y` to update index.html
   - Type `n` to cancel

4. **Test:**
   - Open `index.html` in your browser
   - Check that new images appear

---

## 🎯 That's It!

The script automatically:
- ✅ Scans all folders in `Images/`
- ✅ Finds all image files (jpg, png, gif, webp)
- ✅ Organizes by category
- ✅ Updates your website
- ✅ Shows you statistics

No more manual HTML editing! 🎉
