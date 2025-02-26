# Part1: Creating Hello Qantum

## Overview
This project is an implementation of the **Hello Quantum** game, designed to introduce the fundamentals of quantum computing through a puzzle-based approach. The project involves developing a Python program that manipulates a quantum board using quantum gates.

## Features
- Representation of a **quantum board** using tuples
- Implementation of three quantum **gates**: X, Z, and H
- Functions to manipulate and compare quantum boards
- Error handling for invalid inputs

## Installation
1. Ensure you have **Python 3** installed.
2. Clone the repository:
   ```sh
   git clone https://github.com/TomasCoheur/Foundations-of-Programming.git
   ```
3. Run the script:
   ```sh
   python Proj1.py
   ```
   or
   ```sh
   python Proj2.py
   ```
   

## Usage
The program applies quantum gates to modify the quantum board and helps users understand the effects of these operations.

Example functions:
```python
# Check if a given board is valid
is_valid = eh_tabuleiro(((-1, -1, -1), (1, 1, -1), (0, -1)))
print(is_valid)  # Output: True

# Apply an X gate to the left qubit
new_board = porta_x(existing_board, "E")
print(tabuleiro_str(new_board))
```

# Part2: Playing Hello Quantum 

## Overview

This project expands upon the **Hello Quantum** game by implementing a fully playable version in Python. The goal is to simulate quantum computation concepts through an interactive puzzle game, where users apply quantum gates to achieve target board states.

## Features

- **Abstract Data Types**: Implementation of cells, coordinates, and a quantum board.
- **Quantum Operations**: Support for X, Z, and H gates.
- **Game Functionality**: Interactive gameplay with win conditions.
- **Validation & Error Handling**: Ensuring correct moves and inputs.

## Usage

The game challenges players to transform an initial quantum board into a target board within a given number of moves using quantum gates.

Example functions:

```python
# Initialize a quantum board
tab = tabuleiro_inicial()
print(tabuleiro_para_str(tab))

# Apply an X gate to the left qubit
tab = porta_x(tab, "E")
print(tabuleiro_para_str(tab))

# Play the game with a target board and move limit
hello_quantum("((-1, -1, -1), (0, 1, -1), (1, -1)):3")
```

