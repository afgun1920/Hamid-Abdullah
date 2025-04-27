# Netlify Deployment Instructions

This document provides instructions for deploying your website to Netlify using Netlify Drop, a simple drag-and-drop deployment method.

## What is Netlify Drop?

Netlify Drop is a service that allows you to deploy a website by simply dragging and dropping your website files onto the Netlify Drop page. It's the easiest way to deploy a static website without requiring command-line tools or authentication.

## Deployment Steps

1. **Prepare your website files**
   - Your website files are already prepared in this folder
   - The `netlify.toml` configuration file has been added to handle routing and settings

2. **Deploy using Netlify Drop**
   - Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
   - Drag and drop this entire folder onto the drop zone
   - Netlify will automatically upload and deploy your website

3. **After deployment**
   - Netlify will provide you with a unique URL for your website (e.g., https://your-site-name.netlify.app)
   - You can customize this URL in the Netlify dashboard
   - You can also connect a custom domain if you have one

## Additional Configuration

The `netlify.toml` file includes:
- Configuration for proper routing
- Environment settings
- Redirect rules to ensure your website works correctly

## Custom Domain Setup (Optional)

If you want to use a custom domain:
1. In the Netlify dashboard, go to "Domain settings"
2. Click "Add custom domain"
3. Follow the instructions to configure your DNS settings

## Continuous Deployment (Optional)

For continuous deployment:
1. Connect your Netlify site to a Git repository
2. Push changes to your repository
3. Netlify will automatically rebuild and deploy your site

## Need Help?

Visit [Netlify Support](https://www.netlify.com/support/) for additional assistance.
