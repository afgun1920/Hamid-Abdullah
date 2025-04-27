#!/usr/bin/env python3
import os
import sys
import http.server
import socketserver
import webbrowser
from pathlib import Path

def serve_website(directory, port=8000):
    """Serve the website locally"""
    os.chdir(directory)
    
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    print(f"Serving website at http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    
    # Open the website in the default browser
    webbrowser.open(f"http://localhost:{port}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

def deploy_to_netlify():
    """Deploy the website to Netlify using netlify-cli"""
    try:
        # Check if netlify-cli is installed
        if os.system("netlify --version > /dev/null 2>&1") != 0:
            print("Installing netlify-cli...")
            os.system("npm install -g netlify-cli")
        
        # Deploy to Netlify
        print("Deploying to Netlify...")
        os.system("netlify deploy --prod")
        
    except Exception as e:
        print(f"Error deploying to Netlify: {str(e)}")
        return False
    
    return True

def deploy_to_github_pages():
    """Deploy the website to GitHub Pages"""
    try:
        # Initialize git repository
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "Initial commit"')
        
        # Ask for GitHub repository URL
        repo_url = input("Enter your GitHub repository URL: ")
        
        # Add remote and push
        os.system(f"git remote add origin {repo_url}")
        os.system("git branch -M main")
        os.system("git push -u origin main")
        
        print("Pushed to GitHub. Set up GitHub Pages in your repository settings.")
        
    except Exception as e:
        print(f"Error deploying to GitHub Pages: {str(e)}")
        return False
    
    return True

def deploy_to_vercel():
    """Deploy the website to Vercel using vercel CLI"""
    try:
        # Check if vercel CLI is installed
        if os.system("vercel --version > /dev/null 2>&1") != 0:
            print("Installing Vercel CLI...")
            os.system("npm install -g vercel")
        
        # Deploy to Vercel
        print("Deploying to Vercel...")
        os.system("vercel --prod")
        
    except Exception as e:
        print(f"Error deploying to Vercel: {str(e)}")
        return False
    
    return True

def main():
    # Get the directory of the current script
    script_dir = Path(__file__).parent.absolute()
    website_dir = script_dir
    
    while True:
        print("\nWebsite Deployment Options:")
        print("1. Test website locally")
        print("2. Deploy to Netlify")
        print("3. Deploy to GitHub Pages")
        print("4. Deploy to Vercel")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            port = input("Enter port number (default: 8000): ") or 8000
            serve_website(website_dir, int(port))
        elif choice == "2":
            deploy_to_netlify()
        elif choice == "3":
            deploy_to_github_pages()
        elif choice == "4":
            deploy_to_vercel()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
