#!/usr/bin/env python3

from itertools import chain
import math

filename = 'example.txt'
filename = 'example2.txt'
filename = 'input.txt'

parts = open(filename).read().split('\n\n')

rules = {}
for line in parts[0].split('\n'):
    name, values = line.split(': ')
    rules[name] = [list(map(int, v.split('-'))) for v in values.split(' or ')]

my_ticket = [int(i) for i in parts[1].split('\n')[1].split(',')]

nearby_tickets = [[int(i) for i in line.split(',')] for line in parts[2].split('\n')[1:]]

def valid_for_rule(r, n):
    return r[0][0] <= n <= r[0][1] or r[1][0] <= n <= r[1][1]

def valid_number(n):
    return any(valid_for_rule(r, n) for r in rules.values())

def part1():
    print('part1:', sum(n for n in chain(*nearby_tickets) if not valid_number(n)))

part1()

def valid_ticket(t):
    return all(valid_number(n) for n in t)

nearby_tickets.append(my_ticket)
valid_tickets = [t for t in nearby_tickets if valid_ticket(t)]

def rule_valid_for_col(va, i):
    for t in valid_tickets:
        # print('debug t', t, va)
        if not valid_for_rule(va, t[i]):
            return False
    return True

def part2():
    rule_valid_cols = {}

    for name, rule in rules.items():
        for i in range(len(my_ticket)):
            if rule_valid_for_col(rule, i):
                rule_valid_cols.setdefault(name, [])
                rule_valid_cols[name].append(i)

    not_found = list(rules.keys())
    rule_col = {}

    while len(not_found) > 0:
        for name in not_found:
            v = rule_valid_cols[name]
            if len(v) > 1:
                continue
            col = v[0]
            # print('valid', name, col)
            rule_col[name] = col
            del rule_valid_cols[name]
            # remove col from other rule_valid_cols
            for vv in rule_valid_cols.values():
                if col in vv:
                    vv.remove(col)
            # delete name from not_found
            not_found.remove(name)

    # print(rule_col)
    # print([col for name, col in rule_col.items() if 'departure' in name])

    print('part2:', math.prod([my_ticket[col] for name, col in rule_col.items() if 'departure' in name]))

part2()
