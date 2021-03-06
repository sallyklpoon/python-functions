"""
Sally A01232177
Date Complete: 02-06-2021

A module that will convert seconds to weeks, days, hours, minutes, and seconds.
"""

import doctest

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3_600
SECONDS_IN_DAY = 86_400
SECONDS_IN_WEEK = SECONDS_IN_DAY * 7    # 604,800


def seconds(total_seconds):
    """Produce list of seconds converted to number of weeks, days, hours,
    minutes, and seconds in this ordered format.

    :param total_seconds: a positive integer
    :precondition: total_seconds is a positive integer
    :postcondition: produce an accurate list for the number of weeks, days,
                    hours, minutes and seconds given total_seconds
    :return: list of integers for number of [weeks, days, hours, minutes, seconds] from total_seconds

    Test each converstion works.
    >>> seconds(0)
    [0, 0, 0, 0, 0]
    >>> seconds(59)
    [0, 0, 0, 0, 59]
    >>> seconds(60)
    [0, 0, 0, 1, 0]
    >>> seconds(2_345)
    [0, 0, 0, 39, 5]
    >>> seconds(3_600)
    [0, 0, 1, 0, 0]
    >>> seconds(74_390)
    [0, 0, 20, 39, 50]
    >>> seconds(86_400)
    [0, 1, 0, 0, 0]
    >>> seconds(112_320)
    [0, 1, 7, 12, 0]
    >>> seconds(604_800)
    [1, 0, 0, 0, 0]
    >>> seconds(6_471_029)
    [10, 4, 21, 30, 29]
    """
    conversion_list = [SECONDS_IN_WEEK, SECONDS_IN_DAY, SECONDS_IN_HOUR, SECONDS_IN_MINUTE, 1]
    output = []
    for conversion in conversion_list:
        converted_time = total_seconds // conversion
        total_seconds %= conversion
        output.append(converted_time)
    return output


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    # Run main() if module being executed as a program
    main()
