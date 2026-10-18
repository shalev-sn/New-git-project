# Tic-Tac-Toe

A two-player command-line tic-tac-toe game written in Python. Players take turns placing **X** and **O** on a 3×3 board until someone wins or the board is full.

Game prompts and messages are in Hebrew.

## Requirements

- Python 3

## How to run

From the project directory:

```bash
python tictactoe.py
```

On some systems you may need `python3` instead of `python`.

## How to play

1. Player **X** starts.
2. On each turn, enter a row and column as two numbers from `1` to `3`, separated by a space.

   Example: `1 2` places a mark in row 1, column 2.

3. Invalid moves (occupied cells, out of range, or bad input) are rejected and you try again.
4. The game ends when a player gets three in a row (horizontal, vertical, or diagonal) or when the board is full (draw).

## Files

- `tictactoe.py` — game logic and the command-line interface
