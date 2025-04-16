'''
PROJECT:        TicTacToeReversed - A Reversed Tic-Tac-Toe Game

AUTHORS:        Raymond Allen Agustin & Basiliza Binay-an
DATE:           YYYY-MM-DD
DESCRIPTION:    Description goes here
'''

from utils import *
from game import *
from player import *

def main():
    from os import system
    from datetime import datetime, timedelta
    from colorama import init, Fore, Style

    init(autoreset=True)

    system("cls")

    log_handler.log(level="INFO", activity="Application started.")

    splash.start()
    splash.load(text="Loading Game")

    log_handler.log(level="INFO", activity="Application running.")

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

                    board = Board(game=f"{menu.main_menu[int(main_menu_choice)].upper()} [{menu.bot_menu[int(bot_menu_choice)].upper()}]", size=settings.grid_size, players=[settings.username, "Computer"])

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                moves = board.player_moves + board.opponent_moves

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}")
                                        print(Style.RESET_ALL)
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            if in_turn == board.players[1]: # Opponent
                                start_time = datetime.now()

                                moves = board.player_moves + board.opponent_moves

                                move = bot.easy(size=settings.grid_size, delay=5.25, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            if in_turn == board.players[0]: # Player
                                points = board.update_score(time=(end_time - start_time).total_seconds())
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                points = board.update_score(time=(end_time - start_time).total_seconds())
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Board
                            if board.evaluate(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                if board.player_score > board.opponent_score:
                                    win_text = "YOU WIN"
                                    win_fore = "GREEN"
                                elif board.player_score < board.opponent_score:
                                    win_text = "YOU LOST"
                                    win_fore = "RED"
                                else:
                                    win_text = "DRAW"
                                    win_fore = "YELLOW"

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.result = win_text

                                splash.line(fore=win_fore)
                                splash.ascii_art(text=win_text, fore=win_fore)
                                board.display()
                                splash.line(fore=win_fore)

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
                        # save game info on json
                        board.reset_all()
                        splash.load(text=f"Starting New Game")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        # save game info on json
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
                        board = Board(game=f"{menu.main_menu[int(main_menu_choice)].upper()}", size=settings.grid_size, players=[settings.username, "Friend"])
                        break

                # Start Game
                if friend_menu_choice == '1':

                    splash.load(text=f"Starting Game")

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                moves = board.player_moves + board.opponent_moves

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}{Style.RESET_ALL}")
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            if in_turn == board.players[1]: # Opponent
                                start_time = datetime.now()

                                moves = board.player_moves + board.opponent_moves

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.RED}{"Opponent's turn [O] : "}{Style.RESET_ALL}")
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            # Update Score
                            if in_turn == board.players[0]: # Player
                                points = board.update_score(time=(end_time - start_time).total_seconds())
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                points = board.update_score(time=(end_time - start_time).total_seconds())
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Board
                            if board.evaluate(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                if board.player_score > board.opponent_score:
                                    win_text = "GREEN WINS"
                                    win_fore = "GREEN"
                                elif board.player_score < board.opponent_score:
                                    win_text = "RED WINS"
                                    win_fore = "RED"
                                else:
                                    win_text = "DRAW"
                                    win_fore = "YELLOW"

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.result = win_text

                                splash.line(fore=win_fore)
                                splash.ascii_art(text=win_text, fore=win_fore)
                                board.display()
                                splash.line(fore=win_fore)

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
                            # save game info on json
                            board.reset_all()
                            splash.load(text=f"Starting New Game")
                            continue

                        # Back to Main Menu
                        elif round_menu_choice == '3':
                            # save game info on json
                            splash.load(text=f"Going Back to Main Menu")
                            break

                # Set Friend's Name
                elif friend_menu_choice == '2':
                    splash.load(text=f"Setting Up")

                    while True:
                        try:
                            friend = input(f"Enter a name for your friend : ").strip()
                            input_handler.validate(input_=friend, type="str limit")

                        except Exception as e:
                            input_handler.alert(error=e)
                            continue

                        else:
                            break

                    save_menu = menu.Menu(title="Save Preferences", selection=menu.save_menu, columns=2)
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
                        splash.load(text=f"Reverting Changes")
                        continue

                    # Save
                    elif save_menu_choice == '2':
                        board.players[1] = friend
                        splash.load(text=f"Updating Preferences")
                        continue

                # Back to Menu
                elif friend_menu_choice == '3':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # TODO: Profile
        elif main_menu_choice == '3':
            print(main_menu_choice)
            continue

        # TODO: Mechanics
        elif main_menu_choice == '4':
            mechanics.display()
            splash.load(text="Going Back to Main Menu")
            continue

        # TODO: Settings
        elif main_menu_choice == '5':
            print(main_menu_choice)
            continue

        # Quit
        elif main_menu_choice == '6':
            splash.load(text="Exiting the Game")
            log_handler.log(level="INFO", activity="Application closed.")
            break

        # TODO: Unexpected Termination
        log_handler.log(level="ERROR", activity="Application closed unexpectedly.")

if __name__ == '__main__':
    main()
