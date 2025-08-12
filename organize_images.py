#!/usr/bin/env python3
"""
Image Organization Script for Church Website
This script helps organize and categorize images in the church website project.
"""

import os
import shutil
from pathlib import Path
import json
from datetime import datetime

class ImageOrganizer:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.images_dir = self.project_root / 'images'
        self.report = {
            'timestamp': datetime.now().isoformat(),
            'categories': {},
            'moved_files': [],
            'issues': []
        }
        
    def scan_images(self):
        """Scan all images in the project and categorize them"""
        print("Scanning images directory...")
        
        if not self.images_dir.exists():
            print(f"Images directory not found: {self.images_dir}")
            return
            
        # Define image categories and their patterns
        categories = {
            'carousel': {
                'patterns': ['hero-1', 'hero-2', 'hero-3', 'carousel', 'slide'],
                'description': 'Carousel/Hero section background images',
                'files': []
            },
            'backgrounds': {
                'patterns': ['background', 'banner', 'bg-'],
                'description': 'General background images',
                'files': []
            },
            'logos': {
                'patterns': ['logo', 'brand'],
                'description': 'Logo and branding images',
                'files': []
            },
            'favicons': {
                'patterns': ['favicon', 'icon', 'apple-touch'],
                'description': 'Favicon and app icons',
                'files': []
            },
            'content': {
                'patterns': ['ministry', 'sermon', 'gallery', 'staff', 'event'],
                'description': 'Content images (ministries, sermons, gallery, etc.)',
                'files': []
            },
            'ui': {
                'patterns': ['ui-', 'button', 'arrow', 'social'],
                'description': 'UI elements and icons',
                'files': []
            },
            'payments': {
                'patterns': ['payment', 'donate', 'bank', 'card'],
                'description': 'Payment and donation related images',
                'files': []
            },
            'uncategorized': {
                'patterns': [],
                'description': 'Images that don\'t fit other categories',
                'files': []
            }
        }
        
        # Scan all image files
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
        
        for root, dirs, files in os.walk(self.images_dir):
            for file in files:
                if Path(file).suffix.lower() in image_extensions:
                    file_path = Path(root) / file
                    relative_path = file_path.relative_to(self.images_dir)
                    
                    # Categorize the image
                    categorized = False
                    file_lower = file.lower()
                    
                    for category, info in categories.items():
                        if category == 'uncategorized':
                            continue
                            
                        for pattern in info['patterns']:
                            if pattern in file_lower or pattern in str(relative_path).lower():
                                info['files'].append({
                                    'filename': file,
                                    'current_path': str(relative_path),
                                    'full_path': str(file_path),
                                    'size': file_path.stat().st_size if file_path.exists() else 0
                                })
                                categorized = True
                                break
                        
                        if categorized:
                            break
                    
                    # If not categorized, add to uncategorized
                    if not categorized:
                        categories['uncategorized']['files'].append({
                            'filename': file,
                            'current_path': str(relative_path),
                            'full_path': str(file_path),
                            'size': file_path.stat().st_size if file_path.exists() else 0
                        })
        
        self.report['categories'] = categories
        return categories
    
    def create_organized_structure(self, dry_run=True):
        """Create organized directory structure and optionally move files"""
        print(f"\n{'DRY RUN: ' if dry_run else ''}Creating organized structure...")
        
        categories = self.report['categories']
        
        for category, info in categories.items():
            if not info['files']:
                continue
                
            category_dir = self.images_dir / category
            
            if not dry_run:
                category_dir.mkdir(exist_ok=True)
                print(f"Created directory: {category_dir}")
            else:
                print(f"Would create directory: {category_dir}")
            
            for file_info in info['files']:
                current_path = Path(file_info['full_path'])
                new_path = category_dir / file_info['filename']
                
                if current_path.parent != category_dir:
                    if not dry_run:
                        try:
                            # Create subdirectories if needed
                            new_path.parent.mkdir(parents=True, exist_ok=True)
                            shutil.move(str(current_path), str(new_path))
                            self.report['moved_files'].append({
                                'from': str(current_path),
                                'to': str(new_path)
                            })
                            print(f"Moved: {current_path} -> {new_path}")
                        except Exception as e:
                            error_msg = f"Error moving {current_path}: {str(e)}"
                            print(error_msg)
                            self.report['issues'].append(error_msg)
                    else:
                        print(f"Would move: {current_path} -> {new_path}")
    
    def generate_report(self):
        """Generate a detailed report of the image organization"""
        print("\n" + "="*60)
        print("IMAGE ORGANIZATION REPORT")
        print("="*60)
        
        total_images = 0
        total_size = 0
        
        for category, info in self.report['categories'].items():
            if info['files']:
                category_size = sum(f['size'] for f in info['files'])
                total_size += category_size
                total_images += len(info['files'])
                
                print(f"\n{category.upper()} ({len(info['files'])} files, {self.format_size(category_size)})")
                print(f"Description: {info['description']}")
                print("-" * 40)
                
                for file_info in info['files']:
                    print(f"  • {file_info['filename']} ({self.format_size(file_info['size'])})")
                    print(f"    Path: {file_info['current_path']}")
        
        print(f"\nTOTAL: {total_images} images, {self.format_size(total_size)}")
        
        if self.report['issues']:
            print("\nISSUES:")
            for issue in self.report['issues']:
                print(f"  ! {issue}")
        
        # Save report to file
        report_file = self.project_root / 'image_organization_report.json'
        with open(report_file, 'w') as f:
            json.dump(self.report, f, indent=2)
        print(f"\nDetailed report saved to: {report_file}")
    
    def format_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def find_carousel_images(self):
        """Specifically identify carousel/hero images"""
        print("\nCARROUSEL IMAGES ANALYSIS:")
        print("-" * 40)
        
        carousel_candidates = []
        
        # Look for hero images in backgrounds directory
        backgrounds_dir = self.images_dir / 'backgrounds'
        if backgrounds_dir.exists():
            for file in backgrounds_dir.iterdir():
                if file.is_file() and 'hero' in file.name.lower():
                    carousel_candidates.append(file)
        
        if carousel_candidates:
            print("Found potential carousel images:")
            for img in carousel_candidates:
                print(f"  • {img.name} ({self.format_size(img.stat().st_size)})")
                print(f"    Full path: {img}")
        else:
            print("No carousel images found with 'hero' pattern.")
        
        return carousel_candidates
    
    def check_css_references(self):
        """Check CSS files for image references"""
        print("\nCSS IMAGE REFERENCES:")
        print("-" * 40)
        
        css_files = list(self.project_root.glob('*.css'))
        image_refs = set()
        
        for css_file in css_files:
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Look for image references
                import re
                matches = re.findall(r'url\(["\']?([^"\')]+\.(jpg|jpeg|png|gif|webp|svg))["\']?\)', content, re.IGNORECASE)
                
                for match in matches:
                    image_path = match[0]
                    if 'images/' in image_path:
                        image_refs.add(image_path)
                        print(f"  • {image_path} (in {css_file.name})")
                        
            except Exception as e:
                print(f"Error reading {css_file}: {e}")
        
        return image_refs

def main():
    # Get the current directory (should be the project root)
    project_root = os.getcwd()
    
    print(f"Church Website Image Organizer")
    print(f"Project root: {project_root}")
    
    organizer = ImageOrganizer(project_root)
    
    # Scan images
    categories = organizer.scan_images()
    
    # Find carousel images specifically
    organizer.find_carousel_images()
    
    # Check CSS references
    organizer.check_css_references()
    
    # Generate report
    organizer.generate_report()
    
    # Ask user if they want to organize (dry run first)
    print("\n" + "="*60)
    response = input("Do you want to see what would be moved? (y/n): ").lower().strip()
    
    if response == 'y':
        organizer.create_organized_structure(dry_run=True)
        
        response = input("\nDo you want to actually move the files? (y/n): ").lower().strip()
        if response == 'y':
            organizer.create_organized_structure(dry_run=False)
            print("\nImage organization complete!")
        else:
            print("\nNo files were moved.")
    else:
        print("\nImage scan complete. No files were moved.")

if __name__ == "__main__":
    main()