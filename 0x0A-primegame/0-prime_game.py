#!/usr/bin/python3

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    n = max(nums)
    prime = [True for i in range(max(n + 1, 2))]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    c = 0
    for i in range(len(prime)):
        if prime[i]:
            c += 1
        prime[i] = c
    c = 0
    for n in nums:
        c += prime[n] % 2 == 0
    if c * 2 == len(nums):
        return None
    if c * 2 > len(nums):
        return "Maria"
    return "Ben"