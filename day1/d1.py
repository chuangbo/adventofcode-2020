#!/usr/bin/env python3

from itertools import combinations
import math

filename = 'example.txt'
filename = 'input.txt'

lst = [int(line.strip()) for line in open(filename)]

def find_sum(n):
    for c in combinations(lst, n):
        if sum(c) == 2020:
            return math.prod(c)

print('part1:', find_sum(2))
print('part2:', find_sum(3))
