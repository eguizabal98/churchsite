#!/usr/bin/env python3
"""
CSS Path Update Script for Church Website
This script updates CSS files to reference the newly organized image paths.
"""

import os
import re
from pathlib import Path
import shutil
from datetime import datetime

class CSSPathUpdater:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.backup_dir = self.project_root / 'css_backups'
        self.changes_made = []
        
    def backup_css_files(self):
        """Create backups of CSS files before modification"""
        css_files = list(self.project_root.glob('*.css'))
        
        if not css_files:
            print("No CSS files found in project root.")
            return []
            
        # Create backup directory
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f'backup_{timestamp}'
        backup_path.mkdir(parents=True, exist_ok=True)
        
        backed_up_files = []
        for css_file in css_files:
            backup_file = backup_path / css_file.name
            shutil.copy2(css_file, backup_file)
            backed_up_files.append(backup_file)
            print(f"Backed up: {css_file.name} -> {backup_file}")
            
        return backed_up_files
    
    def update_image_paths(self, dry_run=True):
        """Update image paths in CSS files"""
        css_files = list(self.project_root.glob('*.css'))
        
        # Define path mappings for organized images
        path_mappings = {
            # Carousel images
            r'images/backgrounds/hero-1\.jpg': 'images/carousel/hero-1.jpg',
            r'images/backgrounds/hero-2\.jpg': 'images/carousel/hero-2.jpg', 
            r'images/backgrounds/hero-3\.jpg': 'images/carousel/hero-3.jpg',
            r'images/hero-1\.jpg': 'images/carousel/hero-1.jpg',
            r'images/hero-2\.jpg': 'images/carousel/hero-2.jpg',
            r'images/hero-3\.jpg': 'images/carousel/hero-3.jpg',
            
            # Logo images
            r'images/logo': 'images/logos/logo',
            r'images/brand': 'images/logos/brand',
            
            # Content images - ministries
            r'images/content/ministries/': 'images/content/',
            
            # Content images - sermons  
            r'images/content/sermons/': 'images/content/',
            
            # Content images - gallery
            r'images/content/gallery/': 'images/content/',
            
            # Payment images
            r'images/payments/': 'images/payments/',
            
            # Favicon images
            r'images/favicons/': 'images/favicons/',
        }
        
        for css_file in css_files:
            print(f"\n{'DRY RUN: ' if dry_run else ''}Processing {css_file.name}...")
            
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                original_content = content
                changes_in_file = 0
                
                # Apply path mappings
                for old_pattern, new_path in path_mappings.items():
                    # Find all matches
                    matches = re.findall(old_pattern, content, re.IGNORECASE)
                    if matches:
                        # Replace the matches
                        content = re.sub(old_pattern, new_path, content, flags=re.IGNORECASE)
                        changes_in_file += len(matches)
                        
                        for match in matches:
                            change_info = {
                                'file': css_file.name,
                                'old_path': match if isinstance(match, str) else old_pattern,
                                'new_path': new_path,
                                'pattern': old_pattern
                            }
                            self.changes_made.append(change_info)
                            
                            if dry_run:
                                print(f"  Would change: {old_pattern} -> {new_path}")
                            else:
                                print(f"  Changed: {old_pattern} -> {new_path}")
                
                # Write updated content if changes were made and not dry run
                if changes_in_file > 0 and not dry_run:
                    with open(css_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  ✅ Updated {css_file.name} with {changes_in_file} changes")
                elif changes_in_file > 0 and dry_run:
                    print(f"  📋 Would update {css_file.name} with {changes_in_file} changes")
                else:
                    print(f"  ℹ️  No changes needed in {css_file.name}")
                    
            except Exception as e:
                print(f"  ❌ Error processing {css_file.name}: {e}")
    
    def add_carousel_css(self, dry_run=True):
        """Add specific CSS rules for carousel backgrounds if they don't exist"""
        main_css = self.project_root / 'main.css'
        
        if not main_css.exists():
            print("main.css not found. Cannot add carousel CSS.")
            return
            
        carousel_css = """
/* Carousel Background Images - Added by organization script */
#first-slide {
    background-image: url('images/carousel/hero-1.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

#second-slide {
    background-image: url('images/carousel/hero-2.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

#third-slide {
    background-image: url('images/carousel/hero-3.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
"""
        
        try:
            with open(main_css, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if carousel styles already exist
            if '#first-slide' in content or '#second-slide' in content:
                print("Carousel styles already exist in main.css")
                return
                
            if dry_run:
                print("Would add carousel background CSS to main.css")
                print("Preview of CSS to be added:")
                print(carousel_css)
            else:
                # Add carousel CSS to the end of the file
                updated_content = content + "\n" + carousel_css
                
                with open(main_css, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                    
                print("✅ Added carousel background CSS to main.css")
                
        except Exception as e:
            print(f"❌ Error adding carousel CSS: {e}")
    
    def generate_report(self):
        """Generate a report of changes made"""
        print("\n" + "="*60)
        print("CSS PATH UPDATE REPORT")
        print("="*60)
        
        if not self.changes_made:
            print("No changes were made to CSS files.")
            return
            
        print(f"Total changes made: {len(self.changes_made)}")
        
        # Group changes by file
        files_changed = {}
        for change in self.changes_made:
            file_name = change['file']
            if file_name not in files_changed:
                files_changed[file_name] = []
            files_changed[file_name].append(change)
            
        for file_name, changes in files_changed.items():
            print(f"\n{file_name} ({len(changes)} changes):")
            for change in changes:
                print(f"  • {change['old_path']} -> {change['new_path']}")
    
    def verify_image_paths(self):
        """Verify that referenced images actually exist"""
        print("\nVERIFYING IMAGE PATHS:")
        print("-" * 40)
        
        css_files = list(self.project_root.glob('*.css'))
        missing_images = []
        
        for css_file in css_files:
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find all image references
                image_refs = re.findall(r'url\(["\']?([^"\')]+\.(jpg|jpeg|png|gif|webp|svg))["\']?\)', content, re.IGNORECASE)
                
                for ref in image_refs:
                    image_path = ref[0]
                    if image_path.startswith('images/'):
                        full_path = self.project_root / image_path
                        if not full_path.exists():
                            missing_images.append({
                                'css_file': css_file.name,
                                'image_path': image_path,
                                'full_path': str(full_path)
                            })
                            print(f"❌ Missing: {image_path} (referenced in {css_file.name})")
                        else:
                            print(f"✅ Found: {image_path}")
                            
            except Exception as e:
                print(f"Error checking {css_file.name}: {e}")
                
        if missing_images:
            print(f"\n⚠️  Found {len(missing_images)} missing image references")
        else:
            print("\n✅ All referenced images exist")
            
        return missing_images

def main():
    project_root = os.getcwd()
    
    print("Church Website CSS Path Updater")
    print(f"Project root: {project_root}")
    
    updater = CSSPathUpdater(project_root)
    
    # Create backups
    print("\nCreating backups of CSS files...")
    backups = updater.backup_css_files()
    
    if backups:
        print(f"✅ Created {len(backups)} backup files")
    
    # Dry run first
    print("\n" + "="*60)
    print("DRY RUN - Showing what would be changed:")
    print("="*60)
    
    updater.update_image_paths(dry_run=True)
    updater.add_carousel_css(dry_run=True)
    
    # Ask user if they want to proceed
    print("\n" + "="*60)
    response = input("Do you want to apply these changes? (y/n): ").lower().strip()
    
    if response == 'y':
        print("\nApplying changes...")
        updater.update_image_paths(dry_run=False)
        updater.add_carousel_css(dry_run=False)
        
        # Generate report
        updater.generate_report()
        
        # Verify paths
        updater.verify_image_paths()
        
        print("\n✅ CSS path update complete!")
    else:
        print("\nNo changes applied.")

if __name__ == "__main__":
    main()