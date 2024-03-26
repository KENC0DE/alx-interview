#!/usr/bin/python3
"""
Log parsing
"""
import sys


log = {'ipAddress': [], 'fileSize': 0, 'statusCode': {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0}
    }

n_input = 0

while True:
    try:
        line = sys.stdin.readline().strip().split()
        n_input += 1
        nec = line[-2:]
        if len(line) < 5:
            continue

        stat_code = int(nec[0])
        file_size = int(nec[1])
        log['statusCode'][nec[0]] += 1
        log['fileSize'] += file_size
    except ValueError:
        continue
    except KeyboardInterrupt:
        print('File size: {}'.format(log['fileSize']))
        codes = log['statusCode']
        for key, val in codes.items():
            if val > 0:
                print('{}: {}'.format(key, val))

    if n_input == 10:
        print('File size: {}'.format(log['fileSize']))
        codes = log['statusCode']
        for key, val in codes.items():
            if val > 0:
                print('{}: {}'.format(key, val))

        n_input = 0
