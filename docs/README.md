# Tic Tac Toe: Reversed

Welcome to **Tic Tac Toe: Reversed**, a thrilling twist on the classic game of Tic Tac Toe! In this version, the goal is not to win but to avoid losing. Outsmart your opponent by ensuring you don't complete a line (horizontal, vertical, or diagonal) or place the final mark on the board.

This README provides an overview of the game, its features, installation instructions, and more.

---

## Table of Contents

- [Game Overview](#game-overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Modes](#game-modes)
- [Settings](#settings)
- [Bot Difficulty Levels](#bot-difficulty-levels)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

---

## Game Overview

**Tic Tac Toe: Reversed** is a strategic game where the usual goal of forming a line is your downfall. The player who completes a line or places the final mark on the board loses. This game challenges your ability to think ahead and deceive your opponent.

---

## Features

- **Reversed Gameplay**: Avoid forming a line to win.
- **Multiple Game Modes**:
    - Play against a bot with adjustable difficulty.
    - Play with a friend in local multiplayer mode.
- **Dynamic Bot AI**: Choose from easy, medium, or difficult bot opponents.
- **Player Profiles**: Track your wins, losses, draws, and achievements.
- **Customizable Settings**: Adjust grid size, time limits, and first-move preferences.
- **ASCII Art and Animations**: Enjoy visually appealing terminal graphics and animations.
- **Error Handling**: User-friendly input validation and error messages.
- **Save and Load Progress**: Save your game progress and preferences.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:
     ```bash
     git clone https://github.com/YourUsername/TicTacToe-Reversed.git
     cd TicTacToe-Reversed
     ```
2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
3. Run the game:
     ```bash
     python main.py
     ```

---

## How to Play

1. **Objective**: Avoid forming a line (horizontal, vertical, or diagonal) or placing the final mark on the board.
2. **Game Flow**:
     - Players take turns selecting tiles on the grid.
     - The game ends when a player is forced to complete a line or the board is full.
3. **Scoring**:
     - Points are awarded based on the time taken for each move.
     - Bonus points are given for surviving the round without forming a line.

---

## Game Modes

1. **Play vs. Bot**:
     - Compete against an AI opponent.
     - Choose from three difficulty levels: Easy, Medium, and Difficult.

2. **Play vs. Friend**:
     - Play locally with a friend.
     - Take turns making moves on the same device.

3. **Player Profile**:
     - View your game statistics, achievements, and history.

---

## Settings

Customize your game preferences. The settings menu allows you to:

- **Sign In/Sign Up**: Create or log into a player profile.
- **Change Username/Password**: Update your account credentials.
- **Grid Size**: Adjust the board size (e.g., 3x3, 4x4).
- **Time Limit**: Set a time limit for each move.
- **First Move**: Choose whether you or your opponent goes first.
- **Reset Progress**: Clear your game statistics and history.
- **Reset Preferences**: Restore default settings.
- **Delete Account**: Permanently delete your player profile.

---

## Bot Difficulty Levels

1. **Easy**:
     - The bot makes random moves without strategy.
2. **Medium**:
     - The bot uses basic logic but is still beatable.
3. **Difficult**:
     - The bot employs advanced strategies to challenge the player.

---

## Technical Details

### Project Structure

```
TicTacToe-Reversed/
├── core/
│   ├── board.py         # Game board logic
│   ├── bot.py           # Bot AI logic
│   ├── mechanics.py     # Game rules and win conditions
│   ├── settings.py      # Game configurations
│   ├── player.py        # Player profile management
│   ├── settings.py      #
├── interface/
│   ├── menu.py          # Menu display and navigation
│   ├── splash.py        # ASCII art and animations
├── services/
│   ├── db_handler.py    # Database operations
│   ├── input_handler.py # Input validation
│   ├── log_handler.py   # Logging activities
├── runtime/
│   ├── data/            # Player data storage
│   ├── logs/            # Log files
├── docs/
│   ├── README.md        # Project documentation
├── main.py              # Entry point for the game
├── requirements.txt     # Python dependencies
```

### Key Technologies

- **Python**: Core programming language.
- **Colorama**: For colored terminal output.
- **JSON**: For storing player data and settings.
- **Threading**: For bot animations and delays.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
     ```bash
     git checkout -b feature-name
     ```
3. Commit your changes:
     ```bash
     git commit -m "Add feature-name"
     ```
4. Push to your branch:
     ```bash
     git push origin feature-name
     ```
5. Open a pull request.

---

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

---

Enjoy playing **Tic Tac Toe: Reversed** and challenge yourself to outsmart your opponent!
