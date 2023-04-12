#!/usr/bin/python3
"""Module
"""
import sys


def printStatus(status, fileSize):
    """
    print the stats and size.
    """
    try:
        print('File size: {}'.format(fileSize))
        [print("{}: {}".format(k, v))
         for k, v in sorted(status.items()) if v != 0]
    except Exception:
        pass


status = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
fileSize = 0
words = []
try:
    for i, line in enumerate(sys.stdin, 1):
        words = line.split(' ')

        try:
            if (words[-2].isdigit() and words[-2] in status.keys()):
                status[words[-2]] += 1

            fileSize += int(words[-1].replace('\n', ''))
        except Exception:
            pass
        if i % 10 == 0:
            printStatus(status, fileSize)
    printStatus(status, fileSize)
except KeyboardInterrupt:
    printStatus(status, fileSize)
    raise
