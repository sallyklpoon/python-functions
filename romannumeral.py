"""This module contains the function romannumeral() and its helper functions.

The goal of the function is to convert a given integer in range [1, 10_000] to a
Roman Numeral"""

roman_1s = ["C", "X", "I", "M"]
roman_5s = ["D", "L", "V"]


def number_of_digits(integer):
    return len(str(integer))


def integer_iterative(integer):
    return [int(x) for x in str(integer)]


def i_count(positive_int, int_numberplace):
    roman_1 = roman_1s[int_numberplace]
    roman_number = ""
    for count in range(positive_int):
        roman_number = roman_number + roman_1
    return roman_number


def romannumeral_loop(positive_int, int_numberplace):
    roman_1 = roman_1s[int_numberplace]
    roman_5 = roman_5s[int_numberplace]
    if positive_int == 4:
        return roman_1 + roman_5
    elif positive_int >= 5:
        positive_int -= 5
        return roman_5 + i_count(positive_int, int_numberplace)
    else:
        return i_count(positive_int, int_numberplace)


def romannumeral_upto_hundreds(positive_int):
    roman_number = ""
    int_iterative = integer_iterative(positive_int)
    for numbers_place in range(number_of_digits(positive_int) - 1):
        roman_number += romannumeral_loop(int_iterative[numbers_place], numbers_place)
    return roman_number


def romannumeral(positive_int):
    if positive_int == 10000:
        return roman_1s[3] * 10
    elif number_of_digits(positive_int) == 4:
        int_iterative = integer_iterative(positive_int)
        return i_count(int_iterative[0], 3) + romannumeral_upto_hundreds(positive_int - int_iterative[0]*1000) #something wrong here
    else:
        roman_number = ""
        int_iterative = integer_iterative(positive_int)
        for numbers_place in range(number_of_digits(positive_int)):
            roman_number += romannumeral_loop(int_iterative[numbers_place], numbers_place)
        return roman_number


def main():
    print(number_of_digits(0))
    print(number_of_digits(1_000))
    print(integer_iterative(123))
    print(i_count(3, 0))
    print(i_count(1, 1))
    print(i_count(12, 2))
    print(romannumeral_loop(1, 0))
    print(romannumeral_loop(4, 0))
    print(romannumeral_loop(5, 0))
    print(romannumeral_loop(9, 0))
    print(romannumeral_loop(1, 1))
    print(romannumeral_loop(4, 1))
    print(romannumeral_loop(5, 1))
    print(romannumeral_loop(9, 1))
    print(romannumeral_loop(1, 2))
    print(romannumeral_loop(4, 2))
    print(romannumeral_loop(5, 2))
    print(romannumeral_loop(9, 2))
    print(romannumeral(10000))
    print(romannumeral(4132))
    print(romannumeral(555))
    print(romannumeral(354))
    print(romannumeral(789))


if __name__ == "__main__":
    main()
