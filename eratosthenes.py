"""This module contains a function that uses Eratosthenes method
of finding a list of prime numbers given a range from [0, n],
"""
from math import sqrt, floor


def eratosthenes(upper_bound):
    """Find the numbers within range [0, upper_bound] that are prime numbers.

    :param upper_bound: a positive integer
    :precondition: a positive integer is passed as an argument
    :postcondition: return a correct list of prime numbers up to upper_bound range
    :return: a list of prime numbers up to the upper_bound range
    """
    number_list = list(range(2, upper_bound + 1))
    evaluating_numbers = list(range(2, floor(sqrt(upper_bound))))
    for evaluating_number in evaluating_numbers:
        for number in number_list:
            if number != evaluating_number and number % evaluating_number == 0:
                number_list.remove(number)
    return number_list


def main():
    number_list = [0, 2, 3, 4]
    number_list.remove(3)
    input_integer = 100
    print(eratosthenes(input_integer))
    print(eratosthenes(16))
    print(eratosthenes(19))


if __name__ == '__main__':
    main()
