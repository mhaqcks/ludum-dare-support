from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process
import urllib
import json
import ssl
import urlparse

# Warn about monkey in the middle attacks.


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
    def do_GET(self):
        print(self.path)
        if self.path.startswith('/?'):
            self.wfile.write('jsonCallback({0});'.format(json.dumps(test)))
            self.wfile.write('\n')
            self.wfile.write(urlparse.parse_qs(urlparse.urlparse(self.path).query))
            # self.wfile.write(urlparse.parse_qs(urllib.unquote(self.path[2:])))
        else:
            self.wfile.write("No Command Recieved!\nI'll just wait here.")

def rpc_server():

    server = HTTPServer((HOST, PORT), Handler)
    # SSL
    server.socket = ssl.wrap_socket(server.socket, certfile='./server.pem', server_side=True)

    server.serve_forever()

def main():
    p = Process(target=rpc_server)
    p.start()

    p.join()


if __name__ == '__main__':
    main()
