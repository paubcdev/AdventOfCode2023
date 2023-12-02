import re
replacements = {'one': 'on1e', 'two': 'tw2o', 'three': 'thr3e', 'four': 'fo4ur', 'five': 'fi5ve', 'six':
                'si6x', 'seven': 'sev7en', 'eight': 'ei8ght', 'nine': 'ni9ne'}

with open('./inputs/input_day1.txt') as input_raw:
    values = input_raw.read().strip().split("\n")


def part1(val):
    suma = 0
    for li in val:
        digits = re.sub('\D', '', li)
        suma += int(digits[0] + digits[-1])
    return suma


def part2(val):
    suma = 0
    for li in val:
        for key, value in replacements.items():
            li = li.replace(key, value)
        digits_only = re.sub('\D', '', li)
        suma += int(digits_only[0] + digits_only[-1])
    return suma


res1 = str(part1(values))
res2 = str(part2(values))
