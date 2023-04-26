#!/usr/bin/python3
"""[summary]"""

from sys import argv
argc = len(argv)


def nqueens(num, row, res):
    """Function"""

    if row == num:
        print(res)
    for col in range(num):
        if all(col != c and r + c != row + col and
                r - c != row - col for r, c in res):
            res.append([row, col])
            nqueens(num, row + 1, res)
            res.remove([row, col])


if __name__ == "__main__":
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        num = int(argv[1])
        if num < 4:
            print("N must be at least 4")
            exit(1)
    except Exception:
        print("N must be a number")
        exit(1)
    nqueens(num, 0, [])
