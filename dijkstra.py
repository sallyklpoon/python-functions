

def dijkstra(colours_given):
    for colour in colours_given:
        if colour == "red":
            colour_adjust = colours_given.pop(colours_given.index(colour))
            colours_given.insert(0, colour_adjust)
        elif colour == "blue":
            colour_adjust = colours_given.pop(colours_given.index(colour))
            colours_given.append(colour_adjust)
        else:
            colour_adjust = colours_given.pop(colours_given.index(colour))
            white_position = colours_given.count("red")
            colours_given.insert(white_position, colour_adjust)


def main():
    tests_lst = ["blue", "blue", "blue", "blue", "white", "blue", "blue", "red", "red", "red", "red", "red"]
    dijkstra(tests_lst)
    print(tests_lst)

    # colour_adjust = tests_lst.pop(-1)
    # tests_lst.insert(len(tests_lst) // 2, colour_adjust)
    # print(len(tests_lst) // 2)
    # print(tests_lst)


if __name__ == '__main__':
    main()
