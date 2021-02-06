def dijkstra(colours_given):
    red_tally = colours_given.count("red")
    white_tally = colours_given.count("white")
    blue_tally = colours_given.count("blue")
    written_tally = "red." * red_tally + "white." * white_tally + "blue." * blue_tally
    dutch_colours = written_tally[:-1].split(".")
    colours_given.clear()
    for item in dutch_colours:
        colours_given.append(item)


def main():
    """Execute the program."""
    tests_lst = ["white", "blue", "blue", "red", "white", "red", "white"]
    # Executes to ['red', 'white', 'white', 'red', 'blue', 'blue']
    dijkstra(tests_lst)
    print(tests_lst)
    # string = "red." * 4 + "white." * 3 + "blue." * 3
    # print(string.split("."))

# Execute only if file run as a program
if __name__ == '__main__':
    main()
