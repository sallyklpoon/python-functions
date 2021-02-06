"""Module includes a function called moneychanger and roundoff_pennies.

round_off pennies will round given dollar amount to closes nickel or dime.

moneychanger will produce a list of change needed to cover a total dollar amount.

This module requires the imported function trunc from Python's math library.

Canadian_cash defines as a global list of cash amounts available in canadian currency.
"""
from math import trunc


def roundoff_pennies(total_dollars):
    """Round out pennies from given dollar amount.

    :param total_dollars: a positive floating point number with 2 decimals
    :precondition: total_dollars value is a floating point >= 0.00 with 2 decimals
    :postcondition: return the total_dollars value rounded off without pennies
    :return: a floating point of dollar amount rounded to closest nickel, dime, or dollar to 2 decimal places
    """
    hundredths = int(str(total_dollars)[-1])
    if str(total_dollars)[-2] == ".":
        # Adjust for the stripped 0 at the end if total_dollars ends with 0
        # ex. inputted total_dollars 12.50 will become 12.5
        return total_dollars
    elif hundredths % 5 == 0:
        return total_dollars
    elif hundredths in range(1, 3):
        return round(total_dollars, 1)
    elif hundredths in range(3, 5):
        return round(total_dollars + round((0.05 - hundredths * 10 ** -2), 2), 2)
    elif hundredths in range(6, 8):
        return round(total_dollars + round((0.05 - hundredths * 10 ** -2), 2), 2)
    else:  # hundredths in range(8, 10)
        return round(total_dollars + round((.10 - hundredths * 10 ** -2), 2), 2)


def moneychanger(total_dollars):
    """Produce list of change in Canadian currency to cover total_dollars amount.

    :param total_dollars: a positive floating point number with 2 decimals
    :precondition: total_dollars value is a floating point >= 0.00 with 2 decimals
    :postcondition: return accurate breakdown of Canadian currency to cover the total_dollars amount
                    in a list from largest currency amount to smallest.
    :return: a list with the number of each currency required following this format...
            [$100-bill, $50-bill, $20-bill, $10-bill, $5-bill, $2, $1, 0.25 cents, 0.10 cents, 0.05 cents]
    """
    canadian_change = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05]
    output_change = []
    total_dollars = roundoff_pennies(total_dollars)
    for change_value in canadian_change:
        output_change.append(trunc(total_dollars // change_value))
        total_dollars = round((((total_dollars / change_value) - (total_dollars // change_value)) * change_value), 2)
    return output_change


def main():
    total_dollars = 999.97
    print(roundoff_pennies(total_dollars))
    print(moneychanger(total_dollars))

    # print(roundoff_pennies(999.99))
    # print(int(str(total_dollars)[-1]))
    # print(roundoff_pennies(999.80))
    # print(roundoff_pennies(999.93))
    # print(roundoff_pennies(999.95))
    # print(10 % 5)
    # print(999.97 + round((0.05 - 7 * 10 ** -2), 2))
    pass


if __name__ == '__main__':
    main()
