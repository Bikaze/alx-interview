# 0x02. Minimum Operations

In this project, we delve into an algorithmic challenge that requires determining the fewest number of operations needed to achieve a specific goal in a text file. This problem serves as an excellent exercise in understanding dynamic programming and optimization techniques.

## Problem Statement

In a text file, there is a single character `H`. Your text editor can only execute two operations on this file: **Copy All** and **Paste**. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return 0

## Example

For `n = 9`, the sequence of operations is as follows:

`H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH`

Number of operations: 6

## Usage

To use the solution, you need to import the `minOperations` function into your Python script. This function is defined in a file named `0-minoperations.py`.

### Example Usage

Create a file named `0-main.py` for testing, with the following content:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

from 0-minoperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

### Running the Example
```bash
./0-main.py
```

### Expected Output

```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```

Cheers :)