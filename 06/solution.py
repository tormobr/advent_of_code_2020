from collections import Counter
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Gets a count of every batch in the file
def get_counts():
    text = open("input.txt").read()
    batches = re.split(r"\n\n", text)
    ret = []
    for b in batches:
        l = b.split("\n")
        reps = len(l)
        c = Counter(c for ans in l for c in ans)
        ret.append((c, reps))
    return ret

# Part 1 solution : 
def part_1():
    counts = get_counts()
    return sum(len(c.keys()) for c,reps in counts)

# Part 2 solution : 
def part_2():
    counts = get_counts()
    return sum(sum(v == reps for v in c.values()) for c,reps in counts)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
