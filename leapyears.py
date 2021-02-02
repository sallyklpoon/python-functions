"""Module contains a function to calculate how many leap years
 are in a range of given years.

 This module requires the import of calendar to use the calendar.leapdays(a,b) function"""

import calendar


def leapyears(lower_bound, upper_bound):
    """Calculate the number of leap years in a given range.

    :param lower_bound: an integer > 0 and <= upper_bound
    :param upper_bound: an integer > 0
    :precondition: lower_bound passed to function must be a an integer that is
                   greater than 0 and less than or equal to the upper_bound.
                   The upper_bound passed must be an integer greater than 0.
    :postcondition: produce the correct number of leap years within the given range
    :return: an integer representing the number of leap years within the given range
    """
    return calendar.leapdays(lower_bound, upper_bound)


def main():
    lower_bound = 1918
    upper_bound = 2018
    print(leapyears(lower_bound, upper_bound))
    print(type(leapyears(lower_bound, upper_bound)))


if __name__ == '__main__':
    main()
