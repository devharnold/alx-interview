#!/usr/bin/python3
"""NQueens problem"""
import sys

class NQueenProblem:
    def print_board(board):
        count = 0
        for row in board:
            for el in row:
                if el == 1:
                    count += 1
        
        #not a valid solution
        if count != len(board):
            return
        
        for row in board:
            for el in row:
                print(el, end=" ")
            print()

    def validate(board, i, j):
        #validate rows
        for c in range(j):
            if board[i][c] == 1:
                return False
        
        #validate columns
        for r in range(i):
            if board[r][j] == 1:
                return False
            
        r, c = i, j
        while c >= 0 and r >= 0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1
        return True
    
    def n_qeen(n):
        solutions = [] #Store valid solutions
        board = [[0] * n for _ in range(n)]
        stack = [] # simulate recursive calls
        row, col = 0, 0
        
        while True:
            #Try and place the queen in the current row
            while col < n:
                if NQueenProblem.validate(board, row, col):
                    board[row][col] = 1
                    stack.append((row, col))
                    col = 0
                    break
                col += 1
            else:
                if not stack: #No valid placement found and no backtrack possible
                    break
                row, col = stack.pop()
                board[row][col] = 0
                col += 1
                continue

            if row == n - 1:
                solution = [row[:] for row in board]
                solutions.append(solution)
                board[row][col] = 0
                col += 1

            row += 1

        for solution in solutions:
            NQueenProblem.print_board(solution)
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)


    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N is a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    NQueenProblem.n_queen(N)