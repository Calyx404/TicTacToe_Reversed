"""
mechanics.py

This module provides a detailed guide for players on how to play the reversed Tic Tac Toe game.
It includes information about the game overview, game modes, navigation, gameplay rules, scoring system,
scoreboard functionality, mid-game actions, and support options.

Functions:
    - display(): Displays a comprehensive guide on how to play the game.

Dependencies:
    - colorama: Used for colored terminal output.
    - interface.splash: Provides utility functions for waiting and user interaction.

"""

def display():
    """
    Displays a detailed guide for players on how to play the game. The guide includes:
    - Game overview: Explains the reversed Tic Tac Toe concept.
    - Game modes: Describes available modes (e.g., Play vs. Bot, Play vs. Friend).
    - Navigation: Provides instructions for navigating the game menu.
    - Gameplay rules: Explains the rules of the game.
    - Scoring system: Details how points are awarded during gameplay.
    - The scoreboard: Explains how scores are displayed and updated.
    - Mid-game actions: Describes actions like pausing or exiting the game.
    - Inquiries and support: Provides contact information for feedback or issues.

    Uses the `colorama` library for colored text and the `interface.splash` module for user interaction.
    """

    from colorama import Fore, Style, init
    from interface.splash import wait

    # Helper function for highlighting text
    highlight = lambda text: f"{Style.BRIGHT}{Fore.BLUE}{text}{Style.RESET_ALL}"

    # Display the "How to Play" guide
    print(f"""
  ----------------------------------------------------------------------------------------------------------------------------------
|                                                             {highlight("HOW TO PLAY")}                                                            |
  ----------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🧠 {highlight("Game Overview")}                                                                                                                   |
|                                                                                                                                    |
|    🏆 {highlight("Reversed Strategy, Ultimate Fun!")}                                                                                             |
|       Welcome to Tic Tac Toe Reversed — where the usual goal is your downfall! In this thrilling twist, the player                 |
|       who completes a line (horizontal, vertical, or diagonal) or places the final mark on the board {highlight("loses")}.                        |
|       Outsmart your opponent by {highlight("not")} forming a line. Trust me, it's harder than it sounds!                                          |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    # Wait for user input to continue
    wait(key=b' ', name="space", action="continue", end="\r")

    # Game Modes Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🎯 {highlight("Game Modes")}                                                                                                                      |
|                                                                                                                                    |
|    🤖 {highlight("Play vs. Bot")}                                                                                                                 |
|       - Choose your difficulty: {highlight("Easy")}, {highlight("Medium")}, or {highlight("Difficult")}.                                                                        |
|       - The bot's tactics evolve with difficulty.                                                                                  |
|                                                                                                                                    |
|    🧑 {highlight("Play vs. Friend")}                                                                                                              |
|       - Take turns with a human opponent.                                                                                          |
|       - You can name your rival, or it defaults to {highlight("“Friend”")}.                                                                       |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Navigation Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 📋 {highlight("Navigate the Game")}                                                                                                               |
|                                                                                                                                    |
|    [1] {highlight("Play vs. Bot")}     — Start a match against the undefeatable computer.                                                         |
|    [2] {highlight("Play vs. Friend")}  — Enjoy a time-based match with a fellow human.                                                            |
|    [3] {highlight("Achievements")}     — View profile stats & saved scores.                                                                       |
|    [4] {highlight("How to Play")}      — That's this screen you're reading now!                                                                   |
|    [5] {highlight("Settings")}         — Adjust game preferences and sign in to save progress.                                                    |
|    [6] {highlight("Quit")}             — Exit from the game.                                                                                      |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Gameplay Rules Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🕹️ {highlight("Gameplay Rules")}                                                                                                                  |
|                                                                                                                                    |
|    ⚔️ {highlight("You")} = ❌ | {highlight("Opponent")} = ⭕                                                                                                     |
|       - Take turns selecting from numbered tiles.                                                                                  |
|       - The goal is to {highlight("avoid")} completing a line.                                                                                    |
|       - If you're forced to complete a line, you {highlight("lose")}.                                                                             |
|       - If the board fills up and you placed the last tile, you also {highlight("lose")}.                                                         |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Scoring System Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🧮 {highlight("Scoring System")}                                                                                                                  |
|                                                                                                                                    |
|    ⚡ {highlight("Speed = Points")}                                                                                                               |
|       - Move within 2 seconds:   {highlight("+10 points")}                                                                                        |
|       - Move within 3-5 seconds: {highlight("+05 points")}                                                                                        |
|       - Move after 5 seconds:    {highlight("+01 points")}                                                                                        |
|                                                                                                                                    |
|    🌟 {highlight("Bonus Points")}                                                                                                                 |
|       - +20 pts if you survive the whole round without creating a line!                                                            |
|                                                                                                                                    |
|    🏆 {highlight("Winning")}                                                                                                                      |
|       - The round ends when a player loses by making a line or placing the final tile.                                             |
|       - The player with the higher score WINS!                                                                                     |
|       - Draw? Highest points still decide the winner.                                                                              |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Scoreboard Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 📊 {highlight("The Scoreboard")}                                                                                                                  |
|                                                                                                                                    |
|    - Updated after every move                                                                                                      |
|    - Displays: current scores, player turn, and match outcome                                                                      |
|    - Visible beside the game board                                                                                                 |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Mid-Game Actions Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🛑 {highlight("Mid-Game Actions")}                                                                                                                |
|                                                                                                                                    |
|    [esc]   {highlight("Exit the game")} — no saves, no mercy                                                                                      |
|    [space] {highlight("Pause the game")} — board hides, pause menu overlays                                                                       |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    wait(key=b' ', name="space", action="continue", end="\r")

    # Inquiries & Support Section
    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 📬 {highlight("Inquiries & Support")}                                                                                                             |
|                                                                                                                                    |
|    Got feedback or an issue? Hit us up!                                                                                            |
|       📧 Email: {highlight("developer@gmail.com")}                                                                                                |
|       🔗 LinkedIn: {highlight("https://www.linkedin.com/in/developer-12345")}                                                                     |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    # Wait for user input to go back to the main menu
    wait(key=b'\r', name="enter", action="go back to main menu")
