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


def get_romannumeral(digit, place_value):
    """Produce the roman numeral representation of an integer [1, 9] given its
    place_value in a complete number.

    Each digit in a base10 number can only be [1, 9], function will translate
    these numbers to its roman numeral equivalent by use of importing the
    roman numeral 1 value and roman numeral 5 value for a given place_value.
    
    :param digit: an integer [1, 9]
    :param place_value: an integer [0, 2]
    :precondition: the positive digit belongs either in the ones, tens, or hundreds place
                   of a complete integer and is one of [1, 9]
    :precondition: place_value must be [0, 2] within the placement of the complete number
    :postcondition: produce the correct romannumeral representation of this digit
    :return: roman numeral representation of the integer digit as a string

    Test ones place digits.
    >>> get_romannumeral(1, 0)
    'I'
    >>> get_romannumeral(3, 0)
    'III'
    >>> get_romannumeral(4, 0)
    'IV'
    >>> get_romannumeral(5, 0)
    'V'
    >>> get_romannumeral(8, 0)
    'VIII'
    >>> get_romannumeral(9, 0)
    'IX'

    Test tens place digits.
    >>> get_romannumeral(1, 1)
    'X'
    >>> get_romannumeral(2, 1)
    'XX'
    >>> get_romannumeral(4, 1)
    'XL'
    >>> get_romannumeral(5, 1)
    'L'
    >>> get_romannumeral(7, 1)
    'LXX'
    >>> get_romannumeral(9, 1)
    'XC'

    Test hundreds place digits.
    >>> get_romannumeral(1, 2)
    'C'
    >>> get_romannumeral(3, 2)
    'CCC'
    >>> get_romannumeral(4, 2)
    'CD'
    >>> get_romannumeral(5, 2)
    'D'
    >>> get_romannumeral(6, 2)
    'DC'
    >>> get_romannumeral(9, 2)
    'CM'
    """
    roman_1 = romannumeral_power10s[place_value]
    roman_5 = romannumeral_5power10s[place_value]
    if digit == 4:
        return roman_1 + roman_5
    elif digit == 9:
        return roman_1 + romannumeral_power10s[place_value + 1]
    elif digit in range(5, 9):
        digit -= 5
        return roman_5 + roman_1 * digit
    else:
        return roman_1 * digit


def hundreds_romannumeral(positive_int):
    """Convert integers that have place value up to hundreds into roman numeral.

    :param positive_int: a positive integer <= 999
    :precondition: the integer passed is positive and has a maximum of 3 place values (<= 999)
    :postcondition: produces correct roman numeral representation of the positive_int
    :return: roman numeral representation of the positive_int as a string

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
    digits_iterative = list(reversed([int(digit) for digit in str(positive_int)]))
    for place_value in range(len(str(positive_int))):
        roman_number = get_romannumeral(digits_iterative[place_value], place_value) + roman_number
    return roman_number


def romannumeral(positive_int):
    """Convert integers from [1, 10_000] into roman numerals.

    :param positive_int: a positive integer [1, 10_000]
    :precondition: positive_int is a positive integer within the range of 1 - 10_000
    :postcondition: produce correct roman numeral representation of positive_int
    :return: roman numeral representation of posiitive_int as a string

    >>> romannumeral(1) # minimum
    'I'
    >>> romannumeral(4)
    'IV'
    >>> romannumeral(9)
    'IX'
    >>> romannumeral(99)
    'XCIX'
    >>> romannumeral(100)
    'C'
    >>> romannumeral(499)
    'CDXCIX'
    >>> romannumeral(500)
    'D'
    >>> romannumeral(940)
    'CMXL'
    >>> romannumeral(999)
    'CMXCIX'
    >>> romannumeral(1000)
    'M'
    >>> romannumeral(1049)
    'MXLIX'
    >>> romannumeral(4444)
    'MMMMCDXLIV'
    >>> romannumeral(9999)
    'MMMMMMMMMCMXCIX'
    >>> romannumeral(10_000) # maximum
    'MMMMMMMMMM'
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
