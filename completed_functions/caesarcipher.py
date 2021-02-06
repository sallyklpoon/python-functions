"""
Sally Poon; A01232177
Last date of modification: February 2, 2021

This module contains the function caesarcipher and its helper function, cipher_character.
An import of ascii_lowercase, ascii_uppercase, and digits from the library string
is required.
"""
import doctest
from string import ascii_lowercase, ascii_uppercase, digits


def cipher_character(character, shift):
    """Return a given character ciphered according to shift.

    Ciphered meaning the original character is shifted the amount of places
    indicated by value shift.

    :param character: a string
    :param shift: a number
    :precondition: character is a single character string
    :precondition: shift is an integer
    :postcondition: return accurate ciphered character
    :return: a single character string of ciphered character
    """
    if character in ascii_uppercase:
        return ascii_uppercase[(ascii_uppercase.index(character) + shift) % 26]
    elif character in ascii_lowercase:
        return ascii_lowercase[(ascii_lowercase.index(character) + shift) % 26]
    elif character in digits:
        return str((int(character) + shift) % 10)
    else:
        return character


def caesarcipher(message, encode, shift):
    """Encode/Decrypt a message using Caesar Cipher.

    Caesar Cipher shifts each character a fixed amount of places up or down
    the alphabet and number line [0, 9].

    :param message: any string
    :param encode: a boolean
    :param shift: any number
    :precondition: message parameter must be a string
    :precondition: encode parameter must be True or False.
                   True asks function to encode, False asks function to decrypt
    :precondition: shift parameter must be an integer
    :postcondition: If encode is True, accurately encode given message (apply shift)
                    If encode is False, accurately decrypt given message (revert shift)
    :return: string of ciphered message
    """
    output_translation = ""
    if encode:
        for character in message:
            output_translation += cipher_character(character, shift)
    elif not encode:
        for character in message:
            output_translation += cipher_character(character, -shift)
    return output_translation


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    # Run main() if module is being run as program
    main()
