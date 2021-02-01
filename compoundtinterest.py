"""This module contains a compound interest calculator."""


def compoundinterest(principal, interest_rate, compoundtimes_peryear, years_to_grow):
    """Calculate the amount of money in the account after specified number of years.

    :param principal: a positive or negative float, amount of money originally in account
    :param interest_rate: a positive or negative float, annual interest rate
    :param compoundtimes_peryear: an integer > 0, times per year interest is compounded
    :param years_to_grow: a float > 0, time in years account will be left to grow
    :preconditions: principal must be a number
                    interest_rate must be a positive or negative number
                    compoundtimes_peryear must be an integer greater than 0
                    years_to_grow must be a number greater than 0
    :postcondition: the amount of money accrued over the years will be calculated
    :return: amount of money accrued in account as a float to two decimal places
    """
    accrued_amount = principal * (1 + interest_rate / compoundtimes_peryear) \
        ** (compoundtimes_peryear * years_to_grow)
    return "%.2f" % accrued_amount


def main():
    print(compoundinterest(10_000, 3.875, 12, 7.5))
    print(compoundinterest(324_099, -1.5, 4, 1))
    print(compoundinterest(-37, 2.33, 3, 3))


if __name__ == '__main__':
    main()
