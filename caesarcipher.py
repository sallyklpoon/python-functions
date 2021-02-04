from string import ascii_lowercase, ascii_uppercase, digits

uppercase = list(ascii_uppercase)
lowercase = list(ascii_lowercase)
digits = list(digits)


def translate_number(number):
    return number


def foo(alpha_number, shift):
    if shift < 0:
        shift = -(abs(shift) % 26)
    else:
        shift %= 26
    for alpha_set in [uppercase, lowercase]:
        if alpha_number in alpha_set:
            current_position = alpha_set.index(alpha_number)
            if current_position - shift >= 0:
                translated_letter = alpha_set[shift - (26 - current_position)]
            else:
                translated_letter = alpha_set[current_position + shift]
            return translated_letter


# def find_letter(alpha_number, shift):
#     shift %= 26
#     if alpha_number in uppercase:
#         current_position = uppercase.index(alpha_number)
#         if current_position - shift >= 0:
#             translated_letter = uppercase[shift - (26 - current_position)]
#         else:
#             translated_letter = uppercase[current_position + shift]
#         return translated_letter
#     if alpha_number in lowercase:
#         current_position = lowercase.index(alpha_number)
#         if current_position - shift >= 0:
#             translated_letter = lowercase[shift - (26 - current_position)]
#         else:
#             translated_letter = lowercase[current_position + shift]
#         return translated_letter


letter = "Q"
shift = -85
print(shift % 26)
# print(find_letter(letter, shift))
print(foo(letter, shift))


# def get_translation(character, shift): # pass to appropriate alpha or number comparison
#     if character in digits:
#
#     else:
#         for letter in [uppercase, lowercase]:
#             if character == letter:
#                 output_character = uppercase.index(letter + shift)
#                 return output_character
#     elif character in lowercase:
#         pass
#     elif character in digits:


# def caesarcipher(message, encode, shift):
#     message_characters = list(message)
#     output_translation = ""
#     if encode:
#         for character in message_characters:
#             output_translation += get_translation(character, shift)
#     elif not encode:
#         for character in message_characters:
#             output_translation += get_translation(character, - shift)
#     pass