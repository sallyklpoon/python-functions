""" This module will translate a phone number with letters to all numbers.

Since all phones have specific mapped letters to numbers, the mapped
letters to each number has been defined as lists at the start of the document.

To keep functions short and concise, the phone() function will send each alpha_number
digit in a phone number to alpha_to_number() which will figure out if this digit
belongs in the group of mapped 2-5 numbers (send to map_2to5) or mapped 6-9 numbers
(send to map_6to9).
"""


def map_2to5(alpha_number):
    """Translates inputted alpha_number to the mapped number that is [2, 5].

    :param alpha_number: an alphanumeric string
    :precondition: pass an alphanumeric string with a single character to the
                    function that is either a letter in the mapped_2to5 list
                    or a string integer [2, 5]
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number
    """
    if alpha_number in "ABC":
        return str(2)
    elif alpha_number in "DEF":
        return str(3)
    elif alpha_number in "GHI":
        return str(4)
    else:  # else: alpha_number in "JKL"
        return str(5)


def map_6to9(alpha_number):
    """Translates inputted alpha_number to the mapped number that is [6,9].

    :param alpha_number: a alphanumeric string with a single character
    :precondition: pass an alphanumeric string with a single character to the
                    function that is either a letter in the mapped_6to9 list
                    or a string integer [6, 9]
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number
    """
    if alpha_number in "MNO":
        return str(6)
    elif alpha_number in "PQRS":
        return str(7)
    elif alpha_number in "TUV":
        return str(8)
    else:  # else: alpha_number in "WXYZ"
        return str(9)


def alpha_to_number(alpha_number):
    """Translates a given alpha digit to its mapped number by
    sending it to the correct map function for translation.

    :param alpha_number: an alphanumeric string with a single character
    :postcondition: an alphanumeric string with a single character
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number
    """
    if alpha_number in "ABCDEFGHIJKLabcdefghijkl":
        return map_2to5(alpha_number.upper())
    if alpha_number in "MNOPQRSTUVWXYZmnopqrstuvwxyz":
        return map_6to9(alpha_number.upper())
    else:  # else: alpha_number is a number
        return alpha_number


def phone(input_string):
    """Translates any alphabetical numbers to numerical equivalent.

    :param input_string: an string
    :precondition: input_string is a string with format XXX-XXX-XXXX where
                   X is an alphanumeric character
    :postcondition: correctly translates a phone number with alphabetical
                    numbers to its numerical equivalent XXX-XXX-XXXX format
                    where X is an integer
    :return: string of phone number translated
    """
    translated_phone = ""
    for string_position in range(12):
        if string_position == 3 or string_position == 7:
            translated_phone += "-"
        else:
            translated_phone += alpha_to_number(input_string[string_position])
    return translated_phone


def main():
    phone_number = "555-GeT-FOoD"
    print(phone(phone_number))
    print(phone("800-GOT-JUNK"))
    print(phone("123-456-7890"))

    alpha_number = "A"
    print(map_2to5(alpha_number))

    alpha_number = "Z"
    print(map_6to9(alpha_number))

    print(alpha_to_number("1"))
    print(alpha_to_number("K"))
    print(alpha_to_number("l"))


if __name__ == '__main__':
    main()
