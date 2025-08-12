#!/usr/bin/env python3
"""
Script to prettify all HTML files in the churchsite project
"""

import os
import glob
from bs4 import BeautifulSoup

def prettify_html_file(file_path):
    """Prettify a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Prettify the HTML
        prettified = soup.prettify()
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(prettified)
        
        print(f"✓ Prettified: {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error prettifying {file_path}: {str(e)}")
        return False

def main():
    """Main function to prettify all HTML files"""
    # Get all HTML files in the current directory
    html_files = glob.glob('*.html')
    
    if not html_files:
        print("No HTML files found in the current directory.")
        return
    
    print(f"Found {len(html_files)} HTML files to prettify...\n")
    
    success_count = 0
    for html_file in sorted(html_files):
        if prettify_html_file(html_file):
            success_count += 1
    
    print(f"\nCompleted! Successfully prettified {success_count}/{len(html_files)} files.")

if __name__ == "__main__":
    main()