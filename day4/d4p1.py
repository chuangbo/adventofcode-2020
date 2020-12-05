#!/usr/bin/env python3

filename = 'example.txt'
filename = 'input.txt'

count = 0
for passport in open(filename).read().split('\n\n'):
    p = {}

    for pair in passport.split():
        k, v = pair.split(':')
        if k != 'cid':
            p[k] = v
    
    if len(p.keys()) == 7:
        count += 1

print(count)
