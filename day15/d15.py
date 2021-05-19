#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

lst = []
for line in open(filename):
    lst.append([int(i) for i in line.strip().split(',')])

def memory_game(numbers, last_turn):
    spoken = {}
    turn = 1
    last = None
    for i in numbers:
        spoken[i] = [turn]
        turn += 1
        last = i
    while turn <= last_turn:
        # print(spoken, turn, last)
        last_spoken = spoken[last]
        if len(last_spoken) == 1:
            last = 0
        else:
            last = last_spoken[-1] - last_spoken[-2]

        # print(turn, last)
        last_two = spoken.get(last, [])
        last_two.append(turn)
        spoken[last] = last_two[-2:]
        turn += 1
    
    return last

for numbers in lst:
    print('part1:', memory_game(numbers, 2020))
    print('part1:', memory_game(numbers, 30000000))
