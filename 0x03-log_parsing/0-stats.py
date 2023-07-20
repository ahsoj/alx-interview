#!/usr/bin/python3
"""Log parsing"""

import sys

inputs = sys.stdin
cache = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
total_size = 0
count = 0


try:
    for inp in inputs:
        line = inp.split(" ")
        if len(line) > 4:
            code = line[-2]
            size = int(line[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            count += 1
        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))
            for key,value in sorted(cache.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

