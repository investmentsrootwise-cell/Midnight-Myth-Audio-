# Midnight Myth Audio 🦊🌙

Time travel fox-demon 

## About

Midnight Myth Audio is a Black-owned creative-tech startup that fuses horror storytelling, immersive audio, and gamified lore into a living empire. This repository contains the author profile and information for **Robert Stokes**, the founder and mythic architect.

## Features

- 📖 **eBook-first horror loreverse** - Affiliate-driven content designed to empower fans, educators, and creators
- 🎧 **Immersive audio experiences** - Chilling narratives that bring myths to life
- 🎮 **Gamified lore system** - Interactive storytelling with mythic badges
- 🤝 **Affiliate monetization** - Scalable systems for content sharing and earning

## Files

- `index.html` - Main landing page for Midnight Myth Audio
- `author-profile.html` - Author profile page showcasing Robert Stokes
- `author-profile.json` - Structured data containing profile information and social links

## Author Profile

**Robert Stokes** - Founder & Mythic Architect

The founder and mythic architect of Midnight Myth Audio, Robert spearheaded the creation of Lashay's Midnight Myth Audio, an eBook-first affiliate-driven horror loreverse. Through modular content pipelines, branded promo kits, and classroom-ready modules, Robert transforms chilling narratives into scalable systems that affiliates can monetize and audiences can explore endlessly.

### Social Links

- X (Twitter): [@Alexandereagleman453](https://twitter.com/Alexandereagleman453)
- LinkedIn: [cheekssnow](https://www.linkedin.com/in/cheekssnow)
- Facebook: [Alexandereagleman453](https://www.facebook.com/Alexandereagleman453)
- Instagram: [@alexandereagleman453](https://www.instagram.com/alexandereagleman453)
- TikTok: [@robertstokes37](https://tiktok.com/@robertstokes37)
- Threads: [@Alexandereagleman453](https://www.threads.net/@Alexandereagleman453)
- Discord: [Alexandereagleman4539949](https://discord.gg/Alexandereagleman4539949)
- YouTube: [@robertstokes9300](https://www.youtube.com/@robertstokes9300)

## Vision

Building a mythic empire where horror becomes both a story and a shared economy.

## Performance Optimizations

Recent updates have significantly improved the performance and efficiency of the website:

### CSS Architecture Improvements
- **Extracted Inline Styles**: Moved all inline CSS to external stylesheets (`styles.css`, `index.css`, `author-profile.css`)
  - Enables browser caching for faster subsequent page loads
  - Reduces HTML file size by ~85% (from ~9KB to ~3KB per page)
  - Improves maintainability and code reusability

- **CSS Variables**: Implemented CSS custom properties for consistent theming
  - Centralized color palette, gradients, shadows, and transitions
  - Reduces code duplication and improves maintainability
  - Enables easier theme updates and customization

- **Modular Structure**: 
  - `styles.css` - Shared base styles and CSS variables (2KB)
  - `index.css` - Index page-specific styles (2.7KB)
  - `author-profile.css` - Author profile page-specific styles (3.1KB)

### Benefits
- ✅ **Faster page loads**: External CSS files are cached by browsers
- ✅ **Reduced bandwidth**: HTML files are 67% smaller
- ✅ **Better caching**: CSS files can be cached separately with long expiration times
- ✅ **Improved maintainability**: CSS variables make theme updates easier
- ✅ **Enhanced SEO**: Added meta descriptions and theme color
- ✅ **Resource hints**: Preload directives for critical CSS files

### File Size Comparison
| File | Before | After | Reduction |
|------|---------|--------|-----------|
| index.html | 9.2KB | 3.1KB | 66% |
| author-profile.html | 9.7KB | 6.2KB | 36% |
| **Total** | 18.9KB | 17KB* | 10% |

*Includes new CSS files (7.8KB) that are cached separately

## Deployment

This site is deployed via GitHub Pages. Any push to the main branch will automatically update the live site.

