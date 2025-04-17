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
    from datetime import datetime, timedelta
    from colorama import init, Fore, Style

    init(autoreset=True)

    splash.clear()

    log_handler.log(level="INFO", activity="Application started.")

    splash.start()
    splash.load(text="Loading Game")
    settings = Settings()

    log_handler.log(level="INFO", activity="Application running.")

    # Main Menu
    while True:
        splash.banner()

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

                    board = Board(game=f"{menu.main_menu[int(main_menu_choice)]} [{menu.bot_menu[int(bot_menu_choice)]}]", size=settings.grid_size, players=[settings.username, "Computer"])

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

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

                                move = bot.easy(size=settings.grid_size, delay=6, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            points = board.update_score(time=(end_time - start_time).total_seconds())

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.evaluate_points()

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

                    board = Board(game=f"{menu.main_menu[int(main_menu_choice)]} [{menu.bot_menu[int(bot_menu_choice)]}]", size=settings.grid_size, players=[settings.username, "Computer"])

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

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

                                move = bot.easy(size=settings.grid_size, delay=3, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            points = board.update_score(time=(end_time - start_time).total_seconds())

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.evaluate_points()

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

                # Difficult
                elif bot_menu_choice == '3':

                    board = Board(game=f"{menu.main_menu[int(main_menu_choice)]} [{menu.bot_menu[int(bot_menu_choice)]}]", size=settings.grid_size, players=[settings.username, "Computer"])

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

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

                                move = bot.difficult(size=settings.grid_size, delay=1, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            points = board.update_score(time=(end_time - start_time).total_seconds())

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.evaluate_points()

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

                    splash.load(text=f"Loading Game Board")

                    while True:
                        turn = settings.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

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

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Opponent's turn [O] : "}")
                                        print(Style.RESET_ALL)
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            # Update Score
                            points = board.update_score(time=(end_time - start_time).total_seconds())

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=move)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn=in_turn, in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=None)
                                board.evaluate_points()

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
                        splash.load(text=f"Updating Changes")
                        continue

                # Back to Menu
                elif friend_menu_choice == '3':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # !TODO: Profile
        elif main_menu_choice == '3':
            print(main_menu_choice)
            continue

        # Mechanics
        elif main_menu_choice == '4':
            mechanics.display()
            splash.load(text="Going Back to Main Menu")
            continue

        # !UPDATE : Settings
        elif main_menu_choice == '5':

            while True:
                settings.display()

                while True:
                    try:
                        settings_choice = input(f"Enter your selection from the menu [1-{len(settings.menu)}] : ").strip()
                        input_handler.validate(input_=settings_choice, type="int menu", selection=settings.menu)

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        break

                # Logged-in
                if settings.logged_in:
                    if settings_choice == '1':
                        while True:
                            try:
                                new_username = input(f"Enter new username : ").strip()
                                input_handler.validate(input_=new_username, type="str limit username")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        settings.update_credentials(new_username=new_username)
                        print(f"Username updated to {new_username}.")

                    elif settings_choice == '2':
                        new_password = input("Enter new password: ")
                        settings.update_credentials(new_password=new_password)
                        print("Password updated.")
                    elif settings_choice == '3':
                        settings.logout_user()
                        print("Logged out successfully.")
                    elif settings_choice == '4':
                        grid = input("Choose Grid Size (3/4/5): ")
                        if grid in ['3', '4', '5']:
                            settings.grid_size = int(grid)
                        else:
                            print("Invalid grid size.")
                    elif settings_choice == '5':
                        try:
                            time = int(input("Enter time limit (10-60): "))
                            if 10 <= time <= 60:
                                settings.time_limit = time
                            else:
                                print("Invalid time limit.")
                        except ValueError:
                            print("Please enter a valid number.")
                    elif settings_choice == '6':
                        first = input("Who plays first? [0] You [1] Opponent: ")
                        if first in ['0', '1']:
                            settings.first_move = int(first)
                        else:
                            print("Invalid choice.")
                    elif settings_choice == '7':
                        confirm = input("Are you sure to reset progress? (y/n): ").lower()
                        if confirm == 'y':
                            settings.reset_progress_confirmed()
                    elif settings_choice == '8':
                        confirm = input("Are you sure to delete your account? (y/n): ").lower()
                        if confirm == 'y':
                            if settings.delete_account_confirmed():
                                print("Account deleted successfully.")
                                break
                    elif settings_choice == '9':
                        settings.reset_game_preferences()
                        print("Game preferences reset to default.")
                    elif settings_choice == '10':
                        settings.save_preferences()
                        print("Preferences saved.")
                    elif settings_choice == '11':
                        splash.load(text="Going Back to Main Menu")
                        break

                # Guest
                else:
                    if settings_choice == '1':
                        u = input("Enter username: ")
                        p = input("Enter password: ")
                        if settings.sign_in(u, p):
                            print("Signed in successfully.")
                        else:
                            print("Incorrect username or password.")
                    elif settings_choice == '2':
                        u = input("Choose username: ")
                        p = input("Choose password: ")
                        if settings.sign_up(u, p):
                            print("Account created successfully.")
                        else:
                            print("Username already exists.")
                    elif settings_choice == '3':
                        grid = input("Choose Grid Size (3/4/5): ")
                        if grid in ['3', '4', '5']:
                            settings.grid_size = int(grid)
                        else:
                            print("Invalid grid size.")
                    elif settings_choice == '4':
                        try:
                            time = int(input("Enter time limit (10-60): "))
                            if 10 <= time <= 60:
                                settings.time_limit = time
                            else:
                                print("Invalid time limit.")
                        except ValueError:
                            print("Please enter a valid number.")
                    elif settings_choice == '5':
                        first = input("Who plays first? [0] You [1] Opponent: ")
                        if first in ['0', '1']:
                            settings.first_move = int(first)
                        else:
                            print("Invalid choice.")
                    elif settings_choice == '6':
                        settings.reset_game_preferences()
                        print("Game preferences reset to default.")
                    elif settings_choice == '7':
                        print("Preferences saved (not linked to an account).")
                    elif settings_choice == '8':
                        splash.load(text="Going Back to Main Menu")
                        break

        # Quit
        elif main_menu_choice == '6':
            splash.load(text="Exiting the Game")
            log_handler.log(level="INFO", activity="Application closed.")
            break

if __name__ == '__main__':
    main()
