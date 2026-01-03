# Image Data Generator Scripts

These scripts automatically scan your `Images` folder and update `index.html` with the latest wallpaper data. Use this whenever you add new images to avoid manually editing the HTML.

---

## 📦 What You Get

Two versions of the same script:
- **`generate-image-data.js`** - Node.js version
- **`generate-image-data.py`** - Python version

Choose whichever language you have installed!

---

## 🚀 Usage

### Option 1: Node.js Script

**Requirements:** Node.js installed

```bash
# Run the script
node generate-image-data.js

# Follow the prompts:
# - Shows statistics about your images
# - Asks if you want to update index.html
# - Type 'y' to update, 'n' to just see the data
```

### Option 2: Python Script

**Requirements:** Python 3 installed

```bash
# Run the script
python generate-image-data.py

# Or on some systems:
python3 generate-image-data.py

# Follow the same prompts as above
```

---

## 📁 How It Works

1. **Scans** the `Images/` directory
2. **Finds** all image files (`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`)
3. **Organizes** them by folder/category:
   - Files in `Images/anime/` → `"anime"` category
   - Files in `Images/gradients/` → `"gradients"` category
   - Files directly in `Images/` → `"other"` category
4. **Updates** the `imageData` object in `index.html`
5. **Preserves** all your other HTML code

---

## 🎯 When to Use This

Run the script whenever you:
- ✅ Add new wallpapers to any category folder
- ✅ Create a new category folder with images
- ✅ Delete or rename images
- ✅ Move images between categories

---

## 📊 Example Output

```
🖼️  Scanning Images directory...

📊 Image Collection Statistics:
──────────────────────────────────────────────────
  abstract              21 images
  anime                 33 images
  artsy                  6 images
  floral                14 images
  fractal glass         12 images
  gradients             22 images
  iridescent            11 images
  other                  9 images
  pastel                12 images
  phone                  9 images
──────────────────────────────────────────────────
  TOTAL                149 images

Do you want to update index.html with this data? (y/n):
```

---

## ⚙️ Configuration

You can edit these variables at the top of either script if needed:

```javascript
// JavaScript version
const IMAGES_DIR = './Images';
const OUTPUT_FILE = './index.html';
const SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp'];
```

```python
# Python version
IMAGES_DIR = './Images'
OUTPUT_FILE = './index.html'
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
```

---

## 🔒 Safety Features

- ✅ **Confirmation prompt** - Won't update unless you type 'y'
- ✅ **Preview mode** - Type 'n' to see data without updating
- ✅ **Error handling** - Won't corrupt your HTML if something goes wrong

---

## 🆘 Troubleshooting

**Script won't run?**
- Check that you're in the `blicky_wally` directory
- Make sure Node.js or Python is installed: `node --version` or `python --version`

**Can't find images?**
- Verify the `Images` folder exists in the same directory
- Check that your images have supported extensions

**HTML not updating?**
- The script looks for the exact pattern `const imageData = {...};`
- If you've heavily modified the HTML structure, this pattern might not match

---

## 💡 Pro Tips

1. **Run after every image change** - Make it a habit to run the script whenever you add/remove images
2. **Check the output** - Review the statistics to make sure all your images were found
3. **Test your website** - After updating, open `index.html` in a browser to verify everything works

---

## 📝 Quick Workflow

```bash
# 1. Add new images to your folders
cp new_wallpaper.jpg Images/anime/

# 2. Run the generator
node generate-image-data.js
# or
python generate-image-data.py

# 3. Review the stats and confirm with 'y'
```

---

## 🎨 Need Help?

If you run into issues or want to customize the script further, the code is well-commented and easy to modify!
