#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

count = 0
for group in open(filename).read().split('\n\n'):
    lst = []
    for line in group.splitlines():
        ps = set([c for c in line])
        lst.append(ps)

    s = set.intersection(*lst)
    count += len(s)

print(count)
