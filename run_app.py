#!/usr/bin/env python3
"""
AI Speech Advisory - Application Launcher
Choose between Flask web interface and Streamlit interface
"""

import os
import sys
import subprocess
import webbrowser
import time

def print_banner():
    """Print application banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🎤 AI Speech Advisory                     ║
    ║                 Your Personal Speaking Coach                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'streamlit', 'openai']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("📦 Installing missing packages...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies. Please run: pip install -r requirements.txt")
            return False
    
    return True

def run_flask_app():
    """Run the Flask web application"""
    print("🚀 Starting Flask web application...")
    print("📱 Web interface will be available at: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        # Start Flask app
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Flask application stopped.")

def run_streamlit_app():
    """Run the Streamlit application"""
    print("🚀 Starting Streamlit application...")
    print("📱 Streamlit interface will be available at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        # Start Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "UI/interface.py"])
    except KeyboardInterrupt:
        print("\n🛑 Streamlit application stopped.")

def main():
    """Main launcher function"""
    print_banner()
    
    # Check dependencies
    if not check_dependencies():
        return
    
    while True:
        print("\n🎯 Choose your interface:")
        print("1. 🌐 Flask Web Interface (Modern web app)")
        print("2. 📊 Streamlit Interface (Interactive dashboard)")
        print("3. 📦 Install/Update Dependencies")
        print("4. ❌ Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n🌐 Launching Flask Web Interface...")
            # Open browser after a short delay
            def open_browser():
                time.sleep(2)
                webbrowser.open("http://localhost:5001")
            
            import threading
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            run_flask_app()
            
        elif choice == "2":
            print("\n📊 Launching Streamlit Interface...")
            # Open browser after a short delay
            def open_browser():
                time.sleep(3)
                webbrowser.open("http://localhost:8501")
            
            import threading
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            run_streamlit_app()
            
        elif choice == "3":
            print("\n📦 Installing/Updating dependencies...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
                print("✅ Dependencies updated successfully!")
            except subprocess.CalledProcessError:
                print("❌ Failed to install dependencies.")
            except FileNotFoundError:
                print("❌ requirements.txt not found.")
                
        elif choice == "4":
            print("\n👋 Thank you for using AI Speech Advisory!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main() 