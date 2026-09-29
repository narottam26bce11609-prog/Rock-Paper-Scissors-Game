# Problem Statement

Traditional Rock-Paper-Scissors is a simple hand game played between two people. There is a need for a digital version that allows a single user to play against a computer opponent anytime, without requiring another person. This project implements a command-line Rock-Paper-Scissors game in Python where the user competes against a randomly chosen computer move.

# Scope of the Project

The project focuses on creating a simple, interactive console-based game with the following boundaries:

- Single-player mode only (user vs computer)
- Basic game rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
- Text-based input and output (no GUI)
- Continuous play until the user chooses to quit
- Random computer choice using Python’s built-in `random` module
- Basic input validation for invalid choices

Out of scope:
- Multiplayer support
- Graphical user interface
- Score tracking across multiple sessions
- Advanced AI or difficulty levels
- Online/multiplayer networking

# Target Users

- Beginners learning Python programming
- Students looking for a simple project to understand basic concepts (loops, conditionals, user input, random module)
- Anyone who wants a quick, offline Rock-Paper-Scissors game in the terminal

# High-Level Features

- Interactive command-line interface
- User can choose Rock, Paper, or Scissors
- Computer generates a random choice
- Clear win / lose / draw result after each round
- Option to quit the game at any time by entering `q`
- Input validation with error message for invalid entries
- Continuous gameplay loop until the user exits
