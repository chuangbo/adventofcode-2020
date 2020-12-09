#!/usr/bin/env python3

from itertools import combinations

filename = 'example.txt'
preamble_len = 5
filename = 'input.txt'
preamble_len = 25

lst = []
for line in open(filename):
    n = int(line.strip())
    lst.append(n)

def valid(n, preamble):
    for c in combinations(preamble, 2):
        if sum(c) == n:
            return True
    return False

def find_error(lst, np):
    for i, n in enumerate(lst):
        if i < np:
            continue
        if not valid(n, lst[i-np:i]):
            return n

err = find_error(lst, preamble_len)
print('part1:', err)

def find_contiguous_range(expected, lst):
    for i in range(len(lst)-1):
        acc = 0
        for j in range(i+1, len(lst)):
            n = lst[j]
            acc += n
            if acc == expected:
                l = lst[i:j+1]
                return min(l) + max(l)
            if acc > err:
                break

print('part2:', find_contiguous_range(err, lst))
