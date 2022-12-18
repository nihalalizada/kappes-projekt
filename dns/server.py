import socketserver
from dnslib import DNSRecord, DNSHeader, DNSQuestion, A, QTYPE

class MyDNSHandler(socketserver.BaseRequestHandler):
    def get_ip_address(self, domain_name):
        # Look up the IP address for the domain name
        # (replace this with your own code to resolve the domain name)
        if domain_name == 'google.com':
            return '192.168.178.56'
        else:
            # If the IP address is not available in the local records,
            # use the Google DNS server to resolve the domain name
            dns_resolver = '8.8.8.8'
            dns_request = DNSRecord(DNSHeader(id=1, qr=0, aa=0, ra=0), q=DNSQuestion(domain_name, getattr(QTYPE, 'A'), 1))
            dns_response_bytes = dns_request.send(dns_resolver, 53)
            dns_response = DNSRecord.parse(dns_response_bytes)
            return dns_response.a.rdata

    def handle(self):
        # Receive the DNS query
        data = self.request[0].strip()
        dns_request = DNSRecord.parse(data)

        # Extract the domain name from the DNS query
        domain_name = str(dns_request.q.qname)

        # Look up the IP address for the domain name
        ip_address = self.get_ip_address(domain_name)

        # Construct the DNS response with the IP address
        dns_response = DNSRecord(DNSHeader(id=dns_request.header.id, qr=1, aa=1, ra=1), q=dns_request.q)
        dns_response.add_answer(DNSQuestion(domain_name, getattr(QTYPE, 'A'), 1))

        # Send the DNS response
        self.request[1].sendto(dns_response.pack(), self.client_address)

# Start the DNS server
socketserver.UDPServer(('', 53), MyDNSHandler).serve_forever() #Port auf Windows wird schon benutzt
