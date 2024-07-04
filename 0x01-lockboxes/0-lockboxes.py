#!/usr/bin/python3

"""
This module contains a function to solve the "lockboxes" problem. The problem
asks whether all boxes can be unlocked given a set of boxes, each containing
keys to other boxes. The first box (index 0) is initially unlocked.

Functions:
    canUnlockAll(boxes): Determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Starting with the first box (index 0), this function iterates through each
    box. If the current box can be unlocked (its index is in the list of keys
    we have), it iterates through the keys in the box. Each new key found is
    added to our list of keys, allowing us to unlock more boxes.

    Parameters:
        boxes (list of list of int): A list where each element is a list of
                                     integers representing the keys in a box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]
    for boxIndex in range(len(boxes)):
        if boxIndex in keys:
            for key in boxes[boxIndex]:
                if key not in keys:
                    keys.append(key)
                    keys += boxes[key]
        else:
            return False
    return True
