#!/usr/bin/python3

"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    c = [1 for x in range(sorted(nums)[-1] + 1)]
    c[0], c[1] = 0, 0
    
    for j in range(2, len(c)):

        rm_multiples(c, j)

    for j in nums:

        if sum(c[0:j + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for j in range(2, len(ls)):

        try:
            ls[j * x] = 0
        except (ValueError, IndexError):
            break
