"""This module contains the function romannumeral() and its helper functions.

The goal of the function is to convert a given integer in range [1, 10_000] to a
Roman Numeral. Given the pattern that roman numerals have unique characters for the
collection of power of 10s and 5* power of 10s, lists have been created for
these letters to be used during the conversion."""

romannumeral_power10s = ["I", "X", "C", "M"]     # in integer: 100, 10, 1, 1000
romannumeral_5power10s = ["V", "L", "D"]         # in integer: 500, 50, 5


def get_digits_iterative(integer):
    """Create a list of each digit in an integer.

    Given an integer, each digit number will be an element in the list.

    :param integer: an integer
    :precondition: the inputted parameter is an integer
    :postcondition: a list of each digit as an element
    :return: a list of each digit as an element
    """
    digit_iterative = [int(x) for x in str(integer)]
    return list(reversed(digit_iterative))


def romannumeral_tally(positive_digit, place_value):
    """Tally the value of a positive integer digit using the roman numeral
    for the place_value of this digit.

    Given a single particular digit from a positive integer and its place value,
    tally the place_value's matching roman numeral representation in power of 10s.

    :param positive_digit: an integer
    :param place_value: an integer [0, 3]
    :precondition: an integer and an integer [0, 3] is passed as arguments
    :postcondition: produce a correct roman number tally of the positive_integer_digit value
    with the corresponding roman numeral
    :return: roman numeral tally of the positive_integer_digit value
    """
    roman_1 = romannumeral_power10s[place_value]
    roman_number = ""
    for count in range(positive_digit):
        roman_number += roman_1
    return roman_number


def romannumeral_1to9_loop(positive_digit, place_value):
    """Produce the roman numeral representation of an integer digit [1, 9] given its
    place_value.
    
    :param positive_digit: an integer [1, 9]
    :param place_value: a place value [0, 2]
    :precondition: the positive digit belongs either in the ones, tens, or hundreds place
                   of the complete integer
    :postcondition: produce the correct romannumeral representation of this digit
    :return: roman numeral representation of the integer digit
    """
    roman_1 = romannumeral_power10s[place_value]
    roman_5 = romannumeral_5power10s[place_value]
    if positive_digit == 4:
        return roman_1 + roman_5
    elif positive_digit == 9:
        return roman_1 + romannumeral_power10s[place_value + 1]
    elif positive_digit in range(5, 9):
        positive_digit -= 5
        return roman_5 + romannumeral_tally(positive_digit, place_value)
    else:
        return romannumeral_tally(positive_digit, place_value)


def romannumeral_upto_hundreds(positive_int):
    """Converts integers that have place value up to hundreds into roman numeral.

    :param positive_int: a positive integer <= 999
    :precondition: the integer passed is positive and has a maximum of 3 place values
    :postcondition: produces correct roman numeral representation of integer passed
    :return: roman numeral representation of integer
    """
    roman_number = ""
    int_iterative = get_digits_iterative(positive_int)
    for place_value in range(len(str(positive_int))):
        roman_number = romannumeral_1to9_loop(int_iterative[place_value], place_value) + roman_number
    return roman_number


def romannumeral(positive_int):
    """Converts integers from [1, 10_000] into roman numerals.

    :param positive_int: a positive integer [1, 10_000]
    :precondition: integer passed must be within range of 1 - 10_000
    :postcondition: produce correct roman numeral of integer
    :return: roman numeral representation of integer
    """
    if positive_int == 10_000:
        return romannumeral_power10s[3] * 10
    elif positive_int >= 1000:
        thousands_digit = positive_int // 1000
        return romannumeral_tally(thousands_digit, 3) + \
            romannumeral_upto_hundreds(positive_int - thousands_digit * 1000)
    else:
        return romannumeral_upto_hundreds(positive_int)


def main():
    print(get_digits_iterative(123))

    print(romannumeral_tally(3, 0))
    print(romannumeral_tally(1, 1))
    print(romannumeral_tally(12, 2))

    print(romannumeral_1to9_loop(1, 0))
    print(romannumeral_1to9_loop(4, 0))
    print(romannumeral_1to9_loop(5, 0))
    print(romannumeral_1to9_loop(9, 0))
    print(romannumeral_1to9_loop(1, 1))
    print(romannumeral_1to9_loop(4, 1))
    print(romannumeral_1to9_loop(5, 1))
    print(romannumeral_1to9_loop(9, 1))
    print(romannumeral_1to9_loop(1, 2))
    print(romannumeral_1to9_loop(4, 2))
    print(romannumeral_1to9_loop(5, 2))
    print(romannumeral_1to9_loop(9, 2))

    print(romannumeral_upto_hundreds(999))
    print(romannumeral_upto_hundreds(1))
    print(romannumeral_upto_hundreds(548))

    print(romannumeral(10000))
    print(romannumeral(4132))
    print(romannumeral(5555))
    print(romannumeral(4444))
    print(romannumeral(354))
    print(romannumeral(6789))
    print(romannumeral(9999))
    print(romannumeral(12))
    print(romannumeral(3))


if __name__ == "__main__":
    main()
