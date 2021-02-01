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
    else:                               # else: alpha_number in mapped_5
        return str(5)


def map_6to9(alpha_number):
    if alpha_number in mapped_6:
        return str(6)
    elif alpha_number in mapped_7:
        return str(7)
    elif alpha_number in mapped_8:
        return str(8)
    else:                               # else: alpha_number in mapped_9
        return str(9)


def alpha_to_number(alpha_number):
    if alpha_number in mapped_2to5:
        return map_2to5(alpha_number)
    if alpha_number in mapped_6to9:
        return map_6to9(alpha_number)
    else:                               # else: it is a number
        return alpha_number


def phone(input_string):
    translated_phone = ""
    for string_position in range(12):
        if string_position == 3 or string_position == 7:
            translated_phone += "-"
        else:
            translated_phone += alpha_to_number(input_string[string_position])
    return translated_phone


def main():
    phone_number = "555-FoO-1234"
    print(phone(phone_number))
    print(map_2to5("d"))
    print(alpha_to_number("1"))

    string = "-"
    print(string.isalnum())


if __name__ == '__main__':
    main()
