from days import *


def aoc(day):
    if day == 1:
        print("Part 1: " + day01.res1 + "\n" + "Part 2: " + day01.res2)
    else:
        print("Specify a day between 1 and 25.")


if __name__ == "__main__":
    select = int(input("What day is it? "))
    aoc(select)
