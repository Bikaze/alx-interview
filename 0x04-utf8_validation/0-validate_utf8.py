#!/usr/bin/python3


def validUTF8(data):
    check = [True if i < 256 else False for i in data]
    return all(check)
