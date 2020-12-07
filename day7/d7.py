#!/usr/bin/env python3

import re
import functools

filename = 'example.txt'
filename = 'example2.txt'
filename = 'input.txt'

bag_contents = {}

for line in open(filename):
    bag, content = line.strip().split(' contain ')
    mch = re.match(r'(.+) bag', bag)
    bag = mch.groups()[0]

    if content == 'no other bags.':
        bags = None
    else:
        bags = {}
        for b in content.split(', '):
            n, name = re.match(r'(\d+) (.+) bag', b).groups()
            bags[name] = int(n)
    
    bag_contents[bag] = bags


@functools.cache
def get_flat_content(name):
    bags = bag_contents[name]
    if not bags:
        return {}

    flat = {}
    for bag, bag_n in bags.items():
        flat[bag] = flat.get(bag, 0) + bag_n

        # recursively add bags content
        sub_content = get_flat_content(bag)
        for sub_bag, sub_bag_n in sub_content.items():
            flat[sub_bag] = flat.get(sub_bag, 0) + bag_n * sub_bag_n

    return flat

# print(get_flat_content('light red'))

count_p1 = 0
for bag, content in bag_contents.items():
    content = get_flat_content(bag)
    if 'shiny gold' in content:
        count_p1 += 1
print('part1:', count_p1)

count_p2 = 0
for bag, n in get_flat_content('shiny gold').items():
    count_p2 += n
print('part2:', count_p2)
