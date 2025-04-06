'''
PROJECT:        TicTacToeReversed - A Reversed Tic-Tac-Toe Game

AUTHORS:        Raymond Allen Agustin & Basiliza Binay-an
DATE:           YYYY-MM-DD
DESCRIPTION:    Description goes here
'''

import os, random, time
# from colorama import Fore
from utils import *
from game import *
from player import *


def main():

    # banner.show_title()
    # banner.start_game()

    # loader.load()

    while True:
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
                break

        # Play vs. Bot
        if main_menu_choice == '1':
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
                    break

            # Easy
            if bot_menu_choice == '1':
                game_board = Board(size=settings.grid_size)
                winner = None

                game_board.display()

                while winner == None:
                    in_turn = settings.next_move

                    if in_turn == "Player":
                        while True:
                            try:
                                move = input(f"{in_turn}'s move : ")
                                input_handler.validate(input_=move, type="int move", selection=game_board.board)

                            except Exception as e:
                                input_handler.alert(error=e)
                                continue

                            else:
                                break
                    else:
                        move = random.randint(1,9)
                        print(f"{in_turn}'s move : Computer is thinking...", end="\r")
                        time.sleep(3)
                        print(f"{in_turn}'s move : {move}                     ")


                    # Moderate
                    # 1. Update Board:
                    if in_turn == "Player":
                        game_board.player.append(int(move))
                    else:
                        game_board.opponent.append(int(move))

                    game_board.display()

                    # 2. Update Score:

                    # 3. Evaluate:
                    if game_board.board[0][0] != 1:
                        winner = in_turn

                    else:
                        settings.next_move = settings.prev_move
                        settings.prev_move = in_turn

                print(f'{winner} wins!')
                game_board.reset()

            # Medium
            elif bot_menu_choice == '2':
                print(bot_menu_choice)

            # Difficult
            elif bot_menu_choice == '3':
                print(bot_menu_choice)

            # Back to Main Menu
            elif bot_menu_choice == '4':
                print(bot_menu_choice)
                continue

        # Play vs. Friend
        elif main_menu_choice == '2':
            print(main_menu_choice)

        # Profile
        elif main_menu_choice == '3':
            print(main_menu_choice)

        # Mechanics
        elif main_menu_choice == '4':
            print(main_menu_choice)

        # Settings
        elif main_menu_choice == '5':
            print(main_menu_choice)

        # Quit
        elif main_menu_choice == '6':
            print(main_menu_choice)
            break

if __name__ == '__main__':
    os.system("cls")
    main()
