#!/usr/bin/python3

def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True for _ in range(n + 1)]
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = []
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        primes.append(c)

    players = {"Maria": 0, "Ben": 0}
    for i in range(len(nums)):
        c = primes[nums[i]]
        if c % 2 == 0:
            players["Maria"] += 1
        else:
            players["Ben"] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    if players["Maria"] < players["Ben"]:
        return "Ben"
    return None