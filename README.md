# Proj 1: Hello Quantum - Python Implementation

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
   git clone https://github.com/yourusername/hello-quantum.git
   ```
3. Navigate to the project directory:
   ```sh
   cd hello-quantum
   ```
4. Run the script:
   ```sh
   python main.py
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
