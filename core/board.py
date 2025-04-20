"""
board.py

This module defines the `Board` class, which represents the game board for a reversed Tic Tac Toe game.
It includes methods for displaying the board, evaluating the game state, updating scores, logging moves,
and resetting the board or scores. The class is designed to handle the core functionality of the game.

Classes:
    - Board: Represents the game board and provides methods for game logic and display.

Dependencies:
    - colorama: Used for colored terminal output.
    - interface.splash: Provides utility functions for displaying ASCII art and patterns.
    - player: Handles saving player progress.

"""

class Board:
    """
    Represents the game board for a reversed Tic Tac Toe game.

    Attributes:
        game (str): The name of the game.
        size (int): The size of the board (e.g., 3 for a 3x3 board).
        players (list[str]): A list of player names.
        logs (list[str]): A list of logs for moves and scores.
        result (str or None): The result of the game (e.g., "YOU WON", "YOU LOST", or "DRAW").
        board (list[list[int or str]]): The current state of the board.
        player_moves (list[int]): A list of tiles occupied by the player.
        player_score (int): The player's current score.
        opponent_moves (list[int]): A list of tiles occupied by the opponent.
        opponent_score (int): The opponent's current score.
    """

    def __init__(self, game:str, size:int, players:list[str]) -> None:
        """
        Initializes the Board instance.

        Args:
            game (str): The name of the game.
            size (int): The size of the board.
            players (list[str]): A list of player names.
        """

        self.game = game
        self.logs = []
        self.result = None

        self.size = size
        self.board = [[col + (size * row) for col in range(1, size + 1)] for row in range(size)]

        self.players = players

        self.player_moves = []
        self.player_score = 0

        self.opponent_moves = []
        self.opponent_score = 0

    def display(self) -> None:
        """
        Displays the game board, score board, and logs in the terminal with formatted output.
        Uses the `colorama` library for colored text.
        """

        from colorama import init, Fore, Style

        init(autoreset=True)

        # Set up board dimensions and formatting
        game_board_width = 87
        score_board_width = 43
        tile_height = 3
        tile_width = (game_board_width - (self.size + 1)) // self.size

        # Functions for formatting the display
        def board_border(char: str, end: str, width: int) -> str:
            """
            Creates a horizontal border for the board.

            Args:
                char (str): The character to use for the border.
                end (str): The end characters for the border.
                width (int): The total width of the border.

            Returns:
                str: The formatted border string.
            """

            return end + (char * (width - (len(end) * 2))) + end

        def tile_border(char: str, end: str) -> str:
            """
            Creates a horizontal border for tiles.

            Args:
                char (str): The character to use for the border.
                end (str): The end characters for the border.

            Returns:
                str: The formatted tile border string.
            """

            return "  " + "".join(char * (tile_width - 2) + end for _ in range(self.size))

        def emphasis(text:str, fore:str) -> str:
            """
            Formats text with color and style.

            Args:
                text (str): The text to format.
                fore (str): The color to apply (e.g., "BLUE", "GREEN").

            Returns:
                str: The formatted text.
            """

            if fore.upper() == "BLUE":
                return f'{Style.BRIGHT}{Fore.BLUE}{text}{Style.RESET_ALL}'
            if fore.upper() == "GREEN":
                return f'{Style.BRIGHT}{Fore.GREEN}{text}{Style.RESET_ALL}'
            if fore.upper() == "RED":
                return f'{Style.BRIGHT}{Fore.RED}{text}{Style.RESET_ALL}'
            if fore.upper() == "YELLOW":
                return f'{Style.BRIGHT}{Fore.YELLOW}{text}{Style.RESET_ALL}'

        # Update the board with player and opponent moves
        for row in self.board:
            for tile in self.player_moves:
                if tile in row:
                    row[row.index(tile)] = "X"
            for tile in self.opponent_moves:
                if tile in row:
                    row[row.index(tile)] = "O"

        # Display the game board and score board headers
        game_board_header = emphasis(text=f'{self.game.upper():^{game_board_width - 2}}', fore="BLUE")
        score_board_header = emphasis(text=f'{"SCORE BOARD":^{score_board_width - 2}}', fore="BLUE")

        print(f'\n{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}')
        print(f'|{game_board_header}|  |{score_board_header}|')
        print(f'{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}')

        # Display the player and opponent scores
        player_score_tracker = emphasis(text=f'{f"{self.players[0]} [X] : {self.player_score}":^{(game_board_width - 3) // 2}}', fore="GREEN")
        opponent_score_tracker = emphasis(text=f'{f"{self.players[1]} [O] : {self.opponent_score}":^{(game_board_width - 3) // 2}}', fore="RED")

        if self.player_score > self.opponent_score:
            leading_tracker = emphasis(text=f'{"Winning : Player [X]":^{score_board_width - 2}}', fore="GREEN")
        elif self.opponent_score > self.player_score:
            leading_tracker = leading_tracker = emphasis(text=f'{"Winning : Opponent [O]":^{score_board_width - 2}}', fore="RED")
        else:
            leading_tracker = emphasis(text=f'{"Draw":^{score_board_width - 2}}', fore="YELLOW")

        print(f'|{player_score_tracker}|{opponent_score_tracker}|  |{leading_tracker}|')
        print(f'{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}\n')

        # Display the logs
        logs_display = [f'{board_border(char="-", end="  ", width=score_board_width)}']

        if not self.logs:
            logs_display.append(f'| -> {"No moves in record.":<{score_board_width - 6}}|')
        else:
            for log in self.logs:
                logs_display.append(f'| -> {log:<{score_board_width - 6}}|')

        log_index = 0

        # Display the game board and logs
        for row in self.board:

            # Top border
            print(f' {tile_border(char="-", end="   ")}', end="")

            if log_index < len(logs_display):
                print(f"  {logs_display[log_index]}")
                log_index += 1
            elif log_index == len(logs_display):
                print(f"  {board_border(char='-', end='  ', width=score_board_width)}")
                log_index += 1
            else:
                print(" " * score_board_width)

            # Display each tile in the row
            for tile_row in range(tile_height):

                # Row border
                row_line = ""

                for tile in row:
                    if tile_row == tile_height // 2:
                        if tile == "X":
                            content = f'{Style.BRIGHT}{Fore.GREEN}{f"{tile:^{tile_width}}"}{Fore.RESET}'
                        elif tile == "O":
                            content = f'{Style.BRIGHT}{Fore.RED}{f"{tile:^{tile_width}}"}{Fore.RESET}'
                        else:
                            content = f"{tile:^{tile_width}}"
                    else:
                        content = " " * tile_width

                    row_line += f"|{content}"

                row_line += "|"
                print(f' {row_line}', end="  ")

                # Log display
                if log_index < len(logs_display):
                    print(f" {logs_display[log_index]}")
                    log_index += 1
                elif log_index == len(logs_display):
                    print(f" {board_border(char='-', end='  ', width=score_board_width)}")
                    log_index += 1
                else:
                    print(" " * score_board_width)

        # Bottom border
        print(f' {tile_border(char="-", end="   ")}\n')

    def evaluate_board(self, in_turn_symbol:str) -> bool:
        """
        Evaluates the current state of the board to check for a win or draw.

        Args:
            in_turn_symbol (str): The symbol of the player whose turn it is ("X" or "O").

        Returns:
            bool: True if the game is over (win or draw), False otherwise.
        """

        # Horizontal
        for row in self.board:
            if all(cell == in_turn_symbol for cell in row):
                return True

        # Vertical
        for col in range(len(self.board)):
            if all(row[col] == in_turn_symbol for row in self.board):
                return True

        # Diagonal - Left
        if all(self.board[i][i] == in_turn_symbol for i in range(len(self.board))):
            return True

        # Diagonal - Right
        if all(self.board[i][len(self.board) - 1 - i] == in_turn_symbol for i in range(len(self.board))):
            return True

        # No Spaces Left
        return all(isinstance(tile, str) for row in self.board for tile in row)

    def evaluate_points(self):
        """
        Evaluates the final points and displays the result using ASCII art.
        """

        from interface.splash import line, ascii

        if self.player_score > self.opponent_score:
            win_text = "YOU WON"
            win_fore = "GREEN"
            win_pattern = "X-"
        elif self.player_score < self.opponent_score:
            win_text = "YOU LOST"
            win_fore = "RED"
            win_pattern = "O-"
        else:
            win_text = "DRAW"
            win_fore = "YELLOW"
            win_pattern = "X-O-"

        self.result = win_text

        line(fore=win_fore, pattern=win_pattern)
        ascii(text=win_text, fore=win_fore)
        self.display()
        line(fore=win_fore, pattern=win_pattern)

    def update_score(self, time:float) -> int:
        """
        Updates the score based on the time taken for a move.

        Args:
            time (float): The time taken for the move in seconds.

        Returns:
            int: The points awarded for the move.
        """

        if time <= 2:
            return 10

        elif time <= 5:
            return 5

        else:
            return 1

    def log_score(self, player:str, points:int, move:int) -> None:
        """
        Logs the score for a move.

        Args:
            player (str): The name of the player.
            points (int): The points awarded.
            move (int): The tile number of the move.
        """

        if move is None:
            self.logs.append(f'{player.upper():10} : +{points:02d} bonus points')
        else:
            self.logs.append(f'{player.upper():10} : +{points:02d} points on tile {move}')

    def log_board(self):
        """
        Saves the current board state and result using the Player module.
        """

        from .settings import player
        player.save_progress(board=self.board, result=self.result, score=self.player_score)

    def reset_board(self) -> None:
        """
        Resets the board to its initial state.
        """

        self.player_moves.clear()
        self.opponent_moves.clear()
        self.logs.clear()
        self.result = None
        self.board = [[col + (self.size * row) for col in range(1, self.size + 1)] for row in range(self.size)]

    def reset_score(self) -> None:
        """
        Resets the scores for both players.
        """

        self.player_score = 0
        self.opponent_score = 0

    def reset_all(self) -> None:
        """
        Resets both the board and the scores.
        """

        self.reset_score()
        self.reset_board()
