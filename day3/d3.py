#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

tiles = open(filename).read().splitlines()

width = len(tiles[0])
height = len(tiles)

def count_trees(dx, dy):
    x = 0
    y = 0

    count = 0
    while y < height - 1:
        x += dx
        y += dy

        tx = x % width
        ty = y

        c = tiles[ty][tx]

        # print(x, y, tx, ty, c)
        if c == '#':
            count += 1

    return count

print('part1:', count_trees(3, 1))
print('part2:',
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
)
