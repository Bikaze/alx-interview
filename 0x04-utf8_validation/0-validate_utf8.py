#!/usr/bin/python3
""""This module contains a function that determines if a given data set
represents a valid UTF-8 encoding for one byte characters"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    num_bytes = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            else:
                num_bytes -= 1

    return num_bytes == 0
