#!/usr/bin/env python3

import os

filename = 'example.txt'
filename = 'input.txt'

def open_local(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    return open(filename)

lines = open_local(filename).readlines()

start = int(lines[0])

buses = []
for i, b in enumerate(lines[1].split(',')):
    if b == 'x':
        continue
    buses.append([i, int(b)])

# print(buses)

def part1():
    t = start
    while True:
        for _, b in buses:
            if t % b == 0:
                return (t - start) * b
        t += 1

print('part1:', part1())

def part2():
    t = 0
    increment = 1

    for dt, b in buses:
        while (t + dt) % b != 0:
            # print(t, increment, t + dt, [dt, b])
            t += increment
        # Because all the bus numbers are prime numbers,
        # the next increment is the common multiple for all the matched numbers
        increment *= b

    return t

print('part2:', part2())
