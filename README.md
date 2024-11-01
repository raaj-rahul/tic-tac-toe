# Tic Tac Toe Game in Python

This is a simple, text-based **Tic Tac Toe game** written in Python. It allows two players to play against each other on the same computer. The game runs in the terminal or command prompt.

## Game Overview

- The game board is a 3x3 grid.
- Players take turns marking a cell with either 'X' or 'O'.
- The player who succeeds in placing three of their marks in a row (horizontal, vertical, or diagonal) wins the game.
- If all nine cells are filled without a winner, the game ends in a draw.

## Features

- Two-player functionality.
- Win and draw detection.
- Simple text-based interface.
- Validity checks to prevent overwriting cells.

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository or download the code file.
2. Run the game using Python from your terminal or command prompt.

### Running the Game

1. Open a terminal or command prompt.
2. Navigate to the folder where the code is saved.
3. Run the command:

   ```bash
   python tic_tac_toe.py
   ```

4. Follow the on-screen instructions to start playing.

## Game Rules

1. The board is numbered from 1 to 9 as follows:
    ```
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |
    ```
2. Players take turns entering a number between 1 and 9 to place their mark in the corresponding cell.
3. The game checks for a winner or a draw after each turn.
4. If a player wins, the game announces the winner and exits.
5. If there is a draw, the game announces it and exits.

## Code Explanation

- `board`: A list representing the 3x3 grid.
- `print_board()`: Displays the current state of the board.
- `check_winner(player)`: Checks if the specified player has won.
- `check_draw()`: Checks if the game is a draw.
- `tic_tac_toe()`: The main function that runs the game loop.

## Sample Gameplay

```
|   |   |   |
|   |   |   |
|   |   |   |

Player X's turn.
Enter a position (1-9): 1

| X |   |   |
|   |   |   |
|   |   |   |
```

## Contributing

Feel free to open an issue or submit a pull request if you have suggestions for improvements or additional features.
