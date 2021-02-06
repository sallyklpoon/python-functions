"""
Sally Poon A01232177
Date Completed: 02-06-2021

This module contains a function that uses Eratosthenes method
of finding a list of prime numbers given a range from [0, n].

This module requires the import of math.sqrt() and math.ceil() functions
from the math library.
"""
import doctest
from math import sqrt, ceil


def eratosthenes(upper_bound):
    """Determine the prime numbers within range 0 to given upper_bound.

    :param upper_bound: a positive integer
    :precondition: a positive integer is passed as an argument
    :postcondition: return a correct list of prime numbers up to upper_bound range
    :return: a list of prime numbers up to the upper_bound range

    >>> eratosthenes(1)
    []
    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    number_list = list(range(2, upper_bound + 1))
    evaluating_numbers = list(range(2, ceil(sqrt(upper_bound))))
    for evaluating_number in evaluating_numbers:
        for number in number_list:
            if number != evaluating_number and number % evaluating_number == 0:
                number_list.remove(number)
    return number_list


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()

