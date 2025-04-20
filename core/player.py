"""
player.py

This module defines the `Player` class, which manages player-related functionality for the reversed Tic Tac Toe game.
It includes methods for account management (sign-in, sign-up, sign-out), saving and resetting progress,
updating preferences, managing achievements, and displaying player profiles.

Classes:
    - Player: Represents a player and provides methods for managing player data and interactions.

Dependencies:
    - services.db_handler: Handles database operations such as loading and saving player data.
    - services.log_handler: Logs player activities and errors.
    - interface.splash: Provides utility functions for user interaction.
    - colorama: Used for colored terminal output.

"""

class Player:
    """
    Represents a player in the reversed Tic Tac Toe game.

    Attributes:
        username (str): The player's username.
        password (str or None): The player's password.
        logged_in (bool): Indicates whether the player is logged in.
        wins (int): The number of games the player has won.
        losses (int): The number of games the player has lost.
        draws (int): The number of games that ended in a draw.
        total_games (int): The total number of games played.
        best_streak (int): The player's best winning streak.
        current_streak (int): The player's current winning streak.
        top_score (int): The player's highest score.
        grid_size (int): The preferred grid size for the game.
        time_limit (int): The time limit for each move in seconds.
        first_move (int): Indicates whether the player prefers to go first.
        history (list[dict]): A list of the player's game history.
    """

    def __init__(self):
        """
        Initializes a new Player instance with default values and ensures the database file exists.
        """

        from services.db_handler import _check_file

        _check_file()

        # Identity
        self.username = "Player"
        self.password = None
        self.logged_in = False

        # Statistics
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.total_games = self.wins + self.losses + self.draws

        # Achievements
        self.best_streak = 0
        self.current_streak = 0
        self.top_score = 0

        # Preferences
        self.grid_size = 3
        self.time_limit = 60
        self.first_move = 0

        # History
        self.history = []

    def sign_in(self, username:str, password:str) -> None:
        """
        Signs the player into their account.

        Args:
            username (str): The player's username.
            password (str): The player's password.

        Raises:
            ValueError: If the account does not exist or the password is incorrect.
        """

        from services.log_handler import log
        from services.db_handler import _load_data

        data = _load_data()

        if username not in data:
            log(level="ERROR", activity=f"Failed to load user account: username='{username}' does not exist.")
            raise ValueError("Account does not exist")

        if data[username].get("password", "") != password:
            log(level="WARNING", activity=f"Invalid sign-in attempt: username='{username}', reason='Incorrect password'.")
            raise ValueError("Username and password do not match")

        # Identity
        self.username = username
        self.password = password
        self.logged_in = True

        # Statistics
        stats = data[username].get("statistics", {})
        self.wins = stats.get("wins", 0)
        self.losses = stats.get("losses", 0)
        self.draws = stats.get("draws", 0)
        self.total_games = stats.get("total_games", self.wins + self.losses + self.draws)

        # Achievements
        achieves = data[username].get("achievements", {})
        self.best_streak = achieves.get("best_streak", 0)
        self.current_streak = achieves.get("current_streak", 0)
        self.top_score = achieves.get("top_score", 0)

        # Preferences
        prefs = data[username].get("preferences", {})
        self.grid_size = prefs.get("grid_size", 3)
        self.time_limit = prefs.get("time_limit", 60)
        self.first_move = prefs.get("first_move", 0)

        # History
        self.history = data[username].get("history", [])

        log(level="INFO", activity=f"Sign-in attempt: username='{self.username}'.")
        log(level="INFO", activity=f"Session started: username='{self.username}'.")

    def sign_up(self, username:str, password:str) -> None:
        """
        Creates a new player account.

        Args:
            username (str): The desired username.
            password (str): The desired password.

        Raises:
            ValueError: If the username already exists.
        """

        from services.log_handler import log
        from services.db_handler import _load_data, _save_data

        data = _load_data()

        if username in data:
            log(level="Error", activity=f"Failed to load user account: username='{username}' already exists.")
            raise ValueError("Username already exists")

        data[username] = {
            "password": password,
            "statistics": {
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "total_games": 0
            },
            "achievements": {
                "best_streak": 0,
                "current_streak": 0,
                "top_score": 0
            },
            "preferences": {
                "grid_size": 3,
                "time_limit": 60,
                "first_move": 0
            },
            "history": []
        }

        _save_data(data=data)
        log(level="INFO", activity=f"Account successfully created: username='{username}'.")

    def sign_out(self) -> None:
        """
        Signs the player out of their account and resets their session data.
        """

        from services.log_handler import log

        self.username = "Player"
        self.password = None
        self.logged_in = False

        log(level="INFO", activity=f"Sign-out attempt: username='{self.username}'.")
        log(level="INFO", activity=f"Session terminated: username='{self.username}'.")

    def save_progress(self, board: list[list], result: str, score: int) -> None:
        """
        Saves the player's game progress, including statistics, achievements, and history.

        Args:
            board (list[list]): The final state of the game board.
            result (str): The result of the game ("YOU WON", "YOU LOST", or "DRAW").
            score (int): The player's score for the game.
        """

        if self.logged_in:
            from datetime import datetime
            from services.log_handler import log
            from services.db_handler import _load_data, _save_data

            # Update Statistics
            if result.upper() == "YOU WON":
                self.wins += 1
            elif result.upper() == "YOU LOST":
                self.losses += 1
            elif result.upper() == "DRAW":
                self.draws += 1

            self.total_games = self.wins + self.losses + self.draws

            # Update History
            self.history.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "board": board,
                "result": result,
                "score": score
            })

            # Update Achievements
            for record in self.history:
                result = record.get("result", "").upper()
                score = record.get("score", 0)

                if result == "YOU WON":
                    self.current_streak += 1
                    self.best_streak = max(self.best_streak, self.current_streak)
                else:
                    self.current_streak = 0

                if score > self.top_score:
                    self.top_score = score

            data = _load_data()

            # Save Progress
            data[self.username]["statistics"] = {
                "wins": self.wins,
                "losses": self.losses,
                "draws": self.draws,
                "total_games": self.total_games
            }

            data[self.username]["achievements"] = {
                "best_streak": self.best_streak,
                "current_streak": self.current_streak,
                "top_score": self.top_score
            }

            data[self.username]["history"] = self.history

            _save_data(data=data)
            log(level="INFO", activity=f"Progress successfully saved: username='{self.username}'.")

    def reset_progress(self) -> None:
        """
        Resets the player's progress, including statistics, achievements, and history.
        """

        from services.log_handler import log
        from services.db_handler import _load_data, _save_data

        # Statistics
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.total_games = 0

        # Achievements
        self.best_streak = 0
        self.current_streak = 0
        self.top_score = 0

        # History
        self.history = []

        data = _load_data()

        # Save Progress
        data[self.username]["statistics"] = {
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
            "total_games": self.total_games
        }

        data[self.username]["achievements"] = {
            "best_streak": self.best_streak,
            "current_streak": self.current_streak,
            "top_score": self.top_score
        }

        data[self.username]["history"] = self.history

        _save_data(data=data)
        log(level="INFO", activity=f"Progress successfully saved: username='{self.username}'.")

    def save_preferences(self, grid_size:int = None, time_limit:int = None, first_move:int = None) -> None:
        """
        Saves the player's game preferences.

        Args:
            grid_size (int, optional): The preferred grid size.
            time_limit (int, optional): The time limit for each move in seconds.
            first_move (int, optional): Indicates whether the player prefers to go first.
        """

        if grid_size:
            self.grid_size = grid_size

        if time_limit:
            self.time_limit = time_limit

        if first_move:
            self.first_move = first_move

        if self.logged_in:
            from services.log_handler import log
            from services.db_handler import _load_data, _save_data

            data = _load_data()

            # Save Preferences
            data[self.username]["preferences"] = {
                "grid_size": self.grid_size,
                "time_limit": self.time_limit,
                "first_move": self.first_move
            }

            _save_data(data=data)
            log(level="INFO", activity=f"Preferences successfully saved: username='{self.username}'.")

    def reset_preferences(self) -> None:
        """
        Resets the player's preferences to default values.
        """

        # Preferences
        self.grid_size = 3
        self.time_limit = 60
        self.first_move = 0

        self.save_preferences(grid_size=self.grid_size, time_limit=self.time_limit, first_move=self.first_move)

    def delete_account(self, username:str) -> None:
        """
        Deletes the player's account from the database.

        Args:
            username (str): The username of the account to delete.

        Raises:
            ValueError: If the account does not exist.
        """

        from services.log_handler import log
        from services.db_handler import _load_data, _save_data

        data = _load_data()

        if username not in data:
            log(level="Error", activity=f"Failed to delete user account: username='{username}' does not exists.")
            raise ValueError("Account does not exists")

        # Delete Account
        del data[username]

        _save_data(data=data)
        log(level="INFO", activity=f"Account successfully deleted: username='{username}'.")

    def update_profile(self, old_username:str, new_username:str = None, new_password:str = None) -> None:
        """
        Updates the player's profile information.

        Args:
            old_username (str): The current username.
            new_username (str, optional): The new username.
            new_password (str, optional): The new password.
        """

        from services.log_handler import log
        from services.db_handler import _load_data, _save_data

        data = _load_data()

        if new_username:
            self.username = new_username
            data[new_username] = data.pop(old_username)

        if new_password:
            self.password = new_password
            data[new_username or old_username]["password"] = new_password

        _save_data(data=data)
        log(level="INFO", activity=f"Profile successfully updated: username='{self.username}'.")

    def display_profile(self) -> None:
        """
        Displays the player's profile, including identity, statistics, and achievements.
        """

        from colorama import init, Fore, Style
        from interface.splash import wait

        init(autoreset=True)

        term_width = 134
        center = lambda text: f"{text:^{term_width - 2}}"
        left = lambda text, indent: f"{text:{term_width - (indent + 1)}}"
        highlight = lambda text: f"{Fore.BLUE}{text}{Fore.RESET}"

        if self.logged_in:

            print(f"""{Style.BRIGHT}
  ----------------------------------------------------------------------------------------------------------------------------------
|{highlight(text=center(text="PLAYER PROFILE"))}|
  ----------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 👤 Player Identity                                                                                                                 |
|                                                                                                                                    |
|    🆔 {highlight(text="Username")}       : {left(text=self.username, indent=25)}|
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
            """)

            wait(key=b' ', name="space", action="view more", end="\r")

            print(f"""{Style.BRIGHT}  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 📈 Player Statistics                                                                                                               |
|                                                                                                                                    |
|    ✅ {highlight(text="Wins")}           : {left(text=self.wins, indent=25)}|
|    ❌ {highlight(text="Losses")}         : {left(text=self.losses, indent=25)}|
|    ⚖️ {highlight(text="Draws")}          : {left(text=self.draws, indent=25)}|
|    🧠 {highlight(text="Total Games")}    : {left(text=self.total_games, indent=25)}|
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
            """)

            wait(key=b' ', name="space", action="view more", end="\r")

            print(f"""{Style.BRIGHT}  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🌟 Achievements                                                                                                                    |
|                                                                                                                                    |
|    🏅 {highlight(text="Best Streak")}    : {left(text=self.best_streak, indent=25)}|
|    💯 {highlight(text="Current Streak")} : {left(text=self.current_streak, indent=25)}|
|    🗓️ {highlight(text="Top Score")}      : {left(text=self.top_score, indent=25)}|
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
            """)

            wait(key=b'\r', name="enter", action="go back to main menu")

        else:

            warning = lambda text: f"{Fore.RED}{text}{Fore.RESET}"

            print(f"""{Style.BRIGHT}
  ----------------------------------------------------------------------------------------------------------------------------------
|{highlight(text=center(text="PLAYER PROFILE"))}|
  ----------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| ❌ {warning(text=left(text="Nothing to view. First, create or sign your account in settings.", indent=5))}|
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
            """)

            wait(key=b'\r', name="enter", action="go back to main menu", end="\r")
