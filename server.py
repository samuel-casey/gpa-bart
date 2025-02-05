from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import sys


def run_server(port=4000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server started at http://localhost:{port}")

    # Open browser automatically
    webbrowser.open(f'http://localhost:{port}')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == '__main__':
    # Use custom port if provided as argument
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
