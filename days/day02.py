import math
import re
from collections import defaultdict

with open('./inputs/input_day2.txt') as input_raw:
    values = input_raw.read().strip().split("\n")


def part1(val):
    good_ids = 0
    for line in val:
        parts = re.sub("[;,:]", "", line).split()
        color_max = defaultdict(int)
        for count, color in zip(parts[2::2], parts[3::2]):
            color_max[color] = max(color_max[color], int(count))
        if color_max["red"] <= 12 and color_max["green"] <= 13 and color_max["blue"] <= 14:
            good_ids += int(parts[1])
    return good_ids


def part2(val):
    total_power = 0
    for line in val:
        parts = re.sub("[;,:]", "", line).split()
        color_max = defaultdict(int)
        for count, color in zip(parts[2::2], parts[3::2]):
            color_max[color] = max(color_max[color], int(count))
        power = math.prod(color_max.values())
        total_power += power
    return total_power


res1 = str(part1(values))
res2 = str(part2(values))
