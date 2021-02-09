"""
Sally Poon A01232177
Date Completed: 02-06-2021

Module includes a function called moneychanger and roundoff_pennies.
    round_off pennies will round given dollar amount to closes nickel or dime.
    moneychanger will produce a list of change needed to cover a total dollar amount.

This module requires the imported function trunc from Python's math library.
"""
import doctest
from math import trunc


def roundoff_pennies(total_dollars):
    """Round out pennies from given dollar amount.

    :param total_dollars: a floating point number
    :precondition: total_dollars value is a floating point >= 0.00 with 2 decimals
    :postcondition: return the total_dollars value rounded off without pennies (to the closest multiple of 5 cents)
    :return: a floating point of dollar amount rounded to closest nickel, dime, or dollar to 2 decimal places

    >>> roundoff_pennies(0.00)
    0.0
    >>> roundoff_pennies(0.01)
    0.0
    >>> roundoff_pennies(0.02)
    0.0
    >>> roundoff_pennies(0.03)
    0.05
    >>> roundoff_pennies(0.04)
    0.05
    >>> roundoff_pennies(0.05)
    0.05
    >>> roundoff_pennies(0.06)
    0.05
    >>> roundoff_pennies(0.07)
    0.05
    >>> roundoff_pennies(0.08)
    0.1
    >>> roundoff_pennies(0.09)
    0.1
    >>> roundoff_pennies(0.10)
    0.1
    >>> roundoff_pennies(999.99)
    1000.0
    >>> roundoff_pennies(1023.29)
    1023.3
    >>> roundoff_pennies(698.40)
    698.4
    """
    hundredths = int(str(total_dollars)[-1])
    if str(total_dollars)[-2] == ".":
        # Adjust for the stripped 0 at the end if total_dollars ends with 0
        # ex. in Python, inputted total_dollars 12.50 will become 12.5
        return total_dollars
    elif hundredths in range(1, 3):
        return round(total_dollars, 1)
    elif hundredths in range(3, 8):
        return round(total_dollars + (0.05 - hundredths * 10 ** -2), 2)
    else:  # hundredths in range(8, 10)
        return round(total_dollars + (0.10 - hundredths * 10 ** -2), 2)


def moneychanger(total_dollars):
    """Produce list of change in Canadian currency to cover total_dollars amount with the fewest of each bill
    and coin.

    :param total_dollars: a floating point number
    :precondition: total_dollars value is a floating point >= 0.00 with up to 2 decimal places
    :postcondition: return accurate breakdown of Canadian currency to cover the total_dollars amount
                    in a list from largest currency amount to smallest.
    :return: a list with the number of each currency required following this format...
            [$100-bill, $50-bill, $20-bill, $10-bill, $5-bill, $2, $1, 0.25 cents, 0.10 cents, 0.05 cents]

    Test that conversions work:
    >>> moneychanger(0.05)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    >>> moneychanger(0.10)
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    >>> moneychanger(0.25)
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    >>> moneychanger(1.00)
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    >>> moneychanger(2.00)
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    >>> moneychanger(5.00)
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    >>> moneychanger(10.00)
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    >>> moneychanger(20.00)
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    >>> moneychanger(50.00)
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> moneychanger(100.00)
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    Test other cases to combine
    >>> moneychanger(0.00)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> moneychanger(0.01)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> moneychanger(0.58)
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 0]
    >>> moneychanger(188.40) #should return all 1’s in the list
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> moneychanger(999_999_999.99)
    [10000000, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    canadian_change = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05]
    output_change = []
    total_dollars = roundoff_pennies(total_dollars)
    for change_value in canadian_change:
        output_change.append(trunc(total_dollars // change_value))
        total_dollars = round((((total_dollars / change_value)
                                - (total_dollars // change_value)) * change_value), 2)
    return output_change


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    # Run main() if module is being run as program
    main()
