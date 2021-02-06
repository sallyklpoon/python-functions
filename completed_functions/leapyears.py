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

    >>> leapyears(1, 1)
    0
    >>> leapyears(2019, 2020)
    0
    >>> leapyears(2021, 2021)
    0
    >>> leapyears(1921, 2021)
    25
    >>> leapyears(1, 2020)
    489
    """
    return calendar.leapdays(lower_bound, upper_bound)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
