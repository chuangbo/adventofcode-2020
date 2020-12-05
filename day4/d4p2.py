#!/usr/bin/env python3

import re

filename = 'example.txt'
filename = 'input.txt'

count = 0
for passport in open(filename).read().split('\n\n'):
    p = {}

    for pair in passport.split():
        k, v = pair.split(':')
        if k != 'cid':
            p[k] = v

    # print(p)

    if len(p.keys()) != 7:
        continue

    if not (1920 <= int(p['byr']) <= 2002):
        continue
    if not (2010 <= int(p['iyr']) <= 2020):
        continue
    if not (2020 <= int(p['eyr']) <= 2030):
        continue

    hgt = int(p['hgt'][:-2])
    n = p['hgt'][-2:]
    # print(p['hgt'], hgt, n)

    if n not in ['in', 'cm']:
        continue
    if n == 'in' and not (59 <= hgt <= 76):
        continue
    if n == 'cm' and not (150 <= hgt <= 193):
        continue

    if not re.match(r'#[0-9a-f]{6}', p['hcl']):
        continue

    if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue

    if not re.match(r'^\d{9}$', p['pid']):
        continue

    count += 1

print(count)
