# Connect 4 with Minimax AI

A classic Connect 4 game implementation in Python using the Pygame library and an AI opponent powered by the Minimax algorithm with Alpha-Beta pruning.

## Features
- **Graphical User Interface (GUI)**: Built with Pygame for smooth gameplay.
- **Smart AI**: Challenging AI opponent using Minimax algorithm.
- **Interactive Gameplay**: Mouse control to drop pieces.

## Prerequisites
- Python 3.x
- **Pygame** library

To install the required libraries, run:
```bash
pip install pygame-ce numpy
```

> **Note**: This project uses `pygame-ce` (Community Edition) which is compatible with the latest Python versions.

## How to Run
Navigate to the project directory and run the `main.py` file:
```bash
python main.py
```

## How to Play
1.  The game starts with a random turn (Player or AI).
2.  **Player (Red)**: Move your mouse to position the piece and click to drop it into a column.
3.  **AI (Yellow)**: The AI will automatically calculate and make its move.
4.  The goal is to connect 4 pieces of your color horizontally, vertically, or diagonally.
5.  The game announces the winner when a Connect 4 is achieved.

## Project Structure
- `main.py`: Entry point of the game.
- `constants.py`: Game constants (colors, dimensions).
- `board.py`: Game logic and board management.
- `ai.py`: Minimax AI implementation.
- `gui.py`: Pygame rendering functions.
