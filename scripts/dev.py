#!/usr/bin/env python3
"""
MedEd Local Development & Preview Tool
--------------------------------------
Runs validation checks and starts a local web server for live preview.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import subprocess

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PORT = 8000

def main():
    os.chdir(ROOT_DIR)
    
    print("🏥 Running MedEd Integrity Tests before launch...")
    result = subprocess.run([sys.executable, "scripts/validate.py"])
    if result.returncode != 0:
        print("\n⚠ Tests failed! Please fix errors before previewing.")
        sys.exit(1)

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Disable caching during development
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
            super().end_headers()

    print(f"\n🚀 Starting MedEd local preview server at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.\n")

    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            webbrowser.open(f"http://localhost:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped.")

if __name__ == "__main__":
    main()
