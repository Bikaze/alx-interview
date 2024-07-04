# Lockboxes Solution

## Introduction

This repository contains a Python solution to the lockboxes problem, a challenging puzzle that tests one's ability to work with data structures and algorithms. The problem involves a series of locked boxes, each of which may contain keys to unlock other boxes. The goal is to determine whether all the boxes can be unlocked.

## Problem Statement

You are presented with `n` locked boxes, each numbered sequentially from `0` to `n - 1`. Inside any given box, there may be keys to other boxes. The challenge is to write a method that determines if all the boxes can be opened.

### Specifications:

- **Prototype:** `def canUnlockAll(boxes)`
- **Parameters:** `boxes` is a list of lists, where each sublist contains keys.
- **Key Rules:**
    - A key with the same number as a box opens that box.
    - All keys are positive integers.
    - There may be keys that do not correspond to any box.
- **Initial Condition:** The first box (`boxes[0]`) is unlocked.
- **Return Value:** The method returns `True` if all boxes can be opened, otherwise `False`.

## Solution Overview

The solution is implemented in the `0-lockboxes.py` file, which defines the `canUnlockAll` function. This function takes a list of lists as input, where each sublist represents the keys contained within a box. It then determines whether it is possible to unlock all boxes given these keys.

## Example Usage

To see the `canUnlockAll` function in action, you can use the `main_0.py` script. This script demonstrates how to import and use the function with different sets of boxes to determine if all can be unlocked.

### Script Content

The `main_0.py` script contains the following code:

```python
#!/usr/bin/python3

# Import the canUnlockAll function from the 0-lockboxes module
canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Example 1
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Example 2
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

# Example 3
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
```

## Running the Script

To execute the `main_0.py` script and see the `canUnlockAll` function in action:

1. Open your terminal.
2. Navigate to the directory where `main_0.py` is located.
3. Run the script by typing the following command:

    ```bash
    ./main_0.py