#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

lst = []
for line in open(filename):
    c = line.strip()
    lst.append((c[0], int(c[1:])))

x = 0
y = 0

dx = 10
dy = -1

for c, n in lst:
    if c == 'F':
        x += dx * n
        y += dy * n
    elif c == 'E':
        dx += n
    elif c == 'W':
        dx -= n
    elif c == 'N':
        dy -= n
    elif c == 'S':
        dy += n

    elif c == 'L':
        n //= 90
        for i in range(n):
            dx *= -1
            dx, dy = dy, dx
    elif c == 'R':
        n //= 90
        for i in range(n):
            dy *= -1
            dx, dy = dy, dx

# print(x, y)
print('part2:', x + y)
