#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determine the winner of the game."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes algorithm to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, max_n + 1, start):
                sieve[i] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1  # No primes, Ben wins automatically
        elif prime_count[n] % 2 == 0:
            ben_wins += 1  # Ben wins if prime count is even
        else:
            maria_wins += 1  # Maria wins if prime count is odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
