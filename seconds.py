"""A module that will convert seconds to weeks."""

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3_600
SECONDS_IN_DAY = 86_400
SECONDS_IN_WEEK = SECONDS_IN_DAY * 7    # 604,800

conversion_list = [SECONDS_IN_WEEK, SECONDS_IN_DAY, SECONDS_IN_HOUR, SECONDS_IN_MINUTE, 1]


def seconds(total_seconds):
    """Produce string of seconds converted to number of weeks, days, hours,
    minutes, and seconds.

    :param total_seconds: a positive integer
    :precondition: a positive integer is submitted as the argument
    :postcondition: calculate number of weeks, days, hours, minutes and seconds given the argument
    :return: list of integers for [weeks, days, hours, minutes, seconds]
    """
    output = []
    for conversion in conversion_list:
        converted_time = total_seconds // conversion
        total_seconds = total_seconds % conversion
        output.append(converted_time)
    return output


def main():
    # Cases to test conversion works
    print(seconds(0))
    print(seconds(60))
    print(seconds(3_600))
    print(seconds(86_400))
    print(seconds(604_800), "\n")

    # Other random cases
    print(seconds(65))
    print(seconds(3630))
    print(seconds(112_320))
    print(seconds(1_757_773))
    print(seconds(6_471_029))


if __name__ == "__main__":
    main()
