#!/usr/bin/env python3

def find_idx(line, last):
    start = 0
    end = last
    for c in line.strip():
        mid = int((end - start) / 2)
        if c == 'F' or c == 'L':
            end = start + mid
        else:
            start = start + mid

    return start

# print(find_idx('FBFBBFFRLR'[:7], 128))
# print(find_idx('FBFBBFFRLR'[7:], 8))

filename = 'example.txt'
filename = 'input.txt'

sids = []
for line in open(filename):
    idx = find_idx(line[:7], 128)
    col = find_idx(line[7:], 8)
    sid = idx * 8 + col
    sids.append(sid)

print('part1:', max(sids))

prev = None
for cur in sorted(sids):
    if prev and cur - prev == 2:
        print('part2:', prev + 1)
    prev = cur
