import http.server, socketserver, os, sys

PORT = int(os.environ.get("PORT", 3456))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    sys.stdout.write(f"Serving on port {PORT}\n")
    sys.stdout.flush()
    httpd.serve_forever()
