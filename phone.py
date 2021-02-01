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
    if alpha_number in mapped_2:
        return str(2)
    elif alpha_number in mapped_3:
        return str(3)
    elif alpha_number in mapped_4:
        return str(4)
    else:
        return str(5)


def map_6to9(alpha_number):
    if alpha_number in mapped_6:
        return str(6)
    elif alpha_number in mapped_7:
        return str(7)
    elif alpha_number in mapped_8:
        return str(8)
    else:
        return str(9)


def alpha_to_number(alpha_number):
    if alpha_number in mapped_2to5:
        return map_2to5(alpha_number)
    if alpha_number in mapped_6to9:
        return map_6to9(alpha_number)
    else:
        return alpha_number              # else: it is a number


def validate_input(input_string):
    for string_position in [3, 7]:
        if input_string[string_position] != "-":
            return "false"
    for string_position in [0, 1, 2, 4, 5, 6, 8, 9, 10, 11]:
        if input_string[string_position].isalum():
            return "false"


def phone(input_string):
    if validate_input(input_string) == "false":
        return "Invalid input, please input in format XXX-XXX-XXXX where X is alphanumeric."
    else:
        translated_phone = ""
        for string_position in range(12):
            if string_position == 3 or string_position == 7:
                translated_phone += "-"
            else:
                translated_phone += alpha_to_number(input_string[string_position])
        return translated_phone


def main():
    phone_number = "abc-FoOD"
    print(phone(phone_number))
    print(map_2to5("d"))
    print(alpha_to_number("1"))


if __name__ == '__main__':
    main()
