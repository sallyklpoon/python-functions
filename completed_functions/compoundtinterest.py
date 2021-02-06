"""
Sally Poon A01232177
Date Completed: 02-06-2021

This module contains a compound interest calculator.

Note: due to the nature of round() varying in its rounding
    ex. round(1.345, 2) == 1.34
this module has opted to use "%.2f" to round a number to its closest decimal place.
"""
import doctest


def compoundinterest(principal, interest_rate, compoundtimes_peryear, years_to_grow):
    """Calculate the amount of money in the account after specified number of years.

    :param principal: any number
    :param interest_rate: a positive or negative float
    :param compoundtimes_peryear: an integer > 0
    :param years_to_grow: a float > 0
    :precondition: principal must be a number that is positive or negative up to 2 decimal places
    :precondition: interest_rate must be a positive or negative number
    :precondition: compoundtimes_peryear must be an integer greater than 0
    :precondition: years_to_grow must be a number greater than 0
    :postcondition: the amount of money accrued over the years will be calculated
    :return: amount of money accrued in account as a float to two decimal places

    >>> compoundinterest(0, 0, 1, 0.5)
    0.0
    >>> compoundinterest(-100.50, 0.25, 1, 0.012)
    -100.77
    >>> compoundinterest(-10, -0.011, 1, 0.012)
    -10.0
    >>> compoundinterest(324_099, -1.5, 4, 1)
    49453.58
    >>> compoundinterest(100.50, 1.678, 4, 3.25)
    9548.3
    >>> compoundinterest(-37, 80, 1, 1)
    -2997.0
    >>> compoundinterest(100, 1.1, 356, 1)
    299.91
    >>> compoundinterest(1, .01, 0.5, 300)
    19.5
    """
    return float("%.2f" % (principal * (1 + interest_rate / compoundtimes_peryear)
                 ** (compoundtimes_peryear * years_to_grow)))


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
