#!/usr/bin/python3
"""
This module contains a function `makeChange` that determines the fewest number
of coins needed to make up a given total amount using a combination of greedy
and dynamic programming approaches.
If the amount cannot be met by any combination of the available coins,
the function returns -1.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of integers representing the denominations of the
                      coins.
        total (int): The total amount of money to be made.

    Returns:
        int: The fewest number of coins needed to make up the total amount.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            count += remaining // coin  # Use as many of this coin as possible
            remaining %= coin  # Get the remaining amount

    # Check if the exact total was reached
    if remaining == 0:
        return count
    else:
        return -1
