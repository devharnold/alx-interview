#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """Rotate 2-D matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): The matrix expected
    """
    n = len(matrix)
    for i in range(n // 2):
        y = n - i - 1
        for j in range(i, y):
            x = n - 1 - j
            #curr num
            tmp = matrix[i][j]
            #alter the top-left
            matrix[i][j] = matrix[x][i]
            #alter left-bottom
            matrix[x][i] = matrix[y][x]
            #alter bottom-right
            matrix[y][x] = matrix[j][y]
            #alter right-top
            matrix[j][y] = tmp