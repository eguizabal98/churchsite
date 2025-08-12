#!/usr/bin/env python3
"""
Fix Remaining Image Paths Script
This script fixes the remaining broken image paths after reorganization.
"""

import os
import re
from pathlib import Path

def fix_remaining_paths():
    project_root = Path(os.getcwd())
    main_css = project_root / 'main.css'
    
    if not main_css.exists():
        print("main.css not found")
        return
    
    # Read current CSS content
    with open(main_css, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Fixing remaining image paths...")
    
    # Define the path fixes based on the organized structure
    path_fixes = {
        'images/banner.jpg': 'images/backgrounds/banner.jpg',
        'images/metro-metro.webp': 'images/payments/Bac_credomatic_logo.svg',  # This was likely renamed
        'images/loading.gif': 'images/uncategorized/loading.gif',
        'images/prev.png': 'images/uncategorized/prev.png', 
        'images/next.png': 'images/uncategorized/next.png',
        'images/close.png': 'images/uncategorized/close.png',
        'images/background-1.jpg': 'images/backgrounds/background-1.jpg',
        'images/background-2.jpg': 'images/backgrounds/background-2.jpg', 
        'images/background-6.jpg': 'images/backgrounds/background-6.jpg'
    }
    
    changes_made = 0
    
    for old_path, new_path in path_fixes.items():
        if old_path in content:
            # Check if the new path actually exists
            full_new_path = project_root / new_path
            if full_new_path.exists():
                content = content.replace(old_path, new_path)
                print(f"✅ Fixed: {old_path} -> {new_path}")
                changes_made += 1
            else:
                print(f"⚠️  Skipped: {old_path} (target {new_path} doesn't exist)")
    
    # Special case for metro-metro.webp - check if it should be the SVG file
    if 'images/metro-metro.webp' in content:
        svg_path = 'images/payments/Bac_credomatic_logo.svg'
        if (project_root / svg_path).exists():
            content = content.replace('images/metro-metro.webp', svg_path)
            print(f"✅ Fixed: images/metro-metro.webp -> {svg_path}")
            changes_made += 1
    
    # Write the updated content
    if changes_made > 0:
        with open(main_css, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Applied {changes_made} fixes to main.css")
    else:
        print("\nℹ️  No fixes were needed or possible")
    
    # Verify the fixes
    print("\nVerifying fixes...")
    verify_image_paths()

def verify_image_paths():
    """Verify that all image paths in CSS now exist"""
    project_root = Path(os.getcwd())
    main_css = project_root / 'main.css'
    
    with open(main_css, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image references
    image_refs = re.findall(r'url\(["\']?([^"\')]+\.(jpg|jpeg|png|gif|webp|svg))["\']?\)', content, re.IGNORECASE)
    
    missing_count = 0
    found_count = 0
    
    for ref in image_refs:
        image_path = ref[0]
        if image_path.startswith('images/'):
            full_path = project_root / image_path
            if full_path.exists():
                print(f"✅ {image_path}")
                found_count += 1
            else:
                print(f"❌ {image_path} (missing)")
                missing_count += 1
    
    print(f"\nSummary: {found_count} found, {missing_count} missing")
    
    if missing_count == 0:
        print("🎉 All image paths are now correct!")
    else:
        print(f"⚠️  {missing_count} image paths still need attention")

if __name__ == "__main__":
    fix_remaining_paths()