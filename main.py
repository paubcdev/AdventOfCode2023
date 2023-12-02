from days import *


def aoc(day):
    if day == '1':
        print("Part 1: " + day01.res1 + "\n" + "Part 2: " + day01.res2 + "\n")
    elif day == '2':
        print("Part 1: " + day02.res1 + "\n" + "Part 2: " + day02.res2 + "\n")
    else:
        print("Specify a day between 1 and 25, q to exit.")


if __name__ == "__main__":
    select = ""
    while select != 'q':
        select = str(input("What day do you want to check? "))
        aoc(select)
