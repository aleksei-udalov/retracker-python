#!/usr/bin/python2
# see https://habrahabr.ru/post/96880/
# see https://wiki.theory.org/BitTorrent_Tracker_Protocol#Response_Format

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import struct
from bencode.bencode import bencode

peers = dict()

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        request = parse_qs(urlparse(self.path).query)
        hash = request['info_hash'][0]
        ip = self.client_address[0]
        port = request['port'][0]
        if hash in peers:
            if (ip, port) not in peers[hash]:
                peers[hash].append((ip, port))
        else:
            peers[hash] = [(ip, port),]

        print peers
        prepared_peers = ''
        for p in peers[hash]:
            prepared_peers += ''.join(map(chr, map(int, p[0].split('.'))))
            prepared_peers += struct.pack('>H', int(p[1]))
        response = bencode({'interval': 60, 'peers': prepared_peers})
        print response
        self.wfile.write(response)

s = HTTPServer(('0.0.0.0', 8888), HttpProcessor)
s.serve_forever()
