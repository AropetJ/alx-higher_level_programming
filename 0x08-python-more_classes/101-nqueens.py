#!/usr/bin/python3
# 101-nqueens.py

import sys


def is_safe(board, row, col):
    """The method checks if it's safe to place a queen at board[row][col]"""
    """Check the left side of the current column"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    """Check the upper diagonal on the left side"""
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """Check the lower diagonal on the left side"""
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    """It's safe to place a queen at board[row][col]"""
    return True


def solve_nqueens(board, col):
    """ The method solves the N Queens problem using backtracking"""
    """Base case: If all queens are placed, print the solution"""
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    """Try placing a queen in each row of the current column"""
    for row in range(N):
        if is_safe(board, row, col):
            """Place the queen at board[row][col]"""
            board[row][col] = 1

            """Recur to place the rest of the queens"""
            solve_nqueens(board, col + 1)

            """Backtrack and remove the queen from board[row][col]"""
            board[row][col] = 0


def print_solutions(solutions):
    """Print the solutions to the N Queens problem"""
    for solution in solutions:
        print(solution)


"""Check if the correct number of arguments is provided"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

"""Read the value of N from the command line argument"""
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

"""Check if N is at least 4"""
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

"""Initialize an empty chessboard of size N x N"""
board = [[0 for _ in range(N)] for _ in range(N)]

"""List to store the solutions"""
solutions = []

"""Solve the N Queens problem"""
solve_nqueens(board, 0)

"""Print the solutions"""
print_solutions(solutions)
