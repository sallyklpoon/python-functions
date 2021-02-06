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
    :precondition: given list is a collection of string elements "red", "white", or "blue" only
    :postcondition: modify the list accurately to have all elements in order of "red", "white", then "blue"
    :return: nothing, modifies original list

    >>> dutch = ["red", "white", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'white', 'blue']
    >>> dutch = ["red", "blue", "white"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'white', 'blue']
    >>> dutch = ["blue", "white", "red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'white', 'blue']
    >>> dutch = ["white", "red", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'white', 'blue']
    >>> dutch = ["blue", "blue", "red", "blue", "red", "red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'red', 'blue', 'blue', 'blue']
    >>> dutch = ["red", "white", "white", "red", "red", "white"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'red', 'white', 'white', 'white']
    >>> dutch = ["white", "blue", "blue", "blue", "white", "blue"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['white', 'white', 'blue', 'blue', 'blue', 'blue']
    >>> dutch = ["white", "red", "red", "white", "red", "red"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'red', 'red', 'white', 'white']
    >>> dutch = ["white", "blue", "blue", "red", "white", "red", "white"]
    >>> dijkstra(dutch)
    >>> print(dutch)
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
    """
    tally = "red." * colours_given.count("red") \
            + "white." * colours_given.count("white") \
            + "blue." * colours_given.count("blue")
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
