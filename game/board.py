class Board:
    def __init__(self, game:str, size:int, players:list[str]) -> None:
        self.game = game
        self.size = size
        self.board = [[col + (size * row) for col in range(1, size + 1)] for row in range(size)]
        self.players = players
        self.player_moves = []
        self.opponent_moves = []
        self.player_score = 0
        self.opponent_score = 0
        self.logs = []
        self.result = None

    def display(self) -> None:
        # Imports
        from colorama import init, Fore, Style

        init(autoreset=True)

        # Configuration
        game_board_width = 87
        score_board_width = 43
        tile_height = 3
        tile_width = (game_board_width - (self.size + 1)) // self.size

        # Border helpers
        def board_border(char: str, end: str, width: int) -> str:
            return end + (char * (width - (len(end) * 2))) + end

        def tile_border(char: str, end: str) -> str:
            return "  " + "".join(char * (tile_width - 2) + end for _ in range(self.size))

        def emphasis(text:str, fore:str) -> str:
            if fore.upper() == "BLUE":
                return f'{Style.BRIGHT}{Fore.BLUE}{text}{Style.RESET_ALL}'
            if fore.upper() == "GREEN":
                return f'{Style.BRIGHT}{Fore.GREEN}{text}{Style.RESET_ALL}'
            if fore.upper() == "RED":
                return f'{Style.BRIGHT}{Fore.RED}{text}{Style.RESET_ALL}'
            if fore.upper() == "YELLOW":
                return f'{Style.BRIGHT}{Fore.YELLOW}{text}{Style.RESET_ALL}'

        # Replace tiles with player and opponent symbols
        for row in self.board:
            for tile in self.player_moves:
                if tile in row:
                    row[row.index(tile)] = "X"
            for tile in self.opponent_moves:
                if tile in row:
                    row[row.index(tile)] = "O"

        # Header
        game_board_header = emphasis(text=f'{self.game:^{game_board_width - 2}}', fore="BLUE")
        score_board_header = emphasis(text=f'{"SCORE BOARD":^{score_board_width - 2}}', fore="BLUE")

        print(f'\n{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}')
        print(f'|{game_board_header}|  |{score_board_header}|')
        print(f'{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}')

        # Tracker
        player_score_tracker = emphasis(text=f'{f"Player [X] : {self.player_score}":^{(game_board_width - 3) // 2}}', fore="GREEN")
        opponent_score_tracker = emphasis(text=f'{f"Opponent [O] : {self.opponent_score}":^{(game_board_width - 3) // 2}}', fore="RED")

        if self.player_score > self.opponent_score:
            leading_tracker = emphasis(text=f'{"Winning : Player [X]":^{score_board_width - 2}}', fore="GREEN")
        elif self.opponent_score > self.player_score:
            leading_tracker = leading_tracker = emphasis(text=f'{"Winning : Opponent [O]":^{score_board_width - 2}}', fore="RED")
        else:
            leading_tracker = emphasis(text=f'{"Draw":^{score_board_width - 2}}', fore="YELLOW")

        print(f'|{player_score_tracker}|{opponent_score_tracker}|  |{leading_tracker}|')
        print(f'{board_border(char="-", end="  ", width=game_board_width)}  {board_border(char="-", end="  ", width=score_board_width)}\n')

        # Score Logs
        logs_display = [f'{board_border(char="-", end="  ", width=score_board_width)}']

        if not self.logs:
            logs_display.append(f'| -> {"No moves in record.":<{score_board_width - 6}}|')
        else:
            for log in self.logs:
                logs_display.append(f'| -> {log:<{score_board_width - 6}}|')

        log_index = 0

        # Main Boards
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

            # Contents
            for tile_row in range(tile_height):

                # Game Board
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

                # Score Board
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

    def evaluate(self, in_turn:str, in_turn_symbol:str) -> bool:
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

    def update_score(self, time:float) -> int:
        if time <= 2:
            return 10

        elif time <= 5:
            return 5

        else:
            return 1

    def log_score(self, player:str, points:int, move:int) -> None:
        if move is None:
            self.logs.append(f'{player.upper():10} : +{points:02d} bonus points')
        else:
            self.logs.append(f'{player.upper():10} : +{points:02d} points on tile {move}')

    def reset_board(self) -> None:
        self.player_moves.clear()
        self.opponent_moves.clear()
        self.logs.clear()
        self.result = None
        self.board = [[col + (self.size * row) for col in range(1, self.size + 1)] for row in range(self.size)]

    def reset_score(self) -> None:
        self.player_score = 0
        self.opponent_score = 0

    def reset_all(self) -> None:
        self.reset_score()
        self.reset_board()
