#!/usr/bin/env python3

from itertools import product

filename = 'example2.txt'
filename = 'input.txt'

memory = {}
for line in open(filename):
    line = line.strip()
    if line.startswith('mask = '):
        mask = line.replace('mask = ', '')
        # print('mask =', mask)
    else:
        address, value = line.split(' = ')
        address = int(address[4:-1])
        value = int(value)
        # print('assign', address, value)

        address |= int(mask.replace('X', '0'), 2)

        mask_xs = [len(mask)-1-i for i, x in enumerate(mask) if x == 'X']

        for xs in product([0, 1], repeat=len(mask_xs)):
            for offset, b in zip(mask_xs, xs):
                if b == 0:
                    address &= ~(1 << offset)
                if b == 1:
                    address |= 1 << offset
            # print('assign', address, value)
            memory[address] = value

print('part2:', sum(memory.values()))
