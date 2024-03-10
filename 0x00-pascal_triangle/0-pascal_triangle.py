#!/usr/bin/python3
"""
`--`Initialize a triangle & set the array empty
 -- Iterate through one row
 -- Set the first row = 1
 -- going to the next row, we add 1 row on to the right previous one
 -- iterate through the next and add another one
 -- a function to return all the rows created, given that we prev initialised it as an array
"""

def pascal_triangle(n):
    """  that returns a list of lists of integers representing the Pascal’s triangle of n"""
    triangle = []
    for row_num in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            next_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]
            row.append(next_row)
        triangle.append(row)
    return triangle



