const fs = require('fs');
const path = require('path');

// Configuration
const IMAGES_DIR = './Images';
const OUTPUT_FILE = './index.html';
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
    
    return images;
}

/**
 * Scan the Images directory and build the image data structure
 */
function generateImageData() {
    const imageData = {};
    
    try {
        const categories = fs.readdirSync(IMAGES_DIR);
        
        for (const category of categories) {
            const categoryPath = path.join(IMAGES_DIR, category);
            const stat = fs.statSync(categoryPath);
            
            if (stat.isDirectory()) {
                const images = getImagesFromDir(categoryPath);
                if (images.length > 0) {
                    imageData[category] = images;
                }
            } else {
                const ext = path.extname(category).toLowerCase();
                if (SUPPORTED_EXTENSIONS.includes(ext)) {
                    if (!imageData['other']) {
                        imageData['other'] = [];
                    }
                    imageData['other'].push(category);
                }
            }
        }
    } catch (error) {
        console.error('Error scanning Images directory:', error.message);
        process.exit(1);
    }
    
    return imageData;
}

/**
 * Update the index.html file with new image data
 */
function updateIndexHTML(imageData) {
    try {
        let htmlContent = fs.readFileSync(OUTPUT_FILE, 'utf8');
        
        const imageDataString = JSON.stringify(imageData, null, 12);
        const regex = /const imageData = \{[\s\S]*?\n        \};/;
        const replacement = `const imageData = ${imageDataString};`;
        
        if (regex.test(htmlContent)) {
            htmlContent = htmlContent.replace(regex, replacement);
            fs.writeFileSync(OUTPUT_FILE, htmlContent, 'utf8');
            console.log('✅ Updated website with all images');
            return true;
        } else {
            console.error('❌ Could not find imageData object in index.html');
            return false;
        }
    } catch (error) {
        console.error('❌ Error updating index.html:', error.message);
        return false;
    }
}

/**
 * Display statistics
 */
function displayStats(imageData) {
    console.log('📊 Statistics:');
    console.log('─'.repeat(40));
    
    const categories = Object.keys(imageData).sort();
    let totalImages = 0;
    
    for (const category of categories) {
        const count = imageData[category].length;
        totalImages += count;
        console.log(`  ${category.padEnd(20)} ${count.toString().padStart(3)} images`);
    }
    
    console.log('─'.repeat(40));
    console.log(`  ${'TOTAL'.padEnd(20)} ${totalImages.toString().padStart(3)} images`);
    console.log('');
}

/**
 * Main execution
 */
function main() {
    console.log('🖼️  Scanning Images directory...\n');
    
    const imageData = generateImageData();
    displayStats(imageData);
    
    const success = updateIndexHTML(imageData);
    if (success) {
        console.log('✨ Website is up to date!\n');
    }
}

// Run the script
main();
