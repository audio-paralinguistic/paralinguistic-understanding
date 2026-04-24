#!/usr/bin/env python3
"""Local HTTP server for the ParA-LLM project page."""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def find_free_port(start_port=8000, max_attempts=50):
    import socket
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    return None

def serve_website():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    if not Path('index.html').exists():
        print("Error: index.html not found. Run this script from the website directory.")
        return
    port = find_free_port()
    if port is None:
        print("Error: could not find a free port.")
        return
    httpd = None
    try:
        httpd = socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler)
        print("ParA-LLM project page")
        print("=" * 50)
        print(f"http://localhost:{port}")
        print(f"Serving: {os.getcwd()}")
        print("Ctrl+C to stop\n")
        webbrowser.open(f'http://localhost:{port}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if httpd is not None:
            try:
                httpd.shutdown()
            except Exception:
                pass

if __name__ == "__main__":
    serve_website()
