'''
PROJECT:        TicTacToeReversed - A Reversed Tic-Tac-Toe Game

AUTHORS:        Raymond Allen Agustin & Basiliza Binay-an
DATE:           YYYY-MM-DD
DESCRIPTION:    Description goes here
'''

import os, random
# from colorama import Fore
from datetime import datetime, timedelta
from utils import *
from game import *
from player import *
from bot import *


def main():

    splash.full(text="PRESS 'ENTER' TO START GAME")
    log_handler.log("Start game")
    splash.load(text="Loading Game")

    # Main Menu
    while True:
        splash.title()

        main_menu = menu.Menu(title="Main Menu", selection=menu.main_menu, columns=3)
        main_menu.display()

        while True:
            try:
                main_menu_choice = input(f"Enter your selection from the main menu [1-{len(menu.main_menu)}] : ").strip()
                input_handler.validate(input_=main_menu_choice, type="int menu", selection=menu.main_menu)

            except Exception as e:
                input_handler.alert(error=e)
                continue

            else:
                if int(main_menu_choice) != len(menu.main_menu):
                    splash.load(text=f"Loading {menu.main_menu[int(main_menu_choice)]}")
                break

        # Play vs. Bot
        if main_menu_choice == '1':

            # Difficulty Menu
            while True:
                bot_menu = menu.Menu(title="Play vs. Bot", selection=menu.bot_menu, columns=2)
                bot_menu.display()

                while True:
                    try:
                        bot_menu_choice = input(f"Enter your selection from the menu [1-{len(menu.bot_menu)}] : ").strip()
                        input_handler.validate(input_=bot_menu_choice, type="int menu", selection=menu.bot_menu)

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        if int(bot_menu_choice) != len(menu.bot_menu):
                            splash.load(text=f"Loading {menu.bot_menu[int(bot_menu_choice)]} Round")
                        break

                # Easy
                if bot_menu_choice == '1':

                    while True:
                        players = [settings.username, "Bot"]
                        board = Board(size=settings.grid_size)
                        winner = None
                        turn = first_move

                        board.display()

                        while winner is None:

                            # Get Move
                            in_turn = players[turn]

                            if in_turn == settings.username:
                                start_time = datetime.now()

                                moves = board.player_moves.copy()
                                moves.extend(board.opponent_moves)

                                while True:
                                    try:
                                        move = input(f"Your turn : ")
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            if in_turn == "Bot":
                                start_time = datetime.now()

                                moves = board.player_moves.copy()
                                moves.extend(board.opponent_moves)

                                move = easy.move(settings.grid_size, delay=2, occupied=moves)
                                print(f"Opponent's turn : {move}")

                                end_time = datetime.now()

                            # Update Score
                            if in_turn == settings.username:
                                points = board.update_score((end_time - start_time).total_seconds())
                                board.player_score += points
                            if in_turn == "Bot":
                                points = board.update_score((end_time - start_time).total_seconds())
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == settings.username:
                                board.player_moves.append(int(move))
                            if in_turn == "Bot":
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # TODO : Evaluate Board
                            if board.board[0][0] != 1:
                                bonus_points = 20
                                if in_turn == settings.username:
                                    board.player_score += bonus_points
                                if in_turn == "Bot":
                                    board.opponent_score += bonus_points

                                board.log_score(player=in_turn, points=bonus_points, move=move)
                                board.display()

                                winner = settings.username if board.player_score > board.opponent_score else "Bot"
                                print(f'{winner} wins!')

                            else:
                                turn = 1 - turn

                        # Round Menu
                        round_menu = menu.Menu(title="Play vs. Bot", selection=menu.round_menu, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(menu.round_menu)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=menu.round_menu)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Keep Playing
                        if round_menu_choice == '1':
                            board.reset_board()
                            continue

                        else:
                            break

                    # New Game
                    if round_menu_choice == '2':
                        board.reset_all()
                        splash.load(text=f"Restarting Progress")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        splash.load(text=f"Going Back to Main Menu")
                        break

                # Medium
                elif bot_menu_choice == '2':

                    print(bot_menu_choice)

                # Difficult
                elif bot_menu_choice == '3':

                    print(bot_menu_choice)

                # Back to Main Menu
                elif bot_menu_choice == '4':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # Play vs. Friend
        elif main_menu_choice == '2':
            opponent = "Friend"

            # Friend Menu
            while True:
                friend_menu = menu.Menu(title="Play vs. Friend", selection=menu.friend_menu, columns=3)
                friend_menu.display()

                while True:
                    try:
                        friend_menu_choice = input(f"Enter your selection from the menu [1-{len(menu.friend_menu)}] : ").strip()
                        input_handler.validate(input_=friend_menu_choice, type="int menu", selection=menu.friend_menu)

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        break

                # Start Game
                if friend_menu_choice == '1':

                    splash.load(text=f"Loading Board")

                    while True:
                        players = [settings.username, opponent]
                        board = Board(size=settings.grid_size)
                        winner = None
                        turn = first_move

                        board.display()

                        while winner is None:

                            in_turn = players[turn]

                            if in_turn == settings.username:
                                start_time = datetime.now()

                                moves = board.player_moves.copy()
                                moves.extend(board.opponent_moves)

                                while True:
                                    try:
                                        move = input(f"Your turn : ")
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            if in_turn == opponent:
                                start_time = datetime.now()

                                moves = board.player_moves.copy()
                                moves.extend(board.opponent_moves)

                                while True:
                                    try:
                                        move = input(f"Opponent's turn : ")
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            # Update Score:
                            if in_turn == settings.username:
                                points = board.update_score((end_time - start_time).total_seconds())
                                board.player_score += points
                            if in_turn == opponent:
                                points = board.update_score((end_time - start_time).total_seconds())
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board:
                            if in_turn == settings.username:
                                board.player_moves.append(int(move))
                            if in_turn == opponent:
                                board.opponent_moves.append(int(move))

                            # Display Board:
                            board.display()

                            # Check Winner:
                            if board.board[0][0] != 1:
                                bonus_points = 20
                                if in_turn == settings.username:
                                    board.player_score += bonus_points
                                if in_turn == opponent:
                                    board.opponent_score += bonus_points

                                board.log_score(player=in_turn, points=bonus_points, move=move)
                                board.display()

                                winner = settings.username if board.player_score > board.opponent_score else "Bot"
                                print(f'{winner} wins!')

                            else:
                                turn = 1 - turn

                        # Round Menu
                        round_menu = menu.Menu(title="Play vs. Bot", selection=menu.round_menu, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(menu.round_menu)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=menu.round_menu)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Keep Playing
                        if round_menu_choice == '1':
                            board.reset_board()
                            continue

                        # New Game
                        elif round_menu_choice == '2':
                            board.reset_all()
                            splash.load(text=f"Restarting Progress")
                            continue

                        # Back to Main Menu
                        elif round_menu_choice == '3':
                            splash.load(text=f"Going Back to Main Menu")
                            break

                # Set Friend's Name
                elif friend_menu_choice == '2':
                    while True:
                        try:
                            friend = input(f"Enter a name for your friend : ").strip()
                            input_handler.validate(input_=friend, type="str limit")

                        except Exception as e:
                            input_handler.alert(error=e)
                            continue

                        else:
                            break

                    save_menu = menu.Menu(title="Save Changes", selection=menu.save_menu, columns=2)
                    save_menu.display()

                    while True:
                        try:
                            save_menu_choice = input(f"Enter your selection from the menu [1-{len(menu.save_menu)}] : ").strip()
                            input_handler.validate(input_=save_menu_choice, type="int menu", selection=menu.save_menu)

                        except Exception as e:
                            input_handler.alert(error=e)
                            continue

                        else:
                            break

                    # Cancel
                    if save_menu_choice == '1':
                        splash.load(text=f"Cancelling Changes")
                        continue

                    # Save
                    elif save_menu_choice == '2':
                        opponent = friend
                        splash.load(text=f"Saving Changes")
                        continue

                # Back to Menu
                elif friend_menu_choice == '3':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # Profile
        elif main_menu_choice == '3':
            print(main_menu_choice)
            continue

        # Mechanics
        elif main_menu_choice == '4':
            print(main_menu_choice)
            continue

        # Settings
        elif main_menu_choice == '5':
            print(main_menu_choice)
            continue

        # Quit
        elif main_menu_choice == '6':
            splash.load(text=f"Exiting the Game")
            break

if __name__ == '__main__':
    os.system("cls")
    main()
