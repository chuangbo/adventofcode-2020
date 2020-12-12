#!/usr/bin/env python3

import math
import copy

filename = 'example.txt'
# filename = 'example2.txt'
filename = 'input.txt'

lst = []
for line in open(filename):
    lst.append([ c for c in line.strip()])

w = len(lst[0])
h = len(lst)

def valid_idx(x, y):
    return x >= 0 and y >= 0 and x < w and y < h

def get_first_seat_in_dir(lst, x, y, dx, dy, max_distance):
    sx = x + dx
    sy = y + dy
    d = 1
    while valid_idx(sx, sy) and d <= max_distance:
        s = lst[sy][sx]
        if s == '#' or s == 'L':
            return s
        sx += dx
        sy += dy
        d += 1

# works only for p1
def get_seats_p1(lst, x, y):
    seats = []

    for sy in range(y-1, y+2):
        for sx in range(x-1, x+2):
            if not valid_idx(sx, sy):
                continue
            if sx == x and sy == y:
                continue
            s = lst[sy][sx]
            seats.append(s)

    return seats

# works for p1 and p2
def get_seats_p12(lst, x, y, max_distance):
    seats = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            seats.append(get_first_seat_in_dir(lst, x, y, dx, dy, max_distance))

    return seats

def change_seats(lst, max_distance, tolerance):
    rows = copy.deepcopy(lst)
    count = 0
    for y, line in enumerate(lst):
        for x, s in enumerate(line):
            if s == '.':
                continue

            seats = get_seats_p12(lst, x, y, max_distance)

            if s == 'L' and seats.count('#') == 0:
                rows[y][x] = '#'
                count += 1
            if s == '#' and seats.count('#') >= tolerance:
                rows[y][x] = 'L'
                count += 1
    
    return rows, count

def debug_seats(lst):
    for line in lst:
        print(''.join(line))
    print()

def count_seats(lst):
    return sum(line.count('#') for line in lst)

p1 = copy.deepcopy(lst)
p1_count = None
while p1_count != 0:
    # debug_seats(p1)
    p1, p1_count = change_seats(p1, 1, 4)
    # debug_seats(p1)
    # print(p1_count)

print('part1:', count_seats(p1))

p2 = copy.deepcopy(lst)
p2_count = None
while p2_count != 0:
    # debug_seats(p2)
    p2, p2_count = change_seats(p2, math.inf, 5)
    # debug_seats(p2)
    # print(p2_count)

print('part2:', count_seats(p2))
