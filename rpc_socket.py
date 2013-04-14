from __future__ import print_function
from tornado import websocket
import json

def proxy_factory(socket, func):
    def proxy_call(*args):
        socket.rpc(func, *args)

    return proxy_call


class JavaScriptCaller(object):
    def __init__(self, socket):
        self.socket = socket

    def __getattr__(self, attr):
        return proxy_factory(self.socket, attr)

class RPCSocket(websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(RPCSocket, self).__init__(*args, **kwargs)
        self.js = JavaScriptCaller(self)

        self.SAFE_FUNCTIONS['help'] = 'help'

    def help(self, func=None):
        pass

    def rpc(self, func, *args):
        self.write_message(
            json.dumps({
                'func': func,
                'args': args
                }))

    def open(self):
        print("WebSocket opened")

    def call_command(self,   message):
        cmd_info = json.loads(message)

        try:
            f = getattr(self, self.SAFE_FUNCTIONS[cmd_info['func']])
        except KeyError:
            return

        args = cmd_info.get('args', {})
        f(**args)

    def on_message(self, message):
        self.call_command(message)

    def on_close(self):
        print("WebSocket closed")
