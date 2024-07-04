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
    Determines if all boxes can be opened given a list of lists, where each
    inner list contains keys to other boxes.

    Parameters:
    boxes (list of list of int): A list where each element is a list of
                                 integers representing the keys in a box.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    unlocked = [False] * len(boxes)  # Track unlocked status for each box
    unlocked[0] = True  # The first box is always unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while True:
        changes = False  # Track if any new box was unlocked in this iteration
        newKeys = []
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Unlock the box with the current key
                newKeys += boxes[key]  # Add new keys found in this box
                changes = True
        keys.update(newKeys)
        if not changes:  # If no new boxes were unlocked, stop the loop
            break

    return all(unlocked)  # Return True if all boxes are unlocked, else False
