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
    :param compoundtimes_peryear: an integer
    :param years_to_grow: a float
    :precondition: principal must be a number that is positive or negative up to 2 decimal places
    :precondition: interest_rate must be a positive or negative number
    :precondition: compoundtimes_peryear must be an integer greater than 0
    :precondition: years_to_grow must be a number greater than 0
    :postcondition: the accurate raw number of money accrued over the years will be calculated
    :return: amount of money accrued in account as a float, raw number

    >>> compoundinterest(0, 0, 1, 0.1)
    0.0
    >>> compoundinterest(1000, 0.0, 2, 2) # 0 interest rate
    1000.0
    >>> compoundinterest(-10, -0.011, 1, 0.012) # principal and interest rate negative
    -9.998672774401053
    >>> compoundinterest(324_099, -1.5, 4, 1) # negative interest rate
    49453.582763671875
    >>> compoundinterest(1000, 0.1, 100, 100) # principal and interest rate positive
    21916681.339054313
    """
    accrued_money = principal * (1 + interest_rate / compoundtimes_peryear) ** (compoundtimes_peryear * years_to_grow)
    return accrued_money


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
