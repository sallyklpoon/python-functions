"""
Sally Poon A01232177
Date Completed: 02-06-2021

This module contains a compound interest calculator.

Note: this code will produce raw compoundinterest number without rounding.
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
    :postcondition: the accurate raw number of money accrued over the years will be calculated
    :return: amount of money accrued in account as a float, raw number

    >>> compoundinterest(0, 0, 1, 0.5)
    0.0
    >>> compoundinterest(-100.50, 0.25, 1, 0.012)
    -100.76947174716699
    >>> compoundinterest(-10, -0.011, 1, 0.012)
    -9.998672774401053
    >>> compoundinterest(324_099, -1.5, 4, 1)
    49453.582763671875
    >>> compoundinterest(100.50, 1.678, 4, 3.25)
    9548.303632583229
    >>> compoundinterest(-37, 80, 1, 1)
    -2997.0
    >>> compoundinterest(100, 1.1, 356, 1)
    299.9075439755226
    >>> compoundinterest(1, .01, 0.5, 300)
    19.4996027667626
    """
    return principal * (1 + interest_rate / compoundtimes_peryear) ** (compoundtimes_peryear * years_to_grow)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
