#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_stats(fileSize, statusCode):
    """Print the currenct stats"""
    print('File size: {}'.format(fileSize))
    for key, val in statusCode.items():
        if val != 0:
            print('{}: {}'.format(key, val))


fileSize = 0
statusCode = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}

n_input = 0

try:
    for line in sys.stdin:
        m_line = line.strip().split()
        nec = m_line[-2:]
        if len(m_line) >= 5:
            n_input += 1

            stat_code = int(nec[0])
            file_size = int(nec[1])
            statusCode[nec[0]] += 1
            fileSize += file_size

            if n_input == 10:
                print_stats(fileSize, statusCode)

                n_input = 0
except ValueError:
    pass
finally:
    print_stats(fileSize, statusCode)
