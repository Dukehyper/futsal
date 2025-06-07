# EduDyslexia Example Site

This repository includes a small static website inside `dyslexia_site/` that demonstrates accessibility features aimed at supporting dyslexic university students.

## Running
Simply open `dyslexia_site/index.html` in a modern browser. No build step is required.

## WordPress Integration
The HTML structure is compatible with WordPress templates. To convert this site into a custom theme:

1. Copy the markup of `index.html`, `modules.html`, and `module1.html` into PHP template files such as `page.php` or custom page templates.
2. Enqueue the CSS and JavaScript from the `css` and `js` folders using `wp_enqueue_style` and `wp_enqueue_script` in your theme's `functions.php`.
3. Create Gutenberg blocks for modules and content sections so editors can manage modules through the WordPress admin.
4. Use WordPress accessibility plugins (e.g., WP Accessibility) to provide ARIA landmarks and contrast checking similar to this demo.

The CSS is lightweight and does not depend on any framework, which makes it easy to adapt in a theme.
