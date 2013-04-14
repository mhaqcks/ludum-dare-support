import tornado.ioloop
from rpc_socket import RPCSocket
import random


class LudumSocket(RPCSocket):
    SAFE_FUNCTIONS = {
        'check_version': 'version',
    }

    def version(self):
        v = random.randint(0, 1)
        print(v)
        if v:
            self.js.version('v0.01')
        else:
            self.js.version('v0.02')

application = tornado.web.Application([
    (r"/", LudumSocket),
])

if __name__ == "__main__":
    application.listen(65456)
    tornado.ioloop.IOLoop.instance().start()
