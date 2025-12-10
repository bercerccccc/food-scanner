import http.server
import socketserver
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен → http://localhost:{PORT}/scanner.html")
    webbrowser.open(f"http://localhost:{PORT}/scanner.html")
    httpd.serve_forever()
