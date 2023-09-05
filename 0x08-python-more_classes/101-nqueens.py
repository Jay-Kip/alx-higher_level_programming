#!/usr/bin/python3
import sys

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens_util(n, 0, board, solutions)

    for solution in solutions:
        print_solution(solution)

def solve_nqueens_util(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
    else:
        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col
                solve_nqueens_util(n, row + 1, board, solutions)
                board[row] = -1

def is_safe(row, col, board):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
        return True

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)


    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
