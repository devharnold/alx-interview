#!/usr/bin/python3
import os
"""
minOperations module
"""

def minOperations(n):
    """function that computes the fewest number of ops
    to result in exactly n H characters.
    
    Args:
    n (int): The desired number of H characters.
    Returns:
    int: The fewest number of ops needed
    """
    if not isinstance(n, int):
        return 0
    #set op_count => `operations_count` to 0
    op_count = 0
    clipboard = 0
    done = 1

    for done in range(1, n + 1):
        if clipboard == 0:
            clipboard = done
            op_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            op_count += 2
        elif clipboard > 0:
            op_count += 1
    return op_count



print(minOperations(3))