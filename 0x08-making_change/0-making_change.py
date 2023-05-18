#!/usr/bin/python3
"""" A modul which solves coin problem """


def makeChange(coins, total):
    """
    number of coins needed to meet a given total coin number if total 
    """
    
    if total <= 0:
        return 0

    dpl = [float('inf')] * (total + 1)
    dpl[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dpl[i] = min(dpl[i], dpl[i - coin] + 1)

    if dpl[total] == float('inf'):
        return -1
    else:
        return dpl[total]
