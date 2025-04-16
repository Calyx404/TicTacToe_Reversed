def display():
    from colorama import Fore, Style, init
    from keyboard import wait

    init(autoreset=True)
    highlight = lambda text: f"{Style.BRIGHT}{Fore.BLUE}{text}{Style.RESET_ALL}"

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

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

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

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 📋 {highlight("Navigate the Game")}                                                                                                               |
|                                                                                                                                    |
|    [1] {highlight("Play vs. Bot")}     — Start a match against the undefeatable computer.                                                         |
|    [2] {highlight("Play vs. Friend")}  — Enjoy a time-based match with a fellow human.                                                            |
|    [3] {highlight("Achievements")}     — View profile stats & saved scores                                                                        |
|    [4] {highlight("How to Play")}      — That's this screen you're reading now!                                                                   |
|    [5] {highlight("Settings")}         — Adjust game preferences and sign in to save progress.                                                    |
|    [6] {highlight("Quit")}             — Exit from the game.                                                                                      |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

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

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🧮 {highlight("Scoring System")}                                                                                                                  |
|                                                                                                                                    |
|    ⚡ {highlight("Speed = Points")}                                                                                                               |
|       - Move within 2 seconds: +10 points                                                                                          |
|       - Move within 3-5 seconds: +05 points                                                                                        |
|       - Move after 5 seconds: +01 pointt                                                                                           |
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

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

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

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

    print(f"""  ----------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                    |
| 🛑 {highlight("Mid-Game Actions")}                                                                                                                |
|                                                                                                                                    |
|    [e] {highlight("Exit the game")}  — no saves, no mercy                                                                                          |
|    [p] {highlight("Pause the game")} — board hides, pause menu overlays                                                                           |
|                                                                                                                                    |
  ----------------------------------------------------------------------------------------------------------------------------------
    """)

    print(f"{highlight("PRESS 'RIGHT ARROW' TO CONTINUE...")}", end="\r", flush=True)

    wait("right")

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

    print(f"{highlight("PRESS 'ESC' TO GO BACK TO MAIN MENU...")}")

    wait("esc")
