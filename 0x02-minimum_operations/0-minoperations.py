#!/usr/bin/python3
import os
"""
minOperations module
"""

def minOperations(n):
    """A single character H
    Text editor can only execute two operations in this file
    `Copy All` and `Paste`
    Given a number n, a method that calculates fewest number of
    operations needed to result in exactly n H characters in the file
    """
    if n == 0:
        return 0
    
    min_op = 0
    while n % 2 == 0:
        min_op += 1
        n // 2

    if n > 1:
        option1 = 1 + minOperations(n - 1)
        option2 == 0
        if n % 3 == 0:
            option2 = 1 + minOperations(n // 3)
        min_op += min(option1, option2)
    return min_op