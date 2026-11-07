"""
Local Development Server for RetinaVision AI
Automatically opens browser to http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000

def open_browser():
    time.sleep(0.8)
    print(f"[*] Opening browser at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"=======================================================")
        print(f"  RetinaVision AI — Liquid Glass Web Dashboard")
        print(f"  Serving at: http://localhost:{PORT}")
        print(f"  Press Ctrl+C to terminate server.")
        print(f"=======================================================")
        threading.Thread(target=open_browser, daemon=True).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Server stopped.")

