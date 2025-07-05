'''
PROJECT: TicTacToeReversed - A Reversed Tic-Tac-Toe Game

AUTHORS: Raymond Allen Agustin
DATE:    2025-04-21
VERSION: 1.0.0
'''

'''
TODO:
- timer for play vs friend
- threading for displaying board
- pause mid game
'''

from core import *
from interface import *
from services import *
from datetime import datetime, timedelta
from colorama import init, Fore, Style

def main():

    init(autoreset=True)

    log_handler.log(level="INFO", activity="Application started.")

    player = settings.player
    # splash.start()

    log_handler.log(level="INFO", activity="Application running.")

    # Main Menu
    while True:
        splash.banner()

        main_menu = Menu(title="Main Menu", selection=main_menu_selection, columns=3)
        main_menu.display()

        while True:
            try:
                main_menu_choice = input(f"Enter your selection from the main menu [1-{len(main_menu_selection)}] : ").strip()
                input_handler.validate(input_=main_menu_choice, type="int menu", selection=main_menu_selection)

            except Exception as e:
                input_handler.alert(error=e)
                continue

            else:
                if int(main_menu_choice) != len(main_menu_selection):
                    splash.load(text=f"Loading {main_menu_selection[int(main_menu_choice)]}")
                break

        # Play vs. Bot
        if main_menu_choice == '1':

            # Difficulty Menu
            while True:
                bot_menu = Menu(title="Play vs. Bot", selection=bot_menu_selection, columns=2)
                bot_menu.display()

                while True:
                    try:
                        bot_menu_choice = input(f"Enter your selection from the menu [1-{len(bot_menu_selection)}] : ").strip()
                        input_handler.validate(input_=bot_menu_choice, type="int menu", selection=bot_menu_selection)

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        if int(bot_menu_choice) != len(bot_menu_selection):
                            splash.load(text=f"Loading {bot_menu_selection[int(bot_menu_choice)]} Round")

                        break

                # Easy
                if bot_menu_choice == '1':

                    board = Board(game=f"{main_menu_selection[int(main_menu_choice)]} [{bot_menu_selection[int(bot_menu_choice)]}]", size=player.grid_size, players=[player.username, "Computer"])

                    while True:
                        turn = player.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves
                            start_time = None
                            end_time = None

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}").strip()
                                        print(Style.RESET_ALL)

                                        # if move.upper() == 'PAUSE':
                                        #     splash.clear()
                                        #     pause_menu = Menu(title="Game Paused", selection=pause_menu_selection, columns=3)
                                        #     pause_menu.display()

                                        #     while True:
                                        #         try:
                                        #             pause_menu_choice = input(f"Enter your selection from the menu [1-{len(pause_menu_selection)}] : ").strip()
                                        #             input_handler.validate(input_=pause_menu_choice, type="int menu", selection=pause_menu_selection)

                                        #         except Exception as e:
                                        #             input_handler.alert(error=e)
                                        #             continue

                                        #         else:
                                        #             if int(pause_menu_choice) != len(pause_menu_selection):
                                        #                 splash.load(text=f"{pause_menu_selection[int(pause_menu_choice)]} Game")

                                        #             break

                                        #     # Resume
                                        #     if pause_menu_choice == '1':
                                        #         pause_menu_choice = None
                                        #         move = None
                                        #         board.display()
                                        #         continue

                                        #     else:
                                        #         break

                                        # else:

                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break


                                end_time = datetime.now()

                            if in_turn == board.players[1]: # Opponent
                                start_time = datetime.now()

                                move = bot.easy(size=player.grid_size, delay=6, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            if start_time is not None and end_time is not None:
                                elapsed = (end_time - start_time).total_seconds()
                            else:
                                elapsed = 0
                            points = board.update_score(time=elapsed)

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=-1)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                if move is not None:
                                    board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                if move is not None:
                                    board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=-1)
                                board.evaluate_points()

                            else:
                                turn = 1 - turn

                        # Retry
                        # if pause_menu_choice == '2':
                        #     pause_menu_choice = None
                        #     move = None
                        #     board.reset_all()
                        #     splash.load(text="Starting New Game")
                        #     continue

                        # Back to Main Menu
                        # elif pause_menu_choice == '3':
                        #     splash.load(text=f"Going Back to Main Menu")
                        #     break

                        # Round Menu
                        round_menu = Menu(title="Play vs. Bot", selection=round_menu_selection, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(round_menu_selection)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=round_menu_selection)

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
                        board.log_board()
                        board.reset_all()
                        splash.load(text=f"Starting New Game")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        board.log_board()
                        splash.load(text=f"Going Back to Main Menu")
                        break

                # Medium
                elif bot_menu_choice == '2':

                    board = Board(game=f"{main_menu_selection[int(main_menu_choice)]} [{bot_menu_selection[int(bot_menu_choice)]}]", size=player.grid_size, players=[player.username, "Computer"])

                    while True:
                        turn = player.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves
                            start_time = None
                            end_time = None

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}").strip()
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

                                move = bot.medium(size=player.grid_size, delay=3, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            if start_time is not None and end_time is not None:
                                elapsed = (end_time - start_time).total_seconds()
                            else:
                                elapsed = 0
                            points = board.update_score(time=elapsed)

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=-1)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                if move is not None:
                                    board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                if move is not None:
                                    board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=-1)
                                board.evaluate_points()

                            else:
                                turn = 1 - turn

                        # Round Menu
                        round_menu = Menu(title="Play vs. Bot", selection=round_menu_selection, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(round_menu_selection)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=round_menu_selection)

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
                        board.log_board()
                        board.reset_all()
                        splash.load(text=f"Starting New Game")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        board.log_board()
                        splash.load(text=f"Going Back to Main Menu")
                        break

                # Difficult
                elif bot_menu_choice == '3':

                    board = Board(game=f"{main_menu_selection[int(main_menu_choice)]} [{bot_menu_selection[int(bot_menu_choice)]}]", size=player.grid_size, players=[player.username, "Computer"])

                    while True:
                        turn = player.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves
                            start_time = None
                            end_time = None

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                while True:
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}").strip()
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

                                move = bot.difficult(size=player.grid_size, delay=1, occupied=moves)
                                print(f"{Style.BRIGHT}{Fore.RED}{f"Opponent's turn [O] : {move}"}")

                                end_time = datetime.now()

                            # Update Score
                            if start_time is not None and end_time is not None:
                                elapsed = (end_time - start_time).total_seconds()
                            else:
                                elapsed = 0
                            points = board.update_score(time=elapsed)

                            if in_turn == board.players[0]: # Player
                                board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=-1)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                if move is not None:
                                    board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                if move is not None:
                                    board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=-1)
                                board.evaluate_points()

                            else:
                                turn = 1 - turn

                        # Round Menu
                        round_menu = Menu(title="Play vs. Bot", selection=round_menu_selection, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(round_menu_selection)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=round_menu_selection)

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
                        board.log_board()
                        board.reset_all()
                        splash.load(text=f"Starting New Game")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        board.log_board()
                        splash.load(text=f"Going Back to Main Menu")
                        break

                # Back to Main Menu
                elif bot_menu_choice == '4':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # Play vs. Friend
        elif main_menu_choice == '2':

            friend = "Friend"

            # Friend Menu
            while True:
                friend_menu = Menu(title="Play vs. Friend", selection=friend_menu_selection, columns=3)
                friend_menu.display()

                while True:
                    try:
                        friend_menu_choice = input(f"Enter your selection from the menu [1-{len(friend_menu_selection)}] : ").strip()
                        input_handler.validate(input_=friend_menu_choice, type="int menu", selection=friend_menu_selection)

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        board = Board(game=f"{main_menu_selection[int(main_menu_choice)].upper()}", size=player.grid_size, players=[player.username, friend])

                        if int(friend_menu_choice) != len(friend_menu_selection):
                            splash.load(text=f"Loading {friend_menu_selection[int(friend_menu_choice)]}")

                        break

                # Start Game
                if friend_menu_choice == '1':

                    while True:
                        turn = player.first_move

                        board.display()

                        while board.result is None:

                            # Get Move
                            in_turn = board.players[turn]
                            moves = board.player_moves + board.opponent_moves
                            move = None
                            start_time = None
                            end_time = None

                            if in_turn == board.players[0]: # Player
                                start_time = datetime.now()

                                while True:
                                    # TODO: timer
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.GREEN}{"Your turn [X] : "}").strip()
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
                                    # TODO: timer
                                    try:
                                        move = input(f"{Style.BRIGHT}{Fore.RED}{"Opponent's turn [O] : "}").strip()
                                        print(Style.RESET_ALL)
                                        input_handler.validate(input_=move, type="int move", selection=board.board, occupied=moves)

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                end_time = datetime.now()

                            # Update Score
                            if start_time is not None and end_time is not None:
                                elapsed = (end_time - start_time).total_seconds()
                            else:
                                elapsed = 0
                            points = board.update_score(time=elapsed)

                            if in_turn == board.players[0]: # Player
                                if move is not None:
                                    board.player_score += points
                            if in_turn == board.players[1]: # Opponent
                                if move is not None:
                                    board.opponent_score += points

                            board.log_score(player=in_turn, points=points, move=-1)

                            # Update Board
                            if in_turn == board.players[0]: # Player
                                if move is not None:
                                    board.player_moves.append(int(move))
                            if in_turn == board.players[1]: # Opponent
                                if move is not None:
                                    board.opponent_moves.append(int(move))

                            # Display Board
                            board.display()

                            # Evaluate Winner
                            if board.evaluate_board(in_turn_symbol=f"{"O" if in_turn == board.players[1] else "X"}"):

                                bonus_points = 20

                                if in_turn == board.players[0]: # Player
                                    board.opponent_score += bonus_points
                                if in_turn == board.players[1]: # Opponent
                                    board.player_score += bonus_points

                                board.log_score(player=board.players[1 - turn], points=bonus_points, move=-1)
                                board.evaluate_points()

                            else:
                                turn = 1 - turn

                        # Round Menu
                        round_menu = Menu(title="Play vs. Friend", selection=round_menu_selection, columns=3)
                        round_menu.display()

                        while True:
                            try:
                                round_menu_choice = input(f"Enter your selection from the menu [1-{len(round_menu_selection)}] : ").strip()
                                input_handler.validate(input_=round_menu_choice, type="int menu", selection=round_menu_selection)

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
                        board.log_board()
                        board.reset_all()
                        splash.load(text=f"Starting New Game")
                        continue

                    # Back to Main Menu
                    elif round_menu_choice == '3':
                        board.log_board()
                        splash.load(text=f"Going Back to Main Menu")
                        break

                # Set Friend's Name
                elif friend_menu_choice == '2':
                    splash.label(text="Set Friend's Name")

                    while True:
                        try:
                            friend = input(f"Enter a name for your friend : ").strip()
                            input_handler.validate(input_=friend, type="str limit")

                        except Exception as e:
                            input_handler.alert(error=e)
                            continue

                        else:
                            break

                    save_menu = Menu(title="Set Friend's Name", selection=save_menu_selection, columns=2)
                    save_menu.display()

                    while True:
                        try:
                            save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                            input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                        except Exception as e:
                            input_handler.alert(error=e)
                            continue

                        else:
                            break

                    # Cancel
                    if save_menu_choice == '1':
                        splash.load(text=f"Reverting Changes")
                        continue

                    # Proceed
                    elif save_menu_choice == '2':
                        board.players[1] = friend
                        splash.load(text=f"Updating Changes")
                        continue

                # Back to Menu
                elif friend_menu_choice == '3':
                    splash.load(text=f"Going Back to Main Menu")
                    break

        # Profile
        elif main_menu_choice == '3':
            player.display_profile()
            splash.load(text="Going Back to Main Menu")
            continue

        # Mechanics
        elif main_menu_choice == '4':
            mechanics.display()
            splash.load(text="Going Back to Main Menu")
            continue

        # Settings
        elif main_menu_choice == '5':

            while True:
                settings.display()

                while True:
                    try:
                        settings_choice = input(f"Enter your selection from the menu [1-{len(settings.build_menu())}] : ").strip()
                        input_handler.validate(input_=settings_choice, type="int menu", selection=settings.build_menu())

                    except Exception as e:
                        input_handler.alert(error=e)
                        continue

                    else:
                        print()
                        break

                # Logged-in
                if player.logged_in:

                    # Change Username
                    if settings_choice == '1':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        while True:
                            try:
                                new_username = input(f"Enter new username : ").strip()

                                if new_username.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=new_username, type="str limit")


                                if settings.update_profile(profile="username", value=new_username):
                                    splash.label(text="Username updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Change Password
                    elif settings_choice == '2':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        while True:
                            try:
                                new_password = input(f"Enter new password : ").strip()

                                if new_password.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=new_password, type="mix limit")


                                if settings.update_profile(profile="password", value=new_username):
                                    splash.label(text="Password updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Sign Out
                    elif settings_choice == '3':
                        save_menu = Menu(title="Logout", selection=save_menu_selection, columns=2)
                        save_menu.display()

                        while True:
                            try:
                                save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                                input_handler.validate(input_=save_menu_choice, type="int settings", selection=save_menu_selection)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Cancel
                        if save_menu_choice == '1':
                            splash.label(text="Log out unsuccessful!")
                            continue

                        # Proceed
                        elif save_menu_choice == '2':
                            if settings.sign_out():
                                splash.label(text="Logged out successfully!")
                            continue

                    # Grid Size
                    elif settings_choice == '4':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(3, 6)]

                        while True:
                            try:
                                grid_size_choice = input(f"Select grid size [3/4/5] : ").strip()

                                if grid_size_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=grid_size_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="grid_size", value=int(grid_size_choice)):
                                    splash.label(text="Grid size updated successfully!")


                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Time Limit
                    elif settings_choice == '5':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(10, 61)]

                        while True:
                            try:
                                time_limit_choice = input(f"Adjust time limit [10-60] : ").strip()

                                if time_limit_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=time_limit_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="time_limit", value=int(time_limit_choice)):
                                    splash.label(text="Time limit updated successfully!")


                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # First Move
                    elif settings_choice == '6':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(0, 2)]

                        while True:
                            try:
                                first_move_choice = input(f"Who plays first? [0] You [1] Opponent: ").strip()

                                if first_move_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=first_move_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="first_move", value=int(first_move_choice)):
                                    splash.label(text="Grid size updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Reset Progress
                    elif settings_choice == '7':
                        save_menu = Menu(title="Reset Progress", selection=save_menu_selection, columns=2)
                        save_menu.display()

                        while True:
                            try:
                                save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                                input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Cancel
                        if save_menu_choice == '1':
                            splash.label(text="Reset unsuccessful!")
                            continue

                        # Proceed
                        elif save_menu_choice == '2':
                            if settings.reset_progress():
                                splash.label(text="Progress reset successfully!")
                            continue

                    # Reset Preferences
                    elif settings_choice == '8':
                        save_menu = Menu(title="Reset Preferences", selection=save_menu_selection, columns=2)
                        save_menu.display()

                        while True:
                            try:
                                save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                                input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Cancel
                        if save_menu_choice == '1':
                            splash.label(text="Reset unsuccessful!")
                            continue

                        # Proceed
                        elif save_menu_choice == '2':
                            if settings.reset_preferences():
                                splash.label(text="Preferences reset successfully!")
                            continue

                    # Delete Account
                    elif settings_choice == '9':
                        save_menu = Menu(title="Delete Account", selection=save_menu_selection, columns=2)
                        save_menu.display()

                        while True:
                            try:
                                save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                                input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Cancel
                        if save_menu_choice == '1':
                            splash.label(text="Account deletion unsuccessful!")
                            continue

                        # Proceed
                        elif save_menu_choice == '2':
                            if settings.delete_account():
                                splash.label(text="Account deleted successfully!")
                            continue

                    # Save and Exit
                    elif settings_choice == '10':
                        splash.load(text="Going Back to Main Menu")
                        break

                # Guest
                else:

                    # Sign In
                    if settings_choice == '1':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        while True:

                            try:
                                while True:
                                    try:
                                        username = input(f"Enter username : ").strip()

                                        if username.upper() == 'EXIT':
                                            break

                                        input_handler.validate(input_=username, type="str")

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                while True:
                                    try:
                                        password = input(f"Enter password : ").strip()

                                        if password.upper() == 'EXIT':
                                            break

                                        input_handler.validate(input_=password, type="mix")

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                if 'EXIT' in (username.upper(), password.upper()):
                                    break

                                if settings.sign_in(username=username, password=password):
                                    splash.label(text="Signed in successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Sign Up
                    elif settings_choice == '2':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        while True:

                            try:
                                while True:
                                    try:
                                        username = input(f"Enter username : ").strip()

                                        if username.upper() == 'EXIT':
                                            break

                                        input_handler.validate(input_=username, type="str limit")

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                while True:
                                    try:
                                        password = input(f"Enter password : ").strip()

                                        if password.upper() == 'EXIT':
                                            break

                                        input_handler.validate(input_=password, type="mix limit")

                                    except Exception as e:
                                        input_handler.alert(error=e)
                                        continue

                                    else:
                                        break

                                if 'EXIT' in (username.upper(), password.upper()):
                                    break

                                if settings.sign_up(username=username, password=password):
                                    splash.label(text="Signed up successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Grid Size
                    elif settings_choice == '3':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(3, 6)]

                        while True:
                            try:
                                grid_size_choice = input(f"Select grid size [3/4/5] : ").strip()

                                if grid_size_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=grid_size_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="grid_size", value=int(grid_size_choice)):
                                    splash.label(text="Grid size updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Time Limit
                    elif settings_choice == '4':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(10, 61)]

                        while True:
                            try:
                                time_limit_choice = input(f"Adjust time limit [10-60] : ").strip()

                                if time_limit_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=time_limit_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="time_limit", value=int(time_limit_choice)):
                                    splash.label(text="Time limit updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # First Move
                    elif settings_choice == '5':
                        splash.label(text=settings.menu[int(settings_choice)])
                        splash.hint(text="Enter 'exit' to abort.")

                        selection = [option for option in range(0, 2)]

                        while True:
                            try:
                                first_move_choice = input(f"Who plays first? [0] You [1] Opponent: ").strip()

                                if first_move_choice.upper() == 'EXIT':
                                    break

                                input_handler.validate(input_=first_move_choice, type="int settings", selection=selection)


                                if settings.save_preferences(preference="first_move", value=int(first_move_choice)):
                                    splash.label(text="First move updated successfully!")

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                    # Reset Preferences
                    elif settings_choice == '6':
                        save_menu = Menu(title="Reset Preferences", selection=save_menu_selection, columns=2)
                        save_menu.display()

                        while True:
                            try:
                                save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                                input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break

                        # Cancel
                        if save_menu_choice == '1':
                            splash.label(text="Reset unsuccessful!")
                            continue

                        # Proceed
                        elif save_menu_choice == '2':
                            if settings.reset_preferences():
                                splash.label(text="Preferences reset successfully!")
                            continue

                    # Save and Exit
                    elif settings_choice == '7':
                        splash.load(text="Going Back to Main Menu")
                        break

        # Quit
        elif main_menu_choice == '6':
            save_menu = Menu(title="Quit", selection=save_menu_selection, columns=2)
            save_menu.display()

            while True:
                try:
                    save_menu_choice = input(f"Enter your selection from the menu [1-{len(save_menu_selection)}] : ").strip()
                    input_handler.validate(input_=save_menu_choice, type="int menu", selection=save_menu_selection)

                except Exception as e:
                    input_handler.alert(error=e)
                    continue

                else:
                    break

            # Cancel
            if save_menu_choice == '1':
                splash.load(text="Going Back to Main Menu")
                continue

            # Proceed
            elif save_menu_choice == '2':
                if player.logged_in:
                    if settings.sign_out():
                        splash.load(text="Signing out")

                splash.load(text="Exiting the Game")
                log_handler.log(level="INFO", activity="Application closed.")
                break

if __name__ == '__main__':
    main()
