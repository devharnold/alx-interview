#!/usr/bin/python3
"""makeChange module"""

def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number 
    of coins needed to meet a given amount total."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    result = 0
    i = 0
    while i < n and total > 0:
        result += total // coins[i]
        total %= coins[i]
        i += 1
    if total != 0:
        return -1
    return result