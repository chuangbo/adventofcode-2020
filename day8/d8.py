#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

cmds = []
for line in open(filename):
    cmd, arg = line.strip().split()
    cmds.append([cmd, int(arg)])

def compute(cmds):
    i = 0
    acc = 0
    ran = {}

    while True:
        cmd, arg = cmds[i]
        ran[i] = True

        if cmd == 'nop':
            i += 1
        elif cmd == 'acc':
            acc += arg
            i += 1
        elif cmd == 'jmp':
            i += arg

        if i in ran:
            return False, acc
        elif i >= len(cmds):
            return True, acc

result, acc = compute(cmds)
print('part1:', acc)

fixes = {
    'jmp': 'nop',
    'nop': 'jmp',
}
for i, [cmd, arg] in enumerate(cmds):
    if cmd not in fixes:
        continue

    new = cmds[:]
    new[i] = [fixes[cmd], arg]
    
    result, acc = compute(new)
    if result:
        print('part2:', acc)
        break
