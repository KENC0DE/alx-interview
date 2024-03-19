#!/usr/bin/python3
"""
0. Minimum Operations
"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def minOperations(n):
    """
    Calculate the minimum number of
    operations needed to obtain n 'H' characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations needed,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0
    if n in [2, 3, 4]:
        return n

    if is_prime(n):
        return n

    if n % 2 == 0:
        if n % 4 != 0:
            return n // 2 + 2
        else:
            return n // 2 + 1

    if n % 2 != 0:
        return (n - 1) // 2 + 1
