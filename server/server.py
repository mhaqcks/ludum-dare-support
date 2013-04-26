from twisted.internet import protocol, reactor
from word_list import word_list
import logging
import random
import json

logging.basicConfig(level=logging.DEBUG)

def create_game(self, games, name, max_players=5, password=''):
    code = random.sample(set(word_list) - set([g.password for g in games]), 1)
    g = Game(code, password, create_game.number, name, max_players)

    create_game.number += 1

    games += [g]
    return g
create_game.number = 0

def connect(games, game_number, password=''):
    game = None
    for g in games:
        if g.number == int(game_number):
            if g.password != password:
                return {'Error': 'Invalid Password!'}
            else:
                return {'Success': g.code}


class Game(object):
    def __init__(self, code, password, number, name, max_players=5):
        self.code = code
        self.password = password
        self.name = name
        self.max_players = max_players
        self.number = number
        self.clients = {}

    def add_client(self, client):
        self.clients[id(client)] = client

    def drop_client(self, client):
        del self.clients[id(client)]
        return len(self.clients) > 0


class GameProtocol(protocol.Protocol):
    def __init__(self, games):
        self.games = games
        self.current_game = None

    def connectionMade(self):
        logging.debug('Connection Made...')

    def connectionLost(self, reason):
        logging.debug('Connection Lost...')

        if self.current_game:
            if not self.current_game.drop_client(self):
                del self.games[id(self.current_game)]

        # Otherwise, we never connected to a game anyway. Lulz

    def dataReceieved(self, data):
        pass


class GameFactory(protocol.Factory):
    def __init__(self, games):
        self.games = games

    def buildProtocol(self, addr):
        return GameProtocol(self.games)

def build_list(games, game_number, game_name, players, status, locked):
    # Does all the necessary filtering

    if game_number:
        game_number = int(game_number)
        for g in games:
            if g.number == game_number:
                games = [g]
                break

    rows = []

    if game_name:
        for g in games:
            if game_name.lower() in g.name.lower():
                rows += [g]

        games = rows

    rows = []
    if players.lower() == 'hide full games':
        for g in games:
            n, m = len(g.clients), g.max_players
            if len(g.clients) < g.max_players:
                rows += [g]

        games = rows

    rows = []
    if locked.lower() != 'all':
        for g in games:
            if locked.lower() == 'public' and not g.password:
                rows += [g]
            elif locked.lower() == 'private' and g.password:
                rows += [g]

        games = rows

    return games

class ServerGameProtocol(protocol.Protocol):
    def __init__(self, games):
        self.games = games

    def dataReceived(self, data):
        logging.debug(data)
        info = json.loads(data)

        if info['command'] == 'new_game':
            create_game(self.games, **info['args'])
        elif info['command'] == 'list':
            game_list = build_list(self.games, **info['args'])
            self.transport.write(json.dumps(game_list))
        elif info['command'] == 'connect':
            response = connect(self.games, **info['args'])
            self.transport.write(json.dumps(response))


class ServerGameFactory(protocol.Factory):
    def __init__(self, games):
        self.games = games

    def buildProtocol(self, addr):
        return ServerGameProtocol(self.games)


def main():
    games = []
    reactor.listenTCP(8675, GameFactory(games))
    reactor.listenTCP(5768, ServerGameFactory(games))
    reactor.run()

if __name__ == '__main__':
    logging.debug('Listening...')
    main()
