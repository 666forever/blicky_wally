#!/usr/bin/env python3
"""
One-time Image Renaming Script for Blicky Wally
Renames all images to follow the pattern: --bg-{category}-{number}.{ext}
"""

import os
import re
from pathlib import Path

# Configuration
IMAGES_DIR = './Images'
PREFIX = '--bg-'
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
DRY_RUN = True  # Set to False to actually rename files


def get_images_from_dir(dir_path):
    """Get all image files from a directory"""
    images = []
    
    try:
        for item in sorted(os.listdir(dir_path)):
            full_path = os.path.join(dir_path, item)
            
            if os.path.isdir(full_path):
                continue
            
            ext = Path(item).suffix.lower()
            if ext in SUPPORTED_EXTENSIONS:
                images.append(item)
    except Exception as e:
        print(f"Error reading directory {dir_path}: {e}")
    
    return images


def generate_new_filename(category, index, total, extension):
    """Generate new filename with pattern --bg-{category}-{number}.{ext}"""
    # Determine padding based on total count
    if total < 100:
        padding = 2
    elif total < 1000:
        padding = 3
    else:
        padding = 4
    
    number = str(index).zfill(padding)
    
    # Clean up category name (lowercase, replace spaces/special chars with hyphens)
    clean_category = re.sub(r'[^a-z0-9]+', '-', category.lower()).strip('-')
    
    return f'{PREFIX}{clean_category}-{number}{extension}'


def plan_renames():
    """Plan the renaming operation"""
    rename_plan = {
        'categories': {},
        'total_files': 0,
        'total_categories': 0
    }
    
    try:
        items = os.listdir(IMAGES_DIR)
        
        for item in items:
            item_path = os.path.join(IMAGES_DIR, item)
            
            if os.path.isdir(item_path):
                category_name = item
                category_path = item_path
                images = get_images_from_dir(category_path)
                
                if images:
                    rename_plan['categories'][category_name] = {
                        'path': category_path,
                        'renames': []
                    }
                    
                    for index, filename in enumerate(images, 1):
                        ext = Path(filename).suffix
                        new_filename = generate_new_filename(category_name, index, len(images), ext)
                        
                        rename_plan['categories'][category_name]['renames'].append({
                            'old': filename,
                            'new': new_filename,
                            'old_path': os.path.join(category_path, filename),
                            'new_path': os.path.join(category_path, new_filename)
                        })
                    
                    rename_plan['total_files'] += len(images)
                    rename_plan['total_categories'] += 1
            else:
                # Handle loose files in root
                ext = Path(item).suffix.lower()
                if ext in SUPPORTED_EXTENSIONS:
                    if 'other' not in rename_plan['categories']:
                        rename_plan['categories']['other'] = {
                            'path': IMAGES_DIR,
                            'renames': []
                        }
                    rename_plan['categories']['other']['renames'].append({
                        'old': item,
                        'new': item,  # Will process after counting
                        'old_path': os.path.join(IMAGES_DIR, item),
                        'new_path': os.path.join(IMAGES_DIR, item)
                    })
        
        # Process 'other' category if it exists
        if 'other' in rename_plan['categories']:
            other_files = rename_plan['categories']['other']['renames']
            for index, file_info in enumerate(other_files, 1):
                ext = Path(file_info['old']).suffix
                new_filename = generate_new_filename('other', index, len(other_files), ext)
                file_info['new'] = new_filename
                file_info['new_path'] = os.path.join(IMAGES_DIR, new_filename)
            
            rename_plan['total_files'] += len(other_files)
            rename_plan['total_categories'] += 1
        
    except Exception as e:
        print(f'Error planning renames: {e}')
        exit(1)
    
    return rename_plan


def display_plan(plan):
    """Display the rename plan"""
    print('\n📋 Rename Plan:')
    print('═' * 80)
    
    categories = sorted(plan['categories'].keys())
    
    for category in categories:
        category_data = plan['categories'][category]
        renames = category_data['renames']
        
        print(f'\n📁 {category} ({len(renames)} files)')
        print('─' * 80)
        
        # Show first 5 and last 2 examples
        show_count = min(5, len(renames))
        
        for i in range(show_count):
            rename = renames[i]
            print(f"  {rename['old']}")
            print(f"  → {rename['new']}")
            print()
        
        if len(renames) > 7:
            print(f"  ... ({len(renames) - 7} more files) ...")
            print()
            
            # Show last 2
            for i in range(len(renames) - 2, len(renames)):
                rename = renames[i]
                print(f"  {rename['old']}")
                print(f"  → {rename['new']}")
                print()
    
    print('═' * 80)
    print(f'\n📊 Summary:')
    print(f"  Categories: {plan['total_categories']}")
    print(f"  Total files: {plan['total_files']}")
    print()


def execute_renames(plan):
    """Execute the rename operation"""
    success_count = 0
    error_count = 0
    
    print('\n🔄 Renaming files...\n')
    
    for category in plan['categories'].keys():
        category_data = plan['categories'][category]
        
        for rename in category_data['renames']:
            try:
                # Check if old file exists
                if not os.path.exists(rename['old_path']):
                    print(f"  ⚠️  Skipped (not found): {rename['old']}")
                    continue
                
                # Check if new filename already exists
                if os.path.exists(rename['new_path']) and rename['old_path'] != rename['new_path']:
                    print(f"  ⚠️  Skipped (already exists): {rename['new']}")
                    continue
                
                # Skip if already correctly named
                if rename['old'] == rename['new']:
                    continue
                
                os.rename(rename['old_path'], rename['new_path'])
                success_count += 1
                
            except Exception as e:
                print(f"  ❌ Error renaming {rename['old']}: {e}")
                error_count += 1
    
    print('\n✅ Renaming complete!')
    print(f'  Success: {success_count} files')
    if error_count > 0:
        print(f'  Errors: {error_count} files')
    print()


def main():
    """Main execution"""
    print('\n🖼️  Image Renaming Tool')
    print('═' * 80)
    print(f'Pattern: {PREFIX}{{category}}-{{number}}.{{ext}}')
    print(f'Example: {PREFIX}anime-01.png, {PREFIX}gradients-15.jpg')
    print('═' * 80)
    
    # Generate rename plan
    plan = plan_renames()
    
    # Display plan
    display_plan(plan)
    
    if DRY_RUN:
        print('⚠️  DRY RUN MODE - No files will be renamed')
        print('   To actually rename files, edit the script and set DRY_RUN = False')
        print()
        return
    
    # Ask for confirmation
    print('⚠️  WARNING: This will rename all your image files!')
    print('   Make sure you have a backup first.')
    print()
    answer = input('Do you want to proceed? (yes/no): ').strip().lower()
    
    if answer == 'yes':
        execute_renames(plan)
    else:
        print('\n❌ Operation cancelled. No files were renamed.\n')


if __name__ == '__main__':
    main()
