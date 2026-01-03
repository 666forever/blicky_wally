# One-Time Image Renaming Script

This script renames ALL your images to follow a clean, consistent naming pattern.

---

## 📝 Naming Pattern

**Before:**
```
anime (1).jpeg
shape, smooth, minimalism, modern,  (12).jpg
gradient, pastel, white, iridescent,  (7).jpg
```

**After:**
```
--bg-anime-01.jpeg
--bg-abstract-12.jpg
--bg-pastel-07.jpg
```

**Pattern:** `--bg-{category}-{number}.{extension}`

---

## 🚀 How to Use

### Step 1: Preview (Safe Mode)

The script starts in **DRY RUN mode** - it shows you what will happen without changing anything.

**Node.js:**
```bash
node rename-images.js
```

**Python:**
```bash
python rename-images.py
```

This will show you:
- A preview of all renames
- Examples from each category
- Total file count

### Step 2: Actually Rename Files

Once you're happy with the preview:

1. **Edit the script file:**
   - Open `rename-images.js` or `rename-images.py`
   - Find the line: `DRY_RUN = true` (or `True`)
   - Change it to: `DRY_RUN = false` (or `False`)
   - Save the file

2. **Run again:**
   ```bash
   node rename-images.js
   # or
   python rename-images.py
   ```

3. **Type "yes" when prompted**

4. **Done!** All files are renamed

---

## 🎯 What It Does

### Categories from Folders:
- `Images/anime/` → `--bg-anime-01.png`, `--bg-anime-02.jpg`, etc.
- `Images/gradients/` → `--bg-gradients-01.png`, `--bg-gradients-02.jpg`, etc.
- `Images/abstract/` → `--bg-abstract-01.jpeg`, etc.

### Numbers:
- Automatically zero-padded (01, 02, 03...)
- Padding adjusts based on total files:
  - 1-99 files: `01`, `02`, `03`
  - 100-999 files: `001`, `002`, `003`
  - 1000+ files: `0001`, `0002`, `0003`

### Special Characters:
- Spaces → hyphens
- Category names cleaned and lowercased
- `fractal glass` → `fractal-glass`

---

## ⚠️ Important Safety Notes

### BACKUP FIRST!
This is a **one-time operation** that renames ALL your files. Make sure you have a backup before running!

### Why?
- Once files are renamed, there's no automatic undo
- A backup gives you a safety net if something goes wrong

---

## 📊 Example Output

```
🖼️  Image Renaming Tool
════════════════════════════════════════════════════════════════════════════════
Pattern: --bg-{category}-{number}.{ext}
Example: --bg-anime-01.png, --bg-gradients-15.jpg
════════════════════════════════════════════════════════════════════════════════

📋 Rename Plan:
════════════════════════════════════════════════════════════════════════════════

📁 abstract (21 files)
────────────────────────────────────────────────────────────────────────────────
  gradient, chaotic, bright, (1).jpeg
  → --bg-abstract-01.jpeg

  shape, purple, anime, styled, toned down, (3).jpg
  → --bg-abstract-02.jpg

  shape, smooth, minimalism, modern,  (1).jpeg
  → --bg-abstract-03.jpeg

  ...

📁 anime (33 files)
────────────────────────────────────────────────────────────────────────────────
  anime (1).jpeg
  → --bg-anime-01.jpeg

  anime (1).jpg
  → --bg-anime-02.jpg

  ...

════════════════════════════════════════════════════════════════════════════════

📊 Summary:
  Categories: 10
  Total files: 149

⚠️  DRY RUN MODE - No files will be renamed
   To actually rename files, edit the script and set DRY_RUN = false
```

---

## 🔧 After Renaming

Once files are renamed, don't forget to update your website:

```bash
node generate-image-data.js
```

---

## 🆘 Troubleshooting

**Script won't run?**
- Make sure you're in the `blicky_wally` directory
- Check Node.js/Python is installed

**Want to undo?**
- Restore from your backup

**Some files didn't rename?**
- The script skips files if:
  - Target name already exists
  - File is already correctly named
  - File has unsupported extension

---

## 💡 Pro Tips

1. **Run preview first** - Always check DRY RUN output
2. **Backup before running** - Easy recovery if needed
3. **One time only** - After this, use descriptive names for new images
4. **Update website after** - Run `generate-image-data.js` to update index.html

---

## ✨ Benefits

After renaming:
- ✅ Clean, professional filenames
- ✅ Easy to find files (sorted by category and number)
- ✅ Consistent naming across all categories
- ✅ Better organization and management
- ✅ Easier to manage and organize

Enjoy your organized wallpaper collection! 🎉
