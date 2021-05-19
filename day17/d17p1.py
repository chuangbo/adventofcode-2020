#!/usr/bin/env python3

from itertools import product, combinations, permutations
import functools
import math
import copy

filename = 'example.txt'
# filename = 'example2.txt'
# filename = 'input.txt'

min_x = 0
max_x = 0
min_y = 0
max_y = 0
min_z = 0
max_z = 0

def update_range(x, y, z):
    global min_x, max_x, min_y, max_y, min_z, max_z
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    min_z = min(z, min_z)
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    max_z = max(z, max_z)
    # print(x, y, z)
    # print(min_x, max_x, min_y, max_y, min_z, max_z)

space = {}
for y, line in enumerate(open(filename).read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            coord = (x, y, 0)
            space[coord] = '#'
            update_range(x, y, 0)

def debug(space):
    for z in range(min_z, max_z+1):
        print('z =', z)
        print('min y, min x', min_y, min_x)
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                print(space.get((x, y, z), '.'), end='')
            print()
    print()

print(space)
# debug(space)

def cycle(space):
    new_space = copy.copy(space)

    for z in range(min_z-1, max_z+2):
        for y in range(min_y-1, max_y+2):
            for x in range(min_x-1, max_x+2):
                cur = space.get((x, y, z), '.')
                cubes = get_cubes_p1(space, x, y, z)

                if cur == '.' and cubes.count('#') == 3:
                    new_space[(x, y, z)] = '#'
                    update_range(x, y, z)
                if cur == '#' and not (2 <= cubes.count('#') <= 3):
                    del new_space[(x, y, z)]
                    update_range(x, y, z)

    return new_space

def get_cubes_p1(space, x, y, z):
    cubes = []

    for sz in range(z-1, z+2):
        for sy in range(y-1, y+2):
            for sx in range(x-1, x+2):
                if sx == x and sy == y and sz == z:
                    continue
                s = space.get((sx, sy, sz), '.')
                # print((sx, sy, sz), s)
                cubes.append(s)

    return cubes


# print(space.get((1, 0, 0), '.'))

# print(get_cubes_p1(space, 1, 0, 0))

# debug(space)
# space = cycle(space)
# debug(space)

for i in range(6):
    print('cycle', i)
    space = cycle(space)
    # debug(space)

print(list(space.values()).count('#'))