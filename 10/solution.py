from collections import deque, defaultdict, Counter

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=int)
    sort = sorted(data + [0, max(data) + 3])

    diffs = defaultdict(int)
    for i, current_adapter in enumerate(sort[:-1]):
        next_adapters = [n for n in sort[i+1:i+4] if n - current_adapter <= 3]
        diffs[min(next_adapters) - current_adapter] += 1
    return diffs[1] * diffs[3]

# Part 2 solution 
def part_2():
    data = read_lines("input.txt", f=int)

    # Adding 0 and built in adapter and sorting
    sort = sorted(data + [0, max(data) + 3])
    N = len(sort) -1
    FOUND = {}

    # Asserting distinct
    assert all(c == 1 for c in Counter(sort).values())

    def rec(i):
        current = sort[i]
        if i >= N:
            return 1
        # If path has been explored from this point and out
        if i in FOUND.keys():
            return FOUND[i]

        # call function recursively and sum up the total and add to dict
        tot = sum(rec(j+i+1) for j, x in enumerate(sort[i+1:i+4]) if x - current <= 3)
        FOUND[i] = tot

        return tot
    
    return rec(0)

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
