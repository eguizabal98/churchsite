# Church Website Image Organization Guide

## Overview

This guide documents the organized image structure for the Ciudadanos del Reino church website. All images have been categorized and organized into logical directories for better maintainability and development workflow.

## Directory Structure

```
images/
├── carousel/           # Carousel/Hero section background images
├── backgrounds/        # General background images
├── logos/             # Logo and branding images
├── favicons/          # Favicon and app icons
├── content/           # Content images (ministries, sermons, gallery, etc.)
├── ui/                # UI elements and icons
├── payments/          # Payment and donation related images
└── uncategorized/     # Images that don't fit other categories
```

## Category Details

### 🎠 Carousel (`/images/carousel/`)
**Purpose**: Hero section carousel background images

**Current Files**:
- `hero-1.jpg` (206.5 KB) - First carousel slide background
- `hero-2.jpg` (185.0 KB) - Second carousel slide background  
- `hero-3.jpg` (185.0 KB) - Third carousel slide background

**Usage**: These images are used as background images for the main hero carousel on the homepage. They are referenced in CSS or JavaScript for the `#first-slide`, `#second-slide`, and potentially a third slide.

**CSS Reference Pattern**:
```css
#first-slide {
    background-image: url('../images/carousel/hero-1.jpg');
}

#second-slide {
    background-image: url('../images/carousel/hero-2.jpg');
}
```

### 🖼️ Backgrounds (`/images/backgrounds/`)
**Purpose**: General background images for sections and pages

**Current Files**:
- `404.jpg` - 404 error page background
- `banner.jpg` - General banner background
- `background-1.jpg` - Section background
- `background-2.jpg` - Section background
- `background-6.jpg` - Section background

### 🏷️ Logos (`/images/logos/`)
**Purpose**: Logo and branding images

**Current Files**:
- Various logo files in different formats and sizes
- Brand identity elements

### 📱 Favicons (`/images/favicons/`)
**Purpose**: Website icons for browsers and mobile devices

**Current Files**:
- Multiple favicon sizes and formats
- Apple touch icons
- App icons for various devices

### 📄 Content (`/images/content/`)
**Purpose**: Content-related images organized by type

**Subdirectories**:
- `ministries/` - Ministry-related images
- `sermons/` - Sermon and preaching images
- `gallery/` - Photo gallery images
- `staff/` - Staff and leadership photos
- `events/` - Event photos and promotional images

### 🎨 UI (`/images/ui/`)
**Purpose**: User interface elements and icons

**Note**: Currently empty after reorganization. UI elements were moved to uncategorized for review.

### 💳 Payments (`/images/payments/`)
**Purpose**: Payment and donation related images

**Current Files**:
- Bank logos
- Payment method icons
- Donation-related graphics

### ❓ Uncategorized (`/images/uncategorized/`)
**Purpose**: Images that need manual review and categorization

**Current Files**:
- UI elements that need review (loading.gif, next.png, prev.png, close.png)
- Post images that may need better categorization
- Multimedia ministry images

## Maintenance Guidelines

### Adding New Images

1. **Determine Category**: Before adding new images, determine which category they belong to
2. **Follow Naming Convention**: Use descriptive, lowercase names with hyphens
3. **Optimize Images**: Ensure images are optimized for web use
4. **Update References**: Update any CSS, HTML, or JavaScript references

### Naming Conventions

- Use lowercase letters
- Use hyphens (-) instead of spaces or underscores
- Be descriptive but concise
- Include size indicators when relevant (e.g., `@1.5x`, `@2x`)

**Examples**:
- ✅ `hero-1.jpg`
- ✅ `ministry-youth@1.5x.webp`
- ✅ `sermon-easter-2024.jpg`
- ❌ `Hero Image 1.JPG`
- ❌ `ministry_image.png`

### Image Optimization

- **JPEG**: Use for photographs and complex images
- **PNG**: Use for images with transparency or simple graphics
- **WebP**: Use for modern browsers (provide fallbacks)
- **SVG**: Use for logos and simple graphics

### Updating CSS References

When moving images, update CSS references:

**Before**:
```css
background-image: url('images/hero-1.jpg');
```

**After**:
```css
background-image: url('images/carousel/hero-1.jpg');
```

## Carousel Implementation Notes

### Current Carousel Setup

The homepage carousel uses Owl Carousel with the following structure:

```html
<div class="hero__carousel owl-carousel" id="hero-carousel">
    <div class="slide" id="first-slide">
        <!-- Content -->
    </div>
    <div class="slide" id="second-slide">
        <!-- Content -->
    </div>
</div>
```

### Background Image Implementation

The carousel background images are likely applied through:

1. **CSS Classes**: Direct CSS rules for `#first-slide` and `#second-slide`
2. **JavaScript**: Dynamic application via Owl Carousel's lazy loading
3. **Data Attributes**: HTML data attributes processed by JavaScript

### Recommended CSS Update

Update your CSS file to reference the organized carousel images:

```css
#first-slide {
    background-image: url('../images/carousel/hero-1.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

#second-slide {
    background-image: url('../images/carousel/hero-2.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* If you have a third slide */
#third-slide {
    background-image: url('../images/carousel/hero-3.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
```

## File Size Summary

- **Total Images**: Organized across 8 categories
- **Carousel Images**: 3 files, ~577 KB total
- **Largest Category**: Content images (50+ files)
- **Optimization Opportunity**: Review uncategorized images for proper placement

## Next Steps

1. **Review Uncategorized**: Check the uncategorized folder and properly categorize remaining images
2. **Update CSS**: Update CSS files to reference the new organized paths
3. **Test Website**: Ensure all images load correctly after reorganization
4. **Documentation**: Update any developer documentation with new paths
5. **Backup**: Consider backing up the organized structure

## Tools Used

- **organize_images.py**: Python script for automated image organization
- **image_organization_report.json**: Detailed report of the organization process

---

*Last updated: August 11, 2025*
*Organization completed using automated Python script*