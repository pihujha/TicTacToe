# Tic-Tac-Toe Game README

## Overview
This is a console-based implementation of the classic game Tic-Tac-Toe. Players take turns to place their mark (X or O) on a 3x3 grid, with the objective of getting three marks in a row, column, or diagonal.

## How to Play

1. **Starting the Game**:
    - Run the game script.
    - You will be prompted to choose the game mode.

2. **Selecting a Game Mode**:
    - **Mode 1**: Player vs Player.
    - **Mode 2**: Player vs Computer.

3. **Gameplay**:
    - The game board is represented by a list of 9 positions, indexed from 0 to 8.
    - Players take turns to choose a position on the board to place their mark.
    - The game continues until one player gets three marks in a row, column, or diagonal, or the board is full (tie).

4. **Winning and Losing**:
    - Win by getting three of your marks in a row, column, or diagonal.
    - The game ends in a tie if the board is full and no player has won.
    - After each game, you can choose to play again or exit.

## Code Structure

### Player Classes
- **`Player`**: Base class for both human and computer players.
  - `letter`: The player's mark, either 'X' or 'O'.
  - `get_move(game)`: Method to get the next move. To be implemented by subclasses.
- **`RandomComputerPlayer`**: Inherits from `Player`. Chooses a move randomly from available moves.
- **`HumanPlayer`**: Inherits from `Player`. Prompts the user to input a move.

### Game Class
- **`TicTacToe`**: Represents the Tic-Tac-Toe game.
  - `board`: List of 9 elements representing the game board.
  - `current_winner`: Tracks the current winner of the game.
  - `print_board()`: Prints the current state of the board.
  - `print_board_nums()`: Prints the board positions (0-8).
  - `available_moves()`: Returns a list of available moves.
  - `empty_squares()`: Checks if there are any empty squares.
  - `num_empty_squares()`: Returns the number of empty squares.
  - `make_move(square, letter)`: Makes a move on the board.
  - `winner(square, letter)`: Checks if the current move wins the game.

### Game Functions
- **`play(game, x_player, o_player, print_game=True)`**: Core function to handle the game loop.
- **`choose_game_mode()`**: Prompts the user to choose the game mode.
- **`play_again()`**: Prompts the user to play again or exit.
- **`main()`**: Main function to run the game.

## Running the Game

To run the game, ensure you have Python installed on your system. Save the game script to a file (e.g., `tictactoe.py`), and execute it using the Python interpreter:

```bash
python tictactoe.py
```

## Credits
This game has been created by Pihu Jha. Enjoy playing!
