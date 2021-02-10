"""
Sally Poon A01232177
Date Completed: 02-06-2021

This module will translate a phone number with letters to all numbers.

Since all phones have specific mapped letters to numbers, the mapped
letters to each number are defined as lists at the start of the module.

To keep functions short and concise, the phone() function will send each alpha_number
digit in a phone number to alpha_to_number() which will figure out if this digit
belongs in the group of mapped 2-5 numbers (send to map_2to5) or mapped 6-9 numbers
(send to map_6to9).
"""
import doctest

mapped_2 = ["A", "B", "C"]
mapped_3 = ["D", "E", "F"]
mapped_4 = ["G", "H", "I"]
mapped_5 = ["J", "K", "L"]
mapped_6 = ["M", "N", "O"]
mapped_7 = ["P", "Q", "R", "S"]
mapped_8 = ["T", "U", "V"]
mapped_9 = ["W", "X", "Y", "Z"]


def map_2to5(letter):
    """Translate letter to the mapped number that is [2, 5].

    :param letter: a single character string
    :precondition: pass string with a single uppercase letter mapped to either
                   2, 3, 4, or 5 on the phone
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number

    >>> map_2to5("A")
    '2'
    >>> map_2to5("B")
    '2'
    >>> map_2to5("C")
    '2'
    >>> map_2to5("D")
    '3'
    >>> map_2to5("E")
    '3'
    >>> map_2to5("F")
    '3'
    >>> map_2to5("G")
    '4'
    >>> map_2to5("H")
    '4'
    >>> map_2to5("I")
    '4'
    >>> map_2to5("J")
    '5'
    >>> map_2to5("K")
    '5'
    >>> map_2to5("L")
    '5'
    """
    if letter in mapped_2:
        return str(2)
    elif letter in mapped_3:
        return str(3)
    elif letter in mapped_4:
        return str(4)
    else:  # else: alpha_number in "JKL"
        return str(5)


def map_6to9(letter):
    """Translate letter to the mapped number that is [6, 9].

    :param letter: a single character capitalized letter
    :precondition: pass string with a single uppercase letter mapped to either
                   6, 7, 8, or 9 on the phone
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number

    >>> map_6to9("M")
    '6'
    >>> map_6to9("N")
    '6'
    >>> map_6to9("O")
    '6'
    >>> map_6to9("P")
    '7'
    >>> map_6to9("Q")
    '7'
    >>> map_6to9("R")
    '7'
    >>> map_6to9("S")
    '7'
    >>> map_6to9("T")
    '8'
    >>> map_6to9("U")
    '8'
    >>> map_6to9("V")
    '8'
    >>> map_6to9("W")
    '9'
    >>> map_6to9("X")
    '9'
    >>> map_6to9("Y")
    '9'
    >>> map_6to9("Z")
    '9'
    """
    if letter in mapped_6:
        return str(6)
    elif letter in mapped_7:
        return str(7)
    elif letter in mapped_8:
        return str(8)
    else:  # else: alpha_number in "WXYZ"
        return str(9)


def alpha_to_number(character):
    """Return a given alpha_number digit (letter or number) to its mapped number.

    :param character: a string with a single alphanumeric character
    :postcondition: pass a string with a single character that is either an uppercase letter or number
    :postcondition: translate input character to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number

    >>> alpha_to_number("A")
    '2'
    >>> alpha_to_number("H")
    '4'
    >>> alpha_to_number("L")
    '5'
    >>> alpha_to_number("M")
    '6'
    >>> alpha_to_number("T")
    '8'
    >>> alpha_to_number("Z")
    '9'
    >>> alpha_to_number("0")
    '0'
    >>> alpha_to_number("6")
    '6'
    >>> alpha_to_number("9")
    '9'
    """
    mapped_2to5 = mapped_2 + mapped_3 + mapped_4 + mapped_5
    mapped_6to9 = mapped_6 + mapped_7 + mapped_8 + mapped_9
    if character in mapped_2to5:
        return map_2to5(character)
    if character in mapped_6to9:
        return map_6to9(character)
    else:  # else: alpha_number is a number
        return character


def phone(input_phone):
    """Translate alphabets in a phone number to its numerical equivalent.

    :param input_phone: a string
    :precondition: input_string is a string with format XXX-XXX-XXXX where
                   X is a number or an uppercase letter character
    :postcondition: correctly translate a phone number with alphabetical
                    numbers to its numerical equivalent XXX-XXX-XXXX format
                    where X is an integer string
    :return: string of phone number translated to all numbers

    >>> phone("604-123-4567")
    '604-123-4567'
    >>> phone("AAA-AAA-AAAA")
    '222-222-2222'
    >>> phone("777-777-7777")
    '777-777-7777'
    >>> phone("TRY-THE-LOGI")
    '879-843-5644'
    >>> phone("555-GET-FOOD")
    '555-438-3663'
    >>> phone("A2B-6J9-R3P1")
    '222-659-7371'
    """
    translated_phone = ""
    for character in input_phone:
        if character == "-":
            translated_phone += "-"
        else:
            translated_phone += alpha_to_number(character)
    return translated_phone


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
