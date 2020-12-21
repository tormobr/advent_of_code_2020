import sys
import math
from collections import deque, defaultdict, Counter
from copy import deepcopy
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

sys.setrecursionlimit(100000)

# finds the number of valid strings by recursion
def solve(p2=False):
    data = read_lines("input.txt", f=str)
    strings = read_lines("text.txt", f=str)

    d = defaultdict(list)
    for line in data:
        n, rules = line.split(":")
        if "\"" not in line:
            rules = rules.strip()
            rules = rules.split("|")
            for r in rules:
                hax = r.split()
                d[int(n)].append([int(x) for x in hax])
        else:
            r = re.sub(r"\"", "", rules)
            d[int(n)].append([r.strip()])

    # Change input if part 2
    if p2:
        d[8] = [[42], [42, 8]]
        d[11] = [[42, 31], [42, 11, 31]]
        d[0] = []
        for i in range(1, 40):
            for j in range(1, 40):
                d[0].append(([8]*i) + ([11]*j))

    def rec(index, s, rule, depth):
        if index == len(s):
            return False, 0

        current = s[index]

        if type(d[rule][0][0]) == str:
            good = d[rule][0][0] == current
            return good, int(good)
        else:
            sub_rules = d[rule]

            for r_list in sub_rules:
                skip = 0
                for i, r in enumerate(r_list):
                    ret, strudel = rec(index + skip, s, r, depth+1)
                    if not ret:
                        break
                    skip += strudel

                else:
                    if depth == 0 and index + skip != len(s):
                        return False, 0
                    return True, skip

            return False, 0

    res = []
    for s in strings:
        ret,_ = rec(0, s, 0, 0)
        if ret == True:
            res.append(s)

    return len(res)

        


    return None

# Part 1 solution : 
def part_1():
    return solve()

# Part 2 solution : 
def part_2():
    return solve(p2=True)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
