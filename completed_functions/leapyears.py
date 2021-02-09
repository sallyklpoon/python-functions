"""
Sally Poon A01232177
Date Completed: 02-06-2021

Module contains a function to calculate how many leap years are in a range of given years.

This module requires the import of calendar to use the calendar.leapdays(a,b) function
"""
import calendar
import doctest


def leapyears(lower_bound, upper_bound):
    """Calculate the number of leap years in a given range.

    Range determined by lower and upper bound parameters passed.

    :param lower_bound: an integer
    :param upper_bound: an integer
    :precondition: lower_bound passed is an integer that is > 0 and <= upper_bound.
    :precondition: upper_bound passed is an integer > 0.
    :postcondition: produce the correct number of leap years within the given range
    :return: an integer representing the number of leap years within the given range

    >>> leapyears(2021, 2021)
    0
    >>> leapyears(2004, 2004)
    1
    >>> leapyears(1001, 1009)
    2
    >>> leapyears(1897, 1903)
    0
    >>> leapyears(2000, 2020)
    6
    """
    return calendar.leapdays(lower_bound, upper_bound + 1)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
