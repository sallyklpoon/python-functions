"""This module contains the function romannumeral() and its helper functions.

The goal of the function is to convert a given integer in range [1, 10_000] to a
Roman Numeral"""

roman_1s = ["I", "X", "C", "M"]
roman_5s = ["V", "L", "D"]


def i_count(positive_int):
    roman_number = ""
    for count in range(positive_int):
        roman_number = str(roman_number + "I")
    return roman_number


def romannumeral_ones_place(ones_int):
    if ones_int == 4:
        return "IV"
    elif ones_int >= 5:
        ones_int = ones_int - 5
        return "V" + i_count(ones_int)
    else:
        return i_count(ones_int)


def main():
    print(i_count(0))
    print(i_count(1))
    print(i_count(12))
    print(romannumeral_ones_place(1))
    print(romannumeral_ones_place(4))
    print(romannumeral_ones_place(5))
    print(romannumeral_ones_place(9))


if __name__ == "__main__":
    main()
