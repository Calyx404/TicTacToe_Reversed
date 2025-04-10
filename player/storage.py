import json
import os
from player.player import Player

class PlayerStorage:
    def __init__(self, filepath='players.json'):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump([], f)

    def load_players(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            return [Player.from_dict(p) for p in data]

    def save_players(self, players):
        with open(self.filepath, 'w') as f:
            json.dump([p.to_dict() for p in players], f, indent=4)

    def add_player(self, player):
        players = self.load_players()
        players.append(player)
        self.save_players(players)

    def find_by_username(self, username):
        for p in self.load_players():
            if p.username == username:
                return p

        return None
