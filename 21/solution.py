from copy import deepcopy
import math
from collections import deque, defaultdict, Counter
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    data = read_lines("input.txt", f=str)
    all_foods = []
    food_set = set()
    all_alerg = set()
    D = defaultdict(list)
    DD = defaultdict(set)
    nums = defaultdict(int)
    FOODS = []

    for line in data:
        food, alerg = line.split("(")
        food_list = food.split()
        all_foods.extend(food_list)
        food_set |= set(food_list)

        alerg = re.sub(r"(contains |\))", "", alerg)
        alerg = re.sub(",", "", alerg)
        alerg_list = alerg.split()
        all_alerg  |= set(alerg_list)
        for a in alerg_list:
            nums[a] += 1

        for f in food_list:
            for a in alerg_list:
                D[a].append(f)
                DD[a].add(f)
        for a in alerg_list:
            FOODS.append((a, food_list))

    ret = 0
    non_alerg = []
    for f in all_foods:
        for a, foods in D.items():
            c = Counter(foods)
            if c[f] >= nums[a]:
                break
        else:
            #print("adding:", f)
            non_alerg.append(f)
            ret += 1 
    for n in non_alerg:
        for i, (a, f) in enumerate(FOODS):
            if n in f:
                FOODS[i][1].remove(n)
                if n in food_set:
                    food_set.remove(n)


    ALL_FOODS = defaultdict(list)
    for a, v in FOODS:
        ALL_FOODS[a].append(v)

            
    # Solves part 2
    res = {}
    q = deque([{}])
    while q:
        path = q.popleft() 
        print(path)
        for a, values in ALL_FOODS.items():
            if a in [a for a, v in path.items()]:
                continue
            for curr in food_set:
                if curr in [v for a, v in path.items()]:
                    continue
                if all(curr in rec for rec in values):
                    new_path = deepcopy(path)
                    new_path[a] = curr
                    if len(new_path) == len(food_set):
                        res = new_path
                        return ret, ",".join(v for x, v in sorted(res.items(), key=lambda x: x[0]))
                    q.appendleft(new_path)


# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
