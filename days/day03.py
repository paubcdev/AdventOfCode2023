import re

lines = list(open('../inputs/input_day03.txt', 'r'))

symbols = {}
gears = {}
res1int = 0
for row in range(len(lines[0]) - 1):
    for col in range(len(lines)):
        if lines[row][col] not in '0123456789.':
            symbols[(row, col)] = lines[row][col]
            if lines[row][col] == '*':
                gears[(row, col)] = []

for row_num, row in enumerate(lines):
    for c in re.finditer(r'\d+', row):
        possibilities = []
        for i in range(c.start() - 1, c.end() + 1):
            possibilities.append((row_num - 1, i))
            possibilities.append((row_num, i))
            possibilities.append((row_num + 1, i))
        valid = False
        for p in possibilities:
            if p in symbols:
                valid = True
                if p in gears:
                    gears[p].append(int(c.group()))
        if valid:
            res1int += int(c.group())

res2int = 0
for g in gears:
    if len(gears[g]) == 2:
        res2int += (gears[g][0] * gears[g][1])

res1 = str(res1int)
res2 = str(res2int)
