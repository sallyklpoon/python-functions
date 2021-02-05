from string import ascii_lowercase, ascii_uppercase, digits


def cipher_character(character, shift):
    if character in ascii_uppercase:
        return ascii_uppercase[(ascii_uppercase.index(character) + shift) % 26]
    elif character in ascii_lowercase:
        return ascii_lowercase[(ascii_lowercase.index(character) + shift) % 26]
    elif character in digits:
        return str((int(character) + shift) % 10)
    else:
        return character


def caesarcipher(message, encode, shift):
    output_translation = ""
    if encode:
        for character in message:
            output_translation += cipher_character(character, shift)
    elif not encode:
        for character in message:
            output_translation += cipher_character(character, -shift)
    return output_translation


print(caesarcipher("Hello, How are you 123?", True, -723))
print(caesarcipher("Mjqqt, Mtb fwj dtz 890?", False, -723))