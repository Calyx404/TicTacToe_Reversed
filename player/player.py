class Player:
    def __init__(self, uid, username, password, wins=0, losses=0, fastest_move=0.0, highest_point=0, current_streak=0, best_streak=0):
        self.uid = uid
        self.username = username
        self.password = password
        self.wins = wins
        self.losses = losses
        self.win_rate = self.calculate_win_rate()
        self.fastest_move = fastest_move
        self.highest_point = highest_point
        self.current_streak = current_streak
        self.best_streak = best_streak

    def calculate_win_rate(self):
        total_games = self.wins + self.losses
        return round(self.wins / total_games, 2) if total_games > 0 else 0

    def to_dict(self):
        return {
            "uid": self.uid,
            "username": self.username,
            "password": self.password,
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": self.win_rate,
            "fastest_move": self.fastest_move,
            "highest_point": self.highest_point,
            "current_streak": self.current_streak,
            "best_streak": self.best_streak
        }

    @staticmethod
    def from_dict(data):
        return Player(**data)
