#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

lst = []
for line in open(filename):
    c = line.strip()
    lst.append((c[0], int(c[1:])))

vs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
vi = 0

x = 0
y = 0
for c, n in lst:
    if c == 'F':
        v = vs[vi]
        x += v[0] * n
        y += v[1] * n
    elif c == 'E':
        x += n
    elif c == 'W':
        x -= n
    elif c == 'N':
        y -= n
    elif c == 'S':
        y += n

    elif c == 'L':
        n //= 90
        vi = (vi - n) % 4
    elif c == 'R':
        n //= 90
        vi = (vi + n) % 4

# print(x, y)
print('part1:', abs(x) + abs(y))
