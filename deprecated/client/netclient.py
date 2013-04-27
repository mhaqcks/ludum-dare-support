from twisted.internet import protocol, reactor
import logging
import json


class NetworkObject(object):
    def __init__(self, client, n_id=None):
        self.client = client
        self.n_id = n_id if n_id is not None else id(self)

        if not n_id:
            self.client.add_object(self)

    def net_friendly(self):
        return {'__classname__': type(self).__name__, 'n_id': self.n_id}

    def remove(self):
        self.client.del_object(self)

def malleable(name):
    def set_obj(self, value):
        setattr(self, 'malleable_{0}'.format(name), value)
        self.client.change(self, name, value)

    def get_obj(self):
        return getattr(self, 'malleable_{0}'.format(name))

    return property(get_obj, set_obj)


class TestObject(NetworkObject):
    x = malleable('x')


class NetClient(protocol.Protocol):
    def __init__(self):
        self.game_objects = []
        self.clear_delta()

    def clear_delta(self):
        self.delta = {
            'added': [],
            'removed': [],
            'changed': {}
        }

    def connectionMade(self):
        logging.debug('Connection Made...')
        self.transport.write(json.dumps({
            'command': 'join',
            'args': {'code': 'test-game'}
            }))


    def connectionLost(self, reason):
        logging.debug('Connection Lost: {0}'.format(reason))

    def dataReceived(self, data):
        info = json.loads(data)
        if info['command'] == 'error':
            logging.error('Server Response: {0}'.format(info['args']['message']))
        elif info['command'] == 'update':
            delta = info['args']['delta']

            for a in delta['added']:
                o = getattr(globals(), a['__classname__'])(a[n_id])

                del a['__classname__']
                self.update(a)

            for r in delta['removed']:
                for g in game_objects:
                    if g.n_id == r:
                        del g
                        break

            for u in delta['update']:
                self.update(u)

        else:
            logging.debug(data)

    def update(self, data):
        obj = [o for o in self.game_objects if o.n_id == data['n_id']][0]

        del data['n_id']
        for key, value in data.iteritems():
            setattr(obj, 'malleable_{0}'.format(key), value)

    def add_object(self, obj):
        self.game_objects += [obj]

        self.delta['added'] = obj.net_friendly()
        pass

    def del_object(self, obj):
        logging.debug(obj)

        self.delta['removed'] += [obj.n_id]
        print([id(x) for x in self.game_objects])
        self.game_objects.remove(obj)

    def change(self, obj, key, value):

        if obj.n_id not in self.delta['changed']:
            self.delta['changed'][obj.n_id] = {}

        self.delta['changed'][obj.n_id][key] = value


    def send_delta(self):
        logging.debug(self.delta)
        self.clear_delta()

class GameClientFactory(protocol.ClientFactory):
    def __init__(self, client):
        self.client = client

    def startedConnecting(self, connector):
        logging.debug('Started Connecting...')

    def clientConnectionLost(self, connector, reason):
        logging.debug('Lost connection: {0}'.format(reason))

    def clientConnectionFailed(self, connector, reason):
        logging.debug('Connection Failed: {0}'.format(reason))


    def buildProtocol(self, addr):
        logging.debug('Building Protocol...')
        return self.client


def connect(client):
    reactor.connectTCP('localhost', 8675, GameClientFactory(client))
    reactor.run()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    c = NetClient()

    o = TestObject(c)

    c.send_delta()
    o.remove()
    c.send_delta()
    o.x = 21
    c.send_delta()

    connect(c)

