from twisted.internet import protocol, reactor
import logging
import json


class NetworkObject(object):
    def __init__(self, n_id=None):
        self.n_id = n_id if n_id is not None else id(self)



class NetClient(protocol.Protocol):
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
        else:
            logging.debug(data)

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
    connect(c)

