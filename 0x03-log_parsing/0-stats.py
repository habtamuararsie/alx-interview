#!/usr/bin/python3
"""  a script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""


import sys


def display_message(status_code, file_size):
    """
    Method to display
    Args:
        dictionary_source: dict of status codes
        file_size: total of the file
    Returns:
        Nothing to display
    """


try:
    print("File size: {}".format(file_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))
except Exception:
    pass

fileSize = 0
message_code = 0
count = 0
status_code = {"200": 0,
          "301": 0,
          "400": 0,
          "401": 0,
          "403": 0,
          "404": 0,
          "405": 0,
          "500": 0}

try:

    for line in sys.stdin:
        pars_line = line.split()
        pars_line = pars_line[::-1]

        if len(pars_line) > 2:
            count += 1

            if count <= 10:
                fileSize += int(pars_line[0])
                message_code = pars_line[1]

                if (message_code in status_code.keys()):
                    status_code[message_code] += 1

            if (count == 10):
                display_message(status_code, fileSize)
                count = 0

finally:
    display_message(status_code, fileSize)
