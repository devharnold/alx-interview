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
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n