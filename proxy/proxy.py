import http.server
import socketserver
import re
import urllib.request
import json

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        # Forward the request to the destination server
        req = urllib.request.urlopen(self.path)
        self.send_response(req.getcode())
        self.end_headers()
        self.wfile.write(req.read())

    def do_POST(self):
        # Read the request payload
        length = int(self.headers['Content-Length'])
        payload = self.rfile.read(length)

         # Convert the payload from bytes into a dict object
        payload = urllib.parse.parse_qs(payload)
        print(payload) 

        # Manipulate the payload by changing the value of a specific field
        payload[b'username'] = [b'test']
        payload[b'password'] = [b'test']
        print(payload) 

        # Convert the payload back into bytes
        payload = urllib.parse.urlencode(payload, doseq=True).encode()
        
        # Update the Content-Length header with the new length of the payload
        self.headers['Content-Length'] = str(len(payload))

         # Send the modified request to the destination server
        req = urllib.request.Request(self.path, data=payload, headers=self.headers, method="POST")
        res = urllib.request.urlopen(req)

        # Forward the response from the destination server to the client
        self.send_response(res.getcode())
        self.end_headers()
        self.wfile.write(res.read())

# Start the server
socketserver.TCPServer(('', 8080), MyHTTPRequestHandler).serve_forever()
