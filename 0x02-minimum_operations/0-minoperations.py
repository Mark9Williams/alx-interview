#!/usr/bin/python3
"""fewest number of operations needed to result in exactly n H characters"""


def minOperations(n):
    """fewest number of operations needed to result in n H characters"""
    if n <= 1:
        return 0

    operations = 0
    # Start checking for factors from 2
    factor = 2

    while n > 1:
        # If factor is a divisor of n
        if n % factor == 0:
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n
        else:
            factor += 1  # Move to the next factor

    return operations
