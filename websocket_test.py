import tornado.ioloop
from rpc_socket import RPCSocket


class LudumSocket(RPCSocket):
    SAFE_FUNCTIONS = {
        'check_version': 'version',
    }

    def version(self):
        self.js.version('v0.1')

application = tornado.web.Application([
    (r"/", LudumSocket),
])

if __name__ == "__main__":
    application.listen(65456)
    tornado.ioloop.IOLoop.instance().start()
