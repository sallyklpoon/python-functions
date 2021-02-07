"""
Sally Poon A01232177
Date Completed: 02-05-2021

This module contains the function romannumeral() and its helper functions.

The goal of the function is to convert a given integer in range [1, 10_000] to a
Roman Numeral. Given the pattern that roman numerals have unique characters for the
collection of power of 10s and 5* power of 10s, lists have been created for
these letters to be used during the conversion.
"""
import doctest

romannumeral_power10s = ["I", "X", "C", "M"]     # in integer: 100, 10, 1, 1000
romannumeral_5power10s = ["V", "L", "D"]         # in integer: 500, 50, 5


def romannumeral_1to9_loop(positive_digit, place_value):
    """Produce the roman numeral representation of an integer [1, 9] given its
    place_value in a complete number.

    Each digit in a base10 number can only be [1, 9], function will translate
    these numbers to its roman numeral equivalent by use of importing the
    roman numeral 1 value and roman numeral 5 value for a given place_value.
    
    :param positive_digit: an integer [1, 9]
    :param place_value: an integer [0, 2]
    :precondition: the positive digit belongs either in the ones, tens, or hundreds place
                   of a complete integer and will be [1, 9]
    :precondition: place_value must be [0, 2] within the placement of the complete integer
    :postcondition: produce the correct romannumeral representation of this digit
    :return: roman numeral representation of the integer digit

    Test ones place digits.
    >>> romannumeral_1to9_loop(1, 0)
    'I'
    >>> romannumeral_1to9_loop(3, 0)
    'III'
    >>> romannumeral_1to9_loop(4, 0)
    'IV'
    >>> romannumeral_1to9_loop(5, 0)
    'V'
    >>> romannumeral_1to9_loop(8, 0)
    'VIII'
    >>> romannumeral_1to9_loop(9, 0)
    'IX'

    Test tens place digits.
    >>> romannumeral_1to9_loop(1, 1)
    'X'
    >>> romannumeral_1to9_loop(2, 1)
    'XX'
    >>> romannumeral_1to9_loop(4, 1)
    'XL'
    >>> romannumeral_1to9_loop(5, 1)
    'L'
    >>> romannumeral_1to9_loop(7, 1)
    'LXX'
    >>> romannumeral_1to9_loop(9, 1)
    'XC'

    Test hundreds place digits.
    >>> romannumeral_1to9_loop(1, 2)
    'C'
    >>> romannumeral_1to9_loop(3, 2)
    'CCC'
    >>> romannumeral_1to9_loop(4, 2)
    'CD'
    >>> romannumeral_1to9_loop(5, 2)
    'D'
    >>> romannumeral_1to9_loop(6, 2)
    'DC'
    >>> romannumeral_1to9_loop(9, 2)
    'CM'
    """
    roman_1 = romannumeral_power10s[place_value]
    roman_5 = romannumeral_5power10s[place_value]
    if positive_digit == 4:
        return roman_1 + roman_5
    elif positive_digit == 9:
        return roman_1 + romannumeral_power10s[place_value + 1]
    elif positive_digit in range(5, 9):
        positive_digit -= 5
        return roman_5 + roman_1 * positive_digit
    else:
        return roman_1 * positive_digit


def hundreds_romannumeral(positive_integer):
    """Convert integers that have place value up to hundreds into roman numeral.

    :param positive_integer: a positive integer <= 999
    :precondition: the integer passed is positive and has a maximum of 3 place values
    :postcondition: produces correct roman numeral representation of integer passed
    :return: roman numeral representation of integer

    >>> hundreds_romannumeral(1) #minimum
    'I'
    >>> hundreds_romannumeral(999) #maximum
    'CMXCIX'
    >>> hundreds_romannumeral(6)
    'VI'
    >>> hundreds_romannumeral(54)
    'LIV'
    >>> hundreds_romannumeral(483)
    'CDLXXXIII'
    """
    roman_number = ""
    # turn input number into a list of its digits, reversed
    digits_iterative = list(reversed([int(digit) for digit in str(positive_integer)]))
    for place_value in range(len(str(positive_integer))):
        roman_number = romannumeral_1to9_loop(digits_iterative[place_value], place_value) + roman_number
    return roman_number


def romannumeral(positive_int):
    """Convert integers from [1, 10_000] into roman numerals.

    :param positive_int: a positive integer [1, 10_000]
    :precondition: integer passed must be within range of 1 - 10_000
    :postcondition: produce correct roman numeral of integer
    :return: roman numeral representation of integer

    >>> romannumeral(1) # minimum
    'I'
    >>> romannumeral(10000) # maximum
    'MMMMMMMMMM'
    >>> romannumeral(4444)
    'MMMMCDXLIV'
    >>> romannumeral(5555)
    'MMMMMDLV'
    >>> romannumeral(9999)
    'MMMMMMMMMCMXCIX'
    >>> romannumeral(3)
    'III'
    >>> romannumeral(82)
    'LXXXII'
    >>> romannumeral(354)
    'CCCLIV'
    >>> romannumeral(6789)
    'MMMMMMDCCLXXXIX'
    """
    if positive_int == 10_000:
        return romannumeral_power10s[3] * 10
    else:
        thousands_digit = positive_int // 1000
        return romannumeral_power10s[3] * thousands_digit + \
            hundreds_romannumeral(positive_int - thousands_digit * 1000)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
