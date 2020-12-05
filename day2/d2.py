#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

p1_count = 0
p2_count = 0
for line in open(filename):
    rge, c, pswd = line.split(' ')
    a, b = rge.split('-')
    a = int(a)
    b = int(b)
    c = c[0]

    # print(a, b, c, pswd)

    n = pswd.count(c)
    if a <= n <= b:
        p1_count += 1

    if (pswd[a-1] == c) != (pswd[b-1] == c):
        p2_count += 1

print('part1:', p1_count)
print('part2:', p2_count)
