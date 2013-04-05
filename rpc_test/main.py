from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process
import urllib
import json
import socket, os
from SocketServer import BaseServer
from OpenSSL import SSL


class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        #server.pem's location (containing the server private key and
        #the server certificate).
        fpem = './server.pem'
        ctx.use_privatekey_file (fpem)
        ctx.use_certificate_file(fpem)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,
                                                        self.socket_type))
        self.server_bind()
        self.server_activate()

HOST = 'localhost'
# 1 - 65535
PORT = 65456

def connect(host, port, game_number):
    print(host, port, game_number)

test = {
    'a': 3231,
}

class Handler(BaseHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, "rb", self.rbufsize)
        self.wfile = socket._fileobject(self.request, "wb", self.wbufsize)

    def do_GET(self):
        print(self.path)
        if self.path.startswith('/?'):
            self.wfile.write('jsonCallback({0});'.format(json.dumps(test)))
            #self.wfile.write(urllib.unquote(self.path[2:]))
        else:
            self.wfile.write("No Command Recieved!\nI'll just wait here.")

def rpc_server():

    server = SecureHTTPServer((HOST, PORT), Handler)

    server.serve_forever()

def main():
    p = Process(target=rpc_server)
    p.start()

    p.join()


if __name__ == '__main__':
    main()
