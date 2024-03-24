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
    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2 
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard 
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count

