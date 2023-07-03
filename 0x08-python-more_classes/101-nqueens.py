#!/usr/bin/python3
# 101-nqueens.py

import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at the given position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Initialize an empty board"""
    board = [-1] * n
    solutions = []

    def place_queen(row):
        """Recursive function to place queens row by row"""
        if row == n:
            solutions.append(board.copy())
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queen(row + 1)

    place_queen(0)

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(' '.join(str(col + 1) for col in solution))
