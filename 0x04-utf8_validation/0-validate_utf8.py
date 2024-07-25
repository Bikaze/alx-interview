#!/usr/bin/python3
""""This module contains a function that determines if a given data set
represents a valid UTF-8 encoding for one byte characters"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        if byte > 255:
            return False

        if (byte >> 7) == 0:
            # 1-byte character (ASCII), 0xxxxxxx
            i += 1
            continue
        elif (byte >> 5) == 0b110:
            # 2-byte character, 110xxxxx 10xxxxxx
            num_bytes = 2
        elif (byte >> 4) == 0b1110:
            # 3-byte character, 1110xxxx 10xxxxxx 10xxxxxx
            num_bytes = 3
        elif (byte >> 3) == 0b11110:
            # 4-byte character, 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
            num_bytes = 4
        else:
            return False

        if i + num_bytes >= n:
            return False

        for j in range(1, num_bytes):
            if i + j >= n or (data[i + j] >> 6) != 0b10:
                return False

        i += num_bytes

    return True
