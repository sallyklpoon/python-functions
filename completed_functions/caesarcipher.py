"""
Sally Poon; A01232177
Date completed: 02-06-2021

This module contains the function caesarcipher and its helper function, cipher_character.

An import of ascii_lowercase, ascii_uppercase, and digits from the library string
is required.
"""

from string import ascii_lowercase, ascii_uppercase, digits

import doctest


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

    Test 0 shift.
    >>> cipher_character("q", 0)
    'q'
    >>> cipher_character("P", 0)
    'P'
    >>> cipher_character("4", 0)
    '4'

    Test first characters of each uppercase, lowercase, and digit group.
    >>> cipher_character("a", 3) # positive shift without needing to loop
    'd'
    >>> cipher_character("A", 3)
    'D'
    >>> cipher_character("0", 3)
    '3'
    >>> cipher_character("a", -3) # negative shift loop
    'x'
    >>> cipher_character("A", -3)
    'X'
    >>> cipher_character("0", -3)
    '7'
    >>> cipher_character("a", 548) # large shift
    'c'
    >>> cipher_character("A", 548)
    'C'
    >>> cipher_character("0", 548)
    '8'

    Test last characters of each uppercase, lowercase, and digit group.
    >>> cipher_character("z", 6) # positive shift loop
    'f'
    >>> cipher_character("Z", 6)
    'F'
    >>> cipher_character("9", 6)
    '5'
    >>> cipher_character("z", -9) # negative shift without needing to loop
    'q'
    >>> cipher_character("Z", -9)
    'Q'
    >>> cipher_character("9", -5)
    '4'
    >>> cipher_character("z", -336) # large shift
    'b'
    >>> cipher_character("Z", -336)
    'B'
    >>> cipher_character("9", -336)
    '3'

    Test mid-point characters of each uppercase, lowercase, and digit group.
    >>> cipher_character("h", 6) # positive shift without needing to loop
    'n'
    >>> cipher_character("J", 6)
    'P'
    >>> cipher_character("3", 6)
    '9'
    >>> cipher_character("m", -9) # negative shift without needing to loop
    'd'
    >>> cipher_character("T", -9)
    'K'
    >>> cipher_character("7", -5)
    '2'
    >>> cipher_character("n", 230) # large shift
    'j'
    >>> cipher_character("R", 230)
    'N'
    >>> cipher_character("4", 230)
    '4'
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
    the alphabet and number line [0, 9]. When encode is True, we apply the specified shift,
    when encode is False, we revert the shift.

    :param message: any string
    :param encode: a boolean
    :param shift: any number
    :precondition: message parameter must be a string
    :precondition: encode parameter must be Boolean.
    :precondition: shift parameter must be an integer
    :postcondition: If encode is True, accurately encode given message (apply shift)
                    If encode is False, accurately decrypt given message (revert shift)
    :return: string of ciphered (encoded or decrypted) message

    Test empty string.
    >>> caesarcipher("", True, 3)
    ''
    >>> caesarcipher("", False, 0) #
    ''

    Test filled string.
    >>> caesarcipher("$-%_^ &@   ", False, 4)
    '$-%_^ &@   '
    >>> caesarcipher("123", True, 3)
    '456'
    >>> caesarcipher("123", True, 26)
    '789'
    >>> caesarcipher("ABC", True, 3)
    'DEF'
    >>> caesarcipher("ABC", True, 40)
    'OPQ'
    >>> caesarcipher("T4L-2G9", True, 103)
    'S7K-5F2'
    >>> caesarcipher("T4L-2G9", True, 0)
    'T4L-2G9'
    >>> caesarcipher("H3ll0, wo4ld!!", False, -6)
    'N9rr6, cu0rj!!'
    >>> caesarcipher("H3ll0, wo4ld!!", False, -54)
    'J7nn4, yq8nf!!'
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
    print(caesarcipher("T4L-2G9", True, 103))


if __name__ == '__main__':
    # Run main() if module is being run as program
    main()
