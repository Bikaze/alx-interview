#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """Determine who wins the most rounds in the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of `n` values for each round.

    Returns:
        str: 'Maria' if Maria wins more rounds, 'Ben' if Ben wins more rounds,
              or None if they win an equal number of rounds or no rounds.
    """

    def compute_primes_up_to(max_n):
        """Compute all primes up to a given number using the Sieve of
        Eratosthenes.

        Args:
            max_n (int): The maximum number to compute primes up to.

        Returns:
            list of int: List of prime numbers up to `max_n`.
        """
        if max_n < 2:
            return []

        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1

        primes = [p for p in range(max_n + 1) if is_prime[p]]
        return primes

    if not nums:
        return None

    # Determine the maximum value of n in the input
    max_n = max(nums)

    # Compute all primes up to the maximum value of n
    primes = compute_primes_up_to(max_n)

    # Create a list to store the number of primes up to each number
    # from 1 to max_n
    num_primes_up_to = [0] * (max_n + 1)
    prime_count = 0
    for i in range(1, max_n + 1):
        if i in primes:
            prime_count += 1
        num_primes_up_to[i] = prime_count

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            prime_count = num_primes_up_to[n]
            if prime_count % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
