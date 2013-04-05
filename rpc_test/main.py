from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib
import json
import ssl
import urlparse


class RPCHandler(BaseHTTPRequestHandler):

    functions = {}

    def do_GET(self):
        print(self.path)
        if self.path.startswith('/?'):
            query = urlparse.urlparse(self.path).query

            variables = {}
            for statement in query.split('&'):
                name, value = statement.split('=', 1)
                variables[name] = value

            output = json.loads(urllib.unquote(variables['json']))

            if output['method'] not in self.functions:
                self.wfile.write('This command has not been deemed safe by the overlords!')
            else:
                reply = self.functions[output['method']](**output['args'])
                self.wfile.write('jsonCallback({0})'.format(json.loads(reply)))

        else:
            self.wfile.write("No Command Recieved!\nI'll just wait here.")


class LudumProcedureCallServer(object):
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
            self.server.socket, certfile=self.certfile, server_side=True)

        self.server.serve_forever()


def connect(host, port, game_number):
    print(host, port, game_number)

# Warn about monkey in the middle attacks.
if __name__ == '__main__':
    HOST = 'localhost'
    # 1 - 65535
    PORT = 65456

    rpc = LudumProcedureCallServer(HOST, PORT)

    rpc.register_function(connect)

    rpc.start()
