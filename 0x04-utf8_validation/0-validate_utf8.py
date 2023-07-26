#!/usr/bin/python3
"""UTF8 Validation"""


def validUTF8(data):
    """Validates UTF-8 data."""
    n_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for d in data:
        mask_byte = mask_1
        if n_bytes == 0:
            while mask_byte & d:
                n_bytes += 1
                mask_byte = mask_byte >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        elif not (d & mask_1 and not (d & mask_2)):
            return False
        n_bytes -= 1
    if n_bytes == 0:
        return True
    return False
