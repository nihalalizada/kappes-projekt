import http.server
import socketserver
import urllib.request

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        # Request an Server schicken
        req = urllib.request.urlopen(self.path)
        self.send_response(req.getcode())
        self.end_headers()
        self.wfile.write(req.read())

    def do_POST(self):
        # Payload Request lesen
        length = int(self.headers['Content-Length'])
        payload = self.rfile.read(length)

         # Payload von Byte in dict Object umwandeln
        payload = urllib.parse.parse_qs(payload)
        print(payload) 

        # payload maniplulieren
        payload[b'username'] = [b'test'] #"b" - String lateral um binäre Daten zu repräsentaieren 
        payload[b'password'] = [b'test']
        print(payload) 

        # payload wieder in bytes umwandeln
        payload = urllib.parse.urlencode(payload, doseq=True).encode()
        
        # content-length updaten um Fehler password gleiche Länge zu vermieden
        self.headers['Content-Length'] = str(len(payload))

         # manipulierte Request wieder an Server schicken
        req = urllib.request.Request(self.path, data=payload, headers=self.headers, method="POST")
        res = urllib.request.urlopen(req)

        # antwort vom server an client schicken
        self.send_response(res.getcode())
        self.end_headers()
        self.wfile.write(res.read())

# Start HTTP-Server & wartet auf Port 8080 Anfragen
socketserver.TCPServer(('', 8080), MyHTTPRequestHandler).serve_forever()
