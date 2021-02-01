""" This module will translate a phone number with letters to all numbers.

Since all phones have specific mapped letters to numbers, the mapped
letters to each number has been defined as lists at the start of the document.

To keep functions short and concise, the phone() function will send each alpha_number
digit in a phone number to alpha_to_number() which will figure out if this digit
belongs in the group of mapped 2-5 numbers (send to map_2to5) or mapped 6-9 numbers
(send to map_6to9).
"""
mapped_2 = ["A", "B", "C", "a", "b", "c"]
mapped_3 = ["D", "E", "F", "d", "e", "f"]
mapped_4 = ["G", "H", "I", "g", "h", "i"]
mapped_5 = ["J", "K", "L", "j", "k", "l"]
mapped_6 = ["M", "N", "O", "m", "n", "o"]
mapped_7 = ["P", "Q", "R", "S", "p", "q", "r", "s"]
mapped_8 = ["T", "U", "V", "t", "u", "v"]
mapped_9 = ["W", "X", "Y", "Z", "w", "x", "y", "z"]

mapped_2to5 = mapped_2 + mapped_3 + mapped_4 + mapped_5
mapped_6to9 = mapped_6 + mapped_7 + mapped_8 + mapped_9


def map_2to5(alpha_number):
    """Translates inputted alpha_number to the mapped number that is [2, 5].

    :param alpha_number: an alphanumeric string
    :precondition: pass an alphanumeric string with a single character to the
                    function that is either a letter in the mapped_2to5 list
                    or a string integer [2, 5]
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number
    """
    if alpha_number in mapped_2:
        return str(2)
    elif alpha_number in mapped_3:
        return str(3)
    elif alpha_number in mapped_4:
        return str(4)
    else:                               # else: alpha_number in mapped_5
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
    if alpha_number in mapped_6:
        return str(6)
    elif alpha_number in mapped_7:
        return str(7)
    elif alpha_number in mapped_8:
        return str(8)
    else:                               # else: alpha_number in mapped_9
        return str(9)


def alpha_to_number(alpha_number):
    """Translates a given alpha digit to its mapped number by
    sending it to the correct map function for translation.

    :param alpha_number: an alphanumeric string with a single character
    :postcondition: an alphanumeric string with a single character
    :postcondition: translate input string to the correct mapped number as a string
    :return: a string integer of the mapped alpha_number
    """
    if alpha_number in mapped_2to5:
        return map_2to5(alpha_number)
    if alpha_number in mapped_6to9:
        return map_6to9(alpha_number)
    else:                               # else: it is a number
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
