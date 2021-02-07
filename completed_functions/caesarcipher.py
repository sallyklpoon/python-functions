"""
Sally Poon; A01232177
Date completed: 02-06-2021

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
    >>> cipher_character("a", 548) # positive shift needing to loop
    'c'
    >>> cipher_character("A", 548)
    'C'
    >>> cipher_character("0", 548)
    '8'
    >>> cipher_character("a", -548) # negative shift needing to loop
    'y'
    >>> cipher_character("A", -548)
    'Y'
    >>> cipher_character("0", -548)
    '2'

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
    >>> cipher_character("z", 336) # positive shift needing to loop
    'x'
    >>> cipher_character("Z", 336)
    'X'
    >>> cipher_character("9", 336)
    '5'
    >>> cipher_character("z", -336) # negative shift needing to loop
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
    >>> cipher_character("n", 230) # positive shift needing to loop
    'j'
    >>> cipher_character("R", 230)
    'N'
    >>> cipher_character("4", 230)
    '4'
    >>> cipher_character("s", -1043) # negative shift needing to loop
    'p'
    >>> cipher_character("L", -1043)
    'I'
    >>> cipher_character("8", -1043)
    '5'
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

    Test no shift.
    >>> caesarcipher("Will this 1 encode?", True, 0)
    'Will this 1 encode?'
    >>> caesarcipher("Will this 1 decode?", False, 0)
    'Will this 1 decode?'

    Test string.
    >>> caesarcipher("", True, 2) # empty, encode, positive shift
    ''
    >>> caesarcipher("", False, -4) # empty, decrypt, negative shift
    ''
    >>> caesarcipher("$@- encODE thIS 123!", True, 2) # non-empty, encode, positive shift
    '$@- gpeQFG vjKU 345!'
    >>> caesarcipher("$@- gpeQFG vjKU 345!", False, 2) # non-empty, decrypt, positive shift
    '$@- encODE thIS 123!'
    >>> caesarcipher("a laZy f0x ^&#", True, -12) #non-empty, encode, negative shift
    'o zoNm t8l ^&#'
    >>> caesarcipher("o zoNm t8l ^&#", False, -12) #non-empty, decrypt, negative shift
    'a laZy f0x ^&#'
    >>> caesarcipher("U5l?U7HkHta0=&rB", True, 356) #non-empty, encrypt, extreme positive shift
    'M1d?M3ZcZls6=&jT'
    >>> caesarcipher("M1d?M3ZcZls6=&jT", False, 356) #non-empty, decrypt, extreme positive shift
    'U5l?U7HkHta0=&rB'
    >>> caesarcipher("7nkT%HpA?jXLpWDt", True, -999) #non-empty, encrypt, extreme negative shift
    '8czI%WeP?yMAeLSi'
    >>> caesarcipher("8czI%WeP?yMAeLSi", False, -999) #non-empty, decrypt, extreme negative shift
    '7nkT%HpA?jXLpWDt'
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
