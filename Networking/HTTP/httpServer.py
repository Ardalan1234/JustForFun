from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ''
PORT = 8000


# Define the request handler class
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Set the response content
        response = "Hello, World!"

        # Send the response content
        self.wfile.write(response.encode())


# Set the server address and port
server_address = (HOST, PORT)

# Create an HTTP server with the request handler class
http_server = HTTPServer(server_address, HTTPRequestHandler)

# Start the server
print(f'Server running on port {PORT}...')
http_server.serve_forever()
