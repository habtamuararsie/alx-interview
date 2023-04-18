#!/usr/bin/python3
"""
Module
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    binaryList = ['{:0>8}'.format(str(bin(n))[2:]) for n in data]

    for character in binaryList:
        ones = 0
        if character[0] == '0':
            continue
        for bit in character:
            if bit == '0':
                break
            ones += 1
        if ones > 4 or ones == 1:
            return False
        if character[ones+1] == '0':
            for byte in binaryList[1:]:
                if byte[:2] != '10':
                    return False
        else:
            return False
    return True