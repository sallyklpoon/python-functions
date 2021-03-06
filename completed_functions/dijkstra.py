"""
Sally Poon A01232177
Date Completed: 02-06-2021

This module contains a function to solve the dijkstra problem without any
return or print value -- that is, the function will only modify the original list.
"""
import doctest


def dijkstra(colours_given):
    """Modify an original list of "red", "white", and "blue" by sorting elements in the order of the National
    Dutch Flag colours.

    A solution to the Dijkstra problem.

    :param colours_given: a list of strings
    :precondition: colours_given is a non-empty list of string elements "red", "white", or "blue" only
    :postcondition: modify the list accurately to have all elements in order of "red", "white", then "blue"
    :return: nothing, modifies original list

    >>> dutch = ["red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red']
    >>> dutch = ["blue", "blue", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['blue', 'blue', 'blue']
    >>> dutch = ["red", "red", "white", "white", "blue", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'white', 'white', 'blue', 'blue']
    >>> dutch = ["red", "blue", "red", "white", "red", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'red', 'white', 'blue', 'blue']
    """
    tally = "red." * colours_given.count("red") \
            + "white." * colours_given.count("white") \
            + "blue." * colours_given.count("blue")
    # excluding last ".", split tally string into a list then clear original list
    dutch_colours = tally[:-1].split(".")
    colours_given.clear()
    for element in dutch_colours:
        colours_given.append(element)


def main():
    """Execute the program."""
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    # Run main() if module is being run as program
    main()
