#!/usr/bin/python3
"""N queens puzzle"""

import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif sys.argv[1].isdigit():
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
else:
    print("N must be a number")
    sys.exit(1)


def format_solution(board):
    """Format the board into a list of positions for each queen."""
    return [[row, col] for row in range(len(board))
            for col in range(len(board[row])) if board[row][col]]


def is_valid(board, row, col, N):
    """Check if placing a queen at (row, col) is valid."""
    # Check this column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    """Use backtracking to solve N-Queens problem and store solutions."""
    if row >= N:
        solutions.append(format_solution(board))
        return True

    solved = False
    for col in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = True
            if solve_nqueens(board, row + 1, N, solutions):
                solved = True
            board[row][col] = False

    return solved


def nqueens(N):
    """Solve the N-Queens problem and return solutions in the desired format"""
    board = [[False] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


nqueens(N)
