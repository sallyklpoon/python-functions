"""
Sally Poon ; A01232177
Date Completed: 02-05-2021

This module contains a function that will create a list of 6 unique random numbers [1, 49].

The sample() function from the random library has been imported.

For unit test, run test_lottery.py
"""

from random import sample
import doctest  # See test lottery for unit test


def lottery():
    """Produce a list of 6 unique and random numbers in range [1,49].

    :precondition: user calls lottery()
    :postcondition: produce a list of 6 unique and random numbers within the range of [1,49]
    :return: list of 6 unique and random numbers in the range [1, 49]
    """
    lottery_numbers = sample(range(1, 50), k=6)
    return sorted(lottery_numbers)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
