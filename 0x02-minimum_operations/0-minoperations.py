#!/usr/bin/python3
"""
0. Minimum Operations
"""


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

    ops = {'copy': 0, 'paste': 0}
    chrs = 1  # Start with one 'H' character

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
        else:
            return n

    if n % 2 == 0:
        if n % 4 != 0:
            return n // 2 + 2
        else:
            return n // 2 + 1

    # continue her for odd n.
