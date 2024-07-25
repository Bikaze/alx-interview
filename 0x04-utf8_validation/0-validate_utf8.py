#!/usr/bin/python3
""""This module contains a function that determines if a given data set
represents a valid UTF-8 encoding for one byte characters"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding
    for one byte characters"""
    check = [True if i < 256 else False for i in data if i >= 0]
    return all(check)
