import tornado.ioloop
from tornado import websocket


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print(message)
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


application = tornado.web.Application([
    (r"/", EchoWebSocket),
])

if __name__ == "__main__":
    application.listen(65456)
    tornado.ioloop.IOLoop.instance().start()
