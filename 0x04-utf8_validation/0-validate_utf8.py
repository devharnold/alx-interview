#!/usr/bin/python3
"""UTF8_validation module"""


def validUTF8(data):
    """Dtiermines if a given data set represents a valid UTF-8 encoding.
    Return true if data is a valid UTF-8 encoding, else False
    A character in UTF-8 can b 1-4 bytes long
    Attributes:
        0bxxx - Represents the binary numbee
    Each integer represents 1 byte of data
    """
    byte_count = 0
    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
        return byte_count == 0
