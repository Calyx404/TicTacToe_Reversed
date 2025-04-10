class Board:
    def __init__(self, size:int) -> None:
        self.size = size
        self.board = [[col + (size * row) for col in range(1, size + 1)] for row in range(size)]
        self.player_moves = []
        self.opponent_moves = []
        self.player_score = 0
        self.opponent_score = 0
        self.logs = []

    def display(self) -> None:
        # Configuration
        game_board_width = 87
        score_board_width = 43
        tile_height = 3
        tile_width = (game_board_width - (self.size + 1)) // self.size

        # Border formatters
        def board_border(char: str, end: str, width: int) -> str:
            return end + (char * (width - (len(end) * 2))) + end

        def tile_border(char: str, end: str) -> str:
            return "  " + "".join(char * (tile_width - 2) + end for _ in range(self.size))

        # Replace player and opponent moves
        for row in self.board:
            for tile in self.player_moves:
                if tile in row:
                    row[row.index(tile)] = 'X'
            for tile in self.opponent_moves:
                if tile in row:
                    row[row.index(tile)] = 'O'

        # Display headers
        print(f'{board_border("-", "  ", game_board_width)}  {board_border("-", "  ", score_board_width)}')
        print(f'|{"PLAY VS. BOT [EASY]":^{game_board_width - 2}}|  |{"SCORE BOARD":^{score_board_width - 2}}|')
        print(f'{board_border("-", "  ", game_board_width)}  {board_border("-", "  ", score_board_width)}')

        # Score section
        player_info = f"Player [X] : {self.player_score}"
        opponent_info = f"Opponent [O] : {self.opponent_score}"
        leading = "Winning : Player [X]" if self.player_score > self.opponent_score else \
                ("Winning : Opponent [O]" if self.opponent_score > self.player_score else "Draw")

        print(f'|{player_info:^{(game_board_width - 3) // 2}}|{opponent_info:^{(game_board_width - 3) // 2}}|  |{leading:^{score_board_width - 2}}|')
        print(f'{board_border("-", "  ", game_board_width)}  {board_border("-", "  ", score_board_width)}\n')

        # Prepare logs
        logs_display = [f'{board_border("-", "  ", score_board_width)}']
        if not self.logs:
            logs_display.append(f'| -> {"No moves in record.":<{score_board_width - 6}}|')
        else:
            for log in self.logs:
                logs_display.append(f'| -> {log:<{score_board_width - 6}}|')

        log_index = 0

        # Print game board rows
        for row in self.board:
            # Print top border of tiles
            print(f' {tile_border("-", "   ")}', end="")

            if log_index < len(logs_display):
                print(f"  {logs_display[log_index]}")
                log_index += 1
            elif log_index == len(logs_display):
                print(f"  {board_border('-', '  ', score_board_width)}")
                log_index += 1
            else:
                print(" " * score_board_width)

            # Print tile contents row-by-row
            for h in range(tile_height):
                if h == tile_height // 2:
                    row_line = "".join(f"|{num:^{tile_width}}" for num in row) + "|"
                else:
                    row_line = (f"|{' ' * tile_width}" * self.size) + "|"

                print(f' {row_line}', end="  ")

                if log_index < len(logs_display):
                    print(f" {logs_display[log_index]}")
                    log_index += 1
                elif log_index == len(logs_display):
                    print(f" {board_border('-', '  ', score_board_width)}")
                    log_index += 1
                else:
                    print(" " * score_board_width)

        # Bottom border of the board
        print(f' {tile_border("-", "   ")}')

    def evaluate(self) -> None:
        # Horizontal
        ...

        # Vertical
        ...

        # Diagonal
        ...

    def update_score(self, time:float) -> int:
        if time <= 2:
            return 10
        elif time <= 5:
            return 5
        else:
            return 1

    def log_score(self, player:str, points:int, move:int) -> None:
        self.logs.append(f'{player.upper():10} : +{points} points on tile {move}')

    def reset_board(self) -> None:
        self.player_moves.clear()
        self.opponent_moves.clear()
        self.board = [[col + (self.size * row) for col in range(1, self.size + 1)] for row in range(self.size)]

    def reset_score(self) -> None:
        self.player_score = 0
        self.opponent_score = 0

    def reset_all(self) -> None:
        self.reset_score()
        self.reset_board()
