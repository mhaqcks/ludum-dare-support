from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process
import urllib
import json

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
            #self.wfile.write(urllib.unquote(self.path[2:]))
        else:
            self.wfile.write("No Command Recieved!\nI'll just wait here.")

def rpc_server():

    server = HTTPServer((HOST, PORT), Handler)

    server.serve_forever()

def main():
    p = Process(target=rpc_server)
    p.start()

    p.join()


if __name__ == '__main__':
    main()
