#!/usr/bin/python3
"""
This module contains a function `makeChange` that determines the fewest number
of coins needed to make up a given total amount using dynamic programming.
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

    # Sort coins to attempt using larger denominations first (greedy approach)
    coins.sort(reverse=True)

    # Initialize a list to store the minimum number of coins needed for each
    # amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make the amount 0

    # Iterate over each coin in the list
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made up
    # by any combination of the coins
    return dp[total] if dp[total] != float('inf') else -1
