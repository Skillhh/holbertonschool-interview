#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ minOperations

    n:  (int) number to operate
    Return
        ops: (int)number of operations.
    """
    ops = 0
    if n == 0:
        return 0
    else:
        for i in range(2, n + 1):
            while n % i == 0:
                ops += i
                n /= i
        return ops