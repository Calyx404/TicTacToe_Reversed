class player:
    def __init__(self, uid, username, password, wins = 0, losses = 0, fastest_move = 0, highest_point = 0, current_streak = 0, best_streak = 0):
        self.uid = uid,
        self.username = username,
        self.password = password,
        self.wins = wins,
        self.losses = losses,
        self.win_rate = wins / (wins + losses)
        self.fastest_move = fastest_move,
        self.highest_point = highest_point,
        self.current_streak = current_streak,
        self.best_streak = best_streak
