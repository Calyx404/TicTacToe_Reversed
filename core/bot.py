"""
bot.py

This module provides the logic for the bot opponent in the reversed Tic Tac Toe game.
It includes functions for different difficulty levels (easy, medium, difficult) and a visual "thinking" animation
to simulate the bot's decision-making process.

Functions:
    - think(event): Displays a "thinking" animation while the bot calculates its move.
    - easy(size, delay, occupied): Generates a random move for the bot in easy mode.
    - medium(size, delay, occupied): Generates a random move for the bot in medium mode.
    - difficult(size, delay, occupied): Generates a random move for the bot in difficult mode.

Dependencies:
    - random.choice: Used to randomly select a move from available cells.
    - time.sleep: Used to simulate delays in the bot's decision-making process.
    - threading.Thread: Used to run the "thinking" animation in a separate thread.
    - threading.Event: Used to control the "thinking" animation.

Global Variables:
    - text (str): The message displayed during the bot's "thinking" animation.
"""

from random import choice
from time import sleep
from threading import Thread, Event

# Global
text = "Computer is thinking..."

def think(event:Event) -> None:
    """
    Displays a "thinking" animation while the bot calculates its move.

    Args:
        event (Event): A threading event used to control the animation. The animation stops when the event is set.

    Behavior:
        - Continuously displays a message with a typing effect until the event is set.
        - Clears the message once the event is set.
    """

    from colorama import Fore, Style

    while not event.is_set():
        for index in range(1, len(text) + 1):
            if event.is_set():
                break

            print(" " * 50, end="\r", flush=True)
            print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {text[:index]}"}", end="\r", flush=True)
            sleep(0.1)

    print(" " * 50, end="\r", flush=True)

def easy(size:int, delay:int, occupied:list[int] = []) -> int:
    """
    Generates a random move for the bot in easy mode.

    Args:
        size (int): The size of the game board (e.g., 3 for a 3x3 board).
        delay (int): The delay in seconds before the bot makes its move.
        occupied (list[int], optional): A list of already occupied cells on the board.

    Returns:
        int: The cell number chosen by the bot. Returns None if no moves are available.

    Behavior:
        - Randomly selects a move from the available cells.
        - Simulates a delay and displays the "thinking" animation.
    """

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    all_cells = list(range(1, size**2 + 1))
    available = [cell for cell in all_cells if cell not in occupied]
    move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move

def medium(size:int, delay:int, occupied:list[int] = []) -> int:
    """
    Generates a move for the bot in medium mode, aiming to block the player's moves.

    Args:
        size (int): The size of the game board (e.g., 3 for a 3x3 board).
        delay (int): The delay in seconds before the bot makes its move.
        occupied (list[int], optional): A list of already occupied cells on the board.

    Returns:
        int: The cell number chosen by the bot. Returns None if no moves are available.

    Behavior:
        - Attempts to block the player's moves by analyzing potential lines.
        - Simulates a delay and displays the "thinking" animation.
    """

    def find_blocking_move(size, occupied):
        """
        Finds a move that blocks the player's potential winning line.

        Args:
            size (int): The size of the game board.
            occupied (list[int]): A list of already occupied cells.

        Returns:
            int: The cell number to block the player, or None if no blocking move is found.
        """

        blocking_cell = None
        all_cells = list(range(1, size**2 + 1))
        available = [cell for cell in all_cells if cell not in occupied]

        # Check rows, columns, and diagonals for potential blocking moves
        for row_index in range(size):
            # Check rows
            row_cells = [row_index * size + col_index + 1 for col_index in range(size)]
            if len(set(row_cells) - set(occupied)) == 1:
                blocking_cell = list(set(row_cells) - set(occupied))[0]
            if blocking_cell in available:
                return blocking_cell

            # Check columns
            column_cells = [row_index + size * col_index + 1 for col_index in range(size)]
            if len(set(column_cells) - set(occupied)) == 1:
                blocking_cell = list(set(column_cells) - set(occupied))[0]
            if blocking_cell in available:
                return blocking_cell

        # Check diagonals
        primary_diagonal_cells = [diagonal_index * size + diagonal_index + 1 for diagonal_index in range(size)]
        if len(set(primary_diagonal_cells) - set(occupied)) == 1:
            blocking_cell = list(set(primary_diagonal_cells) - set(occupied))[0]
            if blocking_cell in available:
                return blocking_cell

        secondary_diagonal_cells = [(diagonal_index + 1) * (size - 1) for diagonal_index in range(size)]
        if len(set(secondary_diagonal_cells) - set(occupied)) == 1:
            blocking_cell = list(set(secondary_diagonal_cells) - set(occupied))[0]
            if blocking_cell in available:
                return blocking_cell

        return None

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    # Attempt to find a blocking move
    move = find_blocking_move(size, occupied)

    # If no blocking move is found, pick a random available move
    if move is None:
        all_cells = list(range(1, size**2 + 1))
        available = [cell for cell in all_cells if cell not in occupied]
        move = choice(available) if available else None

    thinking.set()
    thread.join()

    return move

def difficult(size: int, delay: int, occupied: list[int] = []) -> int:
    """
    Generates the most optimal move for the bot in difficult mode using the minimax algorithm.

    Args:
        size (int): The size of the game board (e.g., 3 for a 3x3 board).
        delay (int): The delay in seconds before the bot makes its move.
        occupied (list[int], optional): A list of already occupied cells on the board.

    Returns:
        int: The cell number chosen by the bot. Returns None if no moves are available.

    Behavior:
        - Uses the minimax algorithm to find the best move.
        - Simulates a delay and displays the "thinking" animation.
    """

    def is_winner(board, player):
        """
        Checks if the given player has won on the board.
        """

        for row in range(size):
            if all(board[row * size + col] == player for col in range(size)):
                return True
        for col in range(size):
            if all(board[row * size + col] == player for row in range(size)):
                return True
        if all(board[i * size + i] == player for i in range(size)):
            return True
        if all(board[(i + 1) * (size - 1)] == player for i in range(size)):
            return True
        return False

    def minimax(board, depth, is_maximizing):
        """
        Minimax algorithm to evaluate the best move.
        """

        if is_winner(board, "O"):  # Bot wins
            return 10 - depth
        if is_winner(board, "X"):  # Player wins
            return depth - 10
        if all(cell != " " for cell in board):  # Draw
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(len(board)):
                if board[i] == " ":
                    board[i] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(best_score, score)
            return best_score

    def find_best_move(board):
        """
        Finds the best move for the bot using the minimax algorithm.
        """

        best_score = float("-inf")
        best_move = None
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, 0, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    thinking = Event()

    thinking.clear()
    thread = Thread(target=think, args=(thinking,))
    thread.start()

    sleep(delay)

    # Create the board representation
    all_cells = list(range(1, size**2 + 1))
    board = [" " if cell not in occupied else "X" for cell in all_cells]

    # Find the best move using minimax
    best_move = find_best_move(board)

    thinking.set()
    thread.join()

    return best_move + 1 if best_move is not None else None
