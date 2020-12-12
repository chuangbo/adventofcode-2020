#!/usr/bin/env python3

import functools

filename = 'example.txt'
filename = 'example2.txt'
filename = 'input.txt'

lst = []
for line in open(filename):
    n = int(line.strip())
    lst.append(n)

lst.sort()

lst.insert(0, 0)
lst.append(lst[-1]+3)

diffs = {}

for i in range(1, len(lst)):
    diff = lst[i] - lst[i-1]
    diffs[diff] = diffs.get(diff, 0) + 1

# print(diffs)
print('part1:', diffs[1] * diffs[3])

# I first tried recursion, it turns not that would run til the end of the world
# The key is, to calculate all the arrangements to certain number, the last number (lst[-1]) could never be skipped.
# Because device adapter is always 3+ voltage. So the number of arrangement would be
# the sum of number of arrangement of n-1, n-2, n-3, since they are the numbers can be skipped!
# Thanks yy for the hint!
@functools.cache
def part2(n):
    if n not in lst:
        return 0
    if n == 0:
        return 1
    return part2(n-1) + part2(n-2) + part2(n-3)

print('part2:', part2(lst[-1]))
