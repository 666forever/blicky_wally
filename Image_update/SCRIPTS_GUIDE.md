# 🎯 Quick Reference Guide

## 🔄 Two Main Scripts

### 1. **One-Time Rename** (Use Once)
Renames all images to: `--bg-{category}-{number}.ext`

**Preview:**
```bash
node rename-images.js          # Shows preview, doesn't rename
```

**Actually Rename:**
1. Make sure you have a backup
2. Edit `rename-images.js` and change `DRY_RUN = true` to `DRY_RUN = false`
3. Run: `node rename-images.js`
4. Type `yes` to confirm

---

### 2. **Update Website** (Use Every Time You Add Images)
Updates `index.html` with your latest images.

**Quick:**
```bash
# Windows:
Double-click UPDATE_IMAGES.bat

# Mac/Linux:
./update_images.sh

# Manual:
node generate-image-data.js
```

---

## 📝 Complete Workflow

### First Time Setup:
```bash
# 1. Backup first!
# (Your backup method here)

# 2. Preview the rename
node rename-images.js

# 3. If happy, enable actual renaming
# Edit rename-images.js: DRY_RUN = false

# 4. Run again and confirm
node rename-images.js

# 5. Update website
node generate-image-data.js
```

### Adding New Images Later:
```bash
# 1. Add images to category folder
cp new_wallpaper.jpg Images/anime/

# 2. Update website
Double-click UPDATE_IMAGES.bat
# or: node generate-image-data.js

# 3. Type 'y' to confirm
```

---

## 📁 Files Overview

### Renaming (One-Time):
- `rename-images.js` - Node.js rename script
- `rename-images.py` - Python rename script
- `PREVIEW_RENAME.bat` - Windows launcher
- `RENAME_README.md` - Full rename documentation

### Website Updates (Regular):
- `generate-image-data.js` - Node.js generator
- `generate-image-data.py` - Python generator
- `UPDATE_IMAGES.bat` - Windows launcher
- `update_images.sh` - Mac/Linux launcher
- `GENERATOR_README.md` - Full generator documentation

### This Guide:
- `QUICK_START.md` - Quick reference (you are here!)

---

## ⚠️ Safety Rules

1. **Always backup before renaming**
2. **Preview first** (DRY_RUN mode)
3. **Rename is ONE-TIME** - you can't automatically undo
4. **Website updates are safe** - run anytime

---

## 🎨 Naming Examples

After using the rename script:
```
--bg-abstract-01.jpeg
--bg-abstract-02.jpg
--bg-anime-01.png
--bg-anime-02.jpeg
--bg-gradients-01.jpg
--bg-pastel-01.jpg
--bg-phone-01.jpg
```

Clean, professional, and organized! 🎉
