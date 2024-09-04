#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determine the winner of the game"""
    if x == 0 or not nums:
        return None

    def sieve_of_eratosthenes(max_n):
        """Sieve of Eratosthenes algorithm"""
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False
        for start in range(2, int(max_n**0.5) + 1):
            if sieve[start]:
                for i in range(start * start, max_n + 1, start):
                    sieve[i] = False
        return sieve

    max_n = max(nums)
    prime_sieve = sieve_of_eratosthenes(max_n)

    def count_prime_picks(n):
        # Count how many primes are there up to `n`
        prime_count = 0
        for i in range(2, n + 1):
            if prime_sieve[i]:
                prime_count += 1
        return prime_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_picks = count_prime_picks(n)
        if prime_picks % 2 == 0:
            ben_wins += 1  # Ben wins when prime_picks are even
        else:
            maria_wins += 1  # Maria wins when prime_picks are odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
