#!/usr/bin/env python3
"""
Image Data Generator for Blicky Wally
Scans the Images directory and updates index.html with the latest image data
"""

import os
import json
import re
from pathlib import Path

# Configuration
IMAGES_DIR = './Images'
OUTPUT_FILE = './index.html'
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}


def get_images_from_dir(dir_path):
    """Get all image files from a directory"""
    images = []
    
    try:
        for item in os.listdir(dir_path):
            full_path = os.path.join(dir_path, item)
            
            # Skip directories
            if os.path.isdir(full_path):
                continue
            
            # Check if it's a supported image format
            ext = Path(item).suffix.lower()
            if ext in SUPPORTED_EXTENSIONS:
                images.append(item)
    except Exception as e:
        print(f"Error reading directory {dir_path}: {e}")
    
    return images


def generate_image_data():
    """Scan the Images directory and build the image data structure"""
    image_data = {}
    
    try:
        for item in os.listdir(IMAGES_DIR):
            item_path = os.path.join(IMAGES_DIR, item)
            
            if os.path.isdir(item_path):
                # It's a folder/category
                images = get_images_from_dir(item_path)
                if images:
                    image_data[item] = images
            else:
                # It's a loose file in the root Images directory
                ext = Path(item).suffix.lower()
                if ext in SUPPORTED_EXTENSIONS:
                    if 'other' not in image_data:
                        image_data['other'] = []
                    image_data['other'].append(item)
    except Exception as e:
        print(f"Error scanning Images directory: {e}")
        exit(1)
    
    return image_data


def count_total_images(image_data):
    """Count total images across all categories"""
    return sum(len(images) for images in image_data.values())


def update_index_html(image_data):
    """Update the index.html file with new image data"""
    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert imageData to formatted JSON string with proper indentation
        image_data_string = json.dumps(image_data, indent=12, ensure_ascii=False)
        
        # Find and replace the imageData object in the HTML
        pattern = r'const imageData = \{[\s\S]*?\n        \};'
        replacement = f'const imageData = {image_data_string};'
        
        if re.search(pattern, html_content):
            html_content = re.sub(pattern, replacement, html_content)
            
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print('✅ Successfully updated index.html')
            return True
        else:
            print('❌ Could not find imageData object in index.html')
            return False
    except Exception as e:
        print(f'❌ Error updating index.html: {e}')
        return False


def display_stats(image_data):
    """Display statistics about the image collection"""
    print('\n📊 Image Collection Statistics:')
    print('─' * 50)
    
    categories = sorted(image_data.keys())
    total_images = 0
    
    for category in categories:
        count = len(image_data[category])
        total_images += count
        print(f'  {category:<20} {count:>3} images')
    
    print('─' * 50)
    print(f'  {"TOTAL":<20} {total_images:>3} images')
    print()


def main():
    """Main execution"""
    print('🖼️  Scanning Images directory...\n')
    
    # Generate the image data
    image_data = generate_image_data()
    
    # Display statistics
    display_stats(image_data)
    
    # Ask user if they want to update index.html
    answer = input('Do you want to update index.html with this data? (y/n): ').strip().lower()
    
    if answer in ['y', 'yes']:
        success = update_index_html(image_data)
        if success:
            print('\n✨ Done! Your website is now up to date.\n')
    else:
        print('\n📋 Image data not applied. Here\'s the generated data:\n')
        print(json.dumps(image_data, indent=2, ensure_ascii=False))
        print()


if __name__ == '__main__':
    main()
