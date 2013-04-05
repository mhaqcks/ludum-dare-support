from SimpleXMLRPCServer import SimpleXMLRPCServer
from multiprocessing import Process

HOST = 'localhost'
# 1 - 65535
PORT = 65456

def connect(host, port, game_number):
    print(host, port, game_number)

def rpc_server():
    server = SimpleXMLRPCServer((HOST, PORT))

    server.register_introspection_functions()
    server.register_function(connect)
    server.serve_forever()

def main():
    p = Process(target=rpc_server)
    p.start()

    p.join()


if __name__ == '__main__':
    main()
