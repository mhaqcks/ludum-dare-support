from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from multiprocessing import Process
import urllib
import json
import ssl
import urlparse


class RPCHandler(BaseHTTPRequestHandler):

    functions = {}

    def do_GET(self):
        print(self.path)
        if self.path.startswith('/?'):
            self.wfile.write('jsonCallback({0});'.format(json.dumps(test)))
            self.wfile.write('\n')
            query = urlparse.urlparse(self.path).query

            variables = {}
            for statement in query.split('&'):
                name, value = statement.split('=', 1)
                variables[name] = value

            output = json.loads(urllib.unquote(variables['json']))

            if output['method'] not in self.functions:
                self.wfile.write('This command has not been deemed safe by the overlords!')
            else:
                self.functions[output['method']](**output['args'])
                self.wfile.write(output)

        else:
            self.wfile.write("No Command Recieved!\nI'll just wait here.")


class LudumProcedureCallServer(self):
    def __init__(self, host, port, certfile='./server.pem'):
        self.host = host
        self.port = port
        self.certfile = certfile
        self.functions = {}
        self.handler = RPCHandler

    def register_function(self, function, function_name=None):
        if function_name is None:
            function_name = function.__name__

        self.handler.functions[function_name] = function

    def start(self):
        self.server = HTTPServer((self.host, self.port), self.handler)
        # SSL
        self.server.socket = ssl.wrap_socket(
            server.socket, certfile=self.certfile, server_side=True)

        self.server.serve_forever()

# Warn about monkey in the middle attacks.
if __name__ == '__main__':
    HOST = 'localhost'
    # 1 - 65535
    PORT = 65456

    rpc = LudumProcedureCallServer(HOST, PORT)
