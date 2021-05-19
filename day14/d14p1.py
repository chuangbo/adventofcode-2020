#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

mask = None
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

        value |= int(mask.replace('X', '0'), 2)
        value &= int(mask.replace('X', '1'), 2)

        # print('assign', address, value)
        memory[address] = value

print('part1:', sum(memory.values()))
