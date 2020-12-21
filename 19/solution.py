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

directions = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0)
}

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part 1 solution : 
def part_1():
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

    for i in d.items():
        print(i)

    d[0] = []
    for i in range(1, 40):
        for j in range(1, 40):
            d[0].append(([8]*i) + ([11]*j))

    def rec(index, s, rule, depth):
        if index == len(s):
            #print("TOOO LONG", index, s)
            #time.sleep(2)
            return False, 0

        current = s[index]
        #print("\nnew rec here!!! index:", index)
        #print("rule: ", rule)
        #print("d[rule, 0,0], current: ", d[rule][0][0], current)

        if type(d[rule][0][0]) == str:
            #print("returing from rec", d[rule][0][0] == current)
            good = d[rule][0][0] == current
            return good, int(good)
        else:
            sub_rules = d[rule]

            for r_list in sub_rules:
                #print("Exploring sub_rules: ", r_list)
                skip = 0
                for i, r in enumerate(r_list):
                    ret, strudel = rec(index + skip, s, r, depth+1)
                    #if strudel == -1 and r != r_list[-1]:
                        #return False, 0
                    if not ret:
                        break
                    skip += strudel

                else:
                    if depth == 0 and index + skip != len(s):
                        return False, 0
                    #print("returning with success: ", depth, index, skip, index+skip, s)
                    return True, skip
                #print("Exploring sub_rules: ", r_list, sub_rules)

            return False, 0

    res = []
    for s in strings:
        print(s)
        ret,_ = rec(0, s, 0, 0)
        if ret == True:
            res.append(s)

    print("\n RES: \n")
    for s in res:
        print(s)
    return res, len(res)

        


    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
