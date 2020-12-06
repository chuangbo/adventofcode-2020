#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

count = 0
for group in open(filename).read().split('\n\n'):
    s = set([c for c in group if c != '\n'])
    count += len(s)

print(count)
