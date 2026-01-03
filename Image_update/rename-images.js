const fs = require('fs');
const path = require('path');

// Configuration
const IMAGES_DIR = './Images';
const PREFIX = '--bg-';
const SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp'];

/**
 * Get all image files from a directory
 */
function getImagesFromDir(dirPath) {
    const images = [];
    
    try {
        const items = fs.readdirSync(dirPath);
        
        for (const item of items) {
            const fullPath = path.join(dirPath, item);
            const stat = fs.statSync(fullPath);
            
            if (stat.isDirectory()) continue;
            
            const ext = path.extname(item).toLowerCase();
            if (SUPPORTED_EXTENSIONS.includes(ext)) {
                images.push(item);
            }
        }
    } catch (error) {
        console.error(`Error reading directory ${dirPath}:`, error.message);
    }
    
    return images.sort();
}

/**
 * Generate new filename with pattern --bg-{category}-{number}.{ext}
 */
function generateNewFilename(category, index, total, extension) {
    const padding = total < 100 ? 2 : total < 1000 ? 3 : 4;
    const number = String(index).padStart(padding, '0');
    
    const cleanCategory = category
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');
    
    return `${PREFIX}${cleanCategory}-${number}${extension}`;
}

/**
 * Plan the renaming operation
 */
function planRenames() {
    const renamePlan = {
        categories: {},
        totalFiles: 0,
        totalCategories: 0
    };
    
    try {
        const items = fs.readdirSync(IMAGES_DIR);
        
        for (const item of items) {
            const itemPath = path.join(IMAGES_DIR, item);
            const stat = fs.statSync(itemPath);
            
            if (stat.isDirectory()) {
                const categoryName = item;
                const categoryPath = itemPath;
                const images = getImagesFromDir(categoryPath);
                
                if (images.length > 0) {
                    renamePlan.categories[categoryName] = {
                        path: categoryPath,
                        renames: []
                    };
                    
                    images.forEach((filename, index) => {
                        const ext = path.extname(filename);
                        const newFilename = generateNewFilename(categoryName, index + 1, images.length, ext);
                        
                        renamePlan.categories[categoryName].renames.push({
                            old: filename,
                            new: newFilename,
                            oldPath: path.join(categoryPath, filename),
                            newPath: path.join(categoryPath, newFilename)
                        });
                    });
                    
                    renamePlan.totalFiles += images.length;
                    renamePlan.totalCategories++;
                }
            } else {
                const ext = path.extname(item).toLowerCase();
                if (SUPPORTED_EXTENSIONS.includes(ext)) {
                    if (!renamePlan.categories['other']) {
                        renamePlan.categories['other'] = {
                            path: IMAGES_DIR,
                            renames: []
                        };
                    }
                    renamePlan.categories['other'].renames.push({
                        old: item,
                        new: item,
                        oldPath: path.join(IMAGES_DIR, item),
                        newPath: path.join(IMAGES_DIR, item)
                    });
                }
            }
        }
        
        if (renamePlan.categories['other']) {
            const otherFiles = renamePlan.categories['other'].renames;
            otherFiles.forEach((file, index) => {
                const ext = path.extname(file.old);
                const newFilename = generateNewFilename('other', index + 1, otherFiles.length, ext);
                file.new = newFilename;
                file.newPath = path.join(IMAGES_DIR, newFilename);
            });
            renamePlan.totalFiles += otherFiles.length;
            renamePlan.totalCategories++;
        }
        
    } catch (error) {
        console.error('Error planning renames:', error.message);
        process.exit(1);
    }
    
    return renamePlan;
}

/**
 * Execute the rename operation
 */
function executeRenames(plan) {
    let successCount = 0;
    let skipCount = 0;
    let errorCount = 0;
    
    for (const category of Object.keys(plan.categories)) {
        const categoryData = plan.categories[category];
        
        for (const rename of categoryData.renames) {
            try {
                if (!fs.existsSync(rename.oldPath)) {
                    skipCount++;
                    continue;
                }
                
                if (fs.existsSync(rename.newPath) && rename.oldPath !== rename.newPath) {
                    skipCount++;
                    continue;
                }
                
                if (rename.old === rename.new) {
                    skipCount++;
                    continue;
                }
                
                fs.renameSync(rename.oldPath, rename.newPath);
                successCount++;
                
            } catch (error) {
                errorCount++;
            }
        }
    }
    
    return { successCount, skipCount, errorCount };
}

/**
 * Main execution
 */
function main() {
    console.log('\n🔄 Renaming images...\n');
    
    const plan = planRenames();
    const results = executeRenames(plan);
    
    if (results.successCount > 0) {
        console.log(`✅ Renamed ${results.successCount} files`);
    }
    if (results.skipCount > 0) {
        console.log(`⏭️  Skipped ${results.skipCount} files (already correctly named)`);
    }
    if (results.errorCount > 0) {
        console.log(`❌ ${results.errorCount} errors`);
    }
    
    console.log();
}

// Run the script
main();
