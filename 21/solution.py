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

# Removes all alergens that possibly cant be the source
def remove_non_alerg(D, food_items):
    new_food_items = set()
    DD = defaultdict(list)

    for f in food_items:
        for a, foods in D.items():
            if all(f in x for x in foods):
                DD[a].append(f)
                new_food_items.add(f)

    return new_food_items, DD

# Part 1 solution : 
def extract_data():
    data = read_lines("input.txt", f=str)
    all_foods = []
    D = defaultdict(list)

    # Reading the data into dict
    for line in data:
        food, alerg = line.split("(")
        food_list = food.split()
        all_foods.extend(food_list)

        alerg = re.sub(r"(contains |\))", "", alerg)
        alerg_list = [a.strip() for a in alerg.split(",")]

        for a in alerg_list:
            D[a].append(food_list)
    for i in D.items():
        print(i)

    return set(all_foods), D, all_foods

# Solution to part 1
def part_1():
    food_set, D, all_foods = extract_data()
    SF, SD = remove_non_alerg(D, food_set)

    # Count the number of ingridients that are not valid
    return sum(f not in SF for f in all_foods)

# Solves part 2
def part_2():
    food_set, D, all_foods = extract_data()
    food_set, D = remove_non_alerg(D, food_set)

    q = deque([{}])
    while q:
        path = q.popleft() 
        for a, values in D.items():
            if a in [a for a, v in path.items()]:
                continue
            for v in values:
                if v in [v for a, v in path.items()]:
                    continue
                new_path = deepcopy(path)
                new_path[a] = v
                if len(new_path) == len(food_set):
                    return ",".join(v for x, v in sorted(new_path.items(), key=lambda x: x[0]))

                q.appendleft(new_path)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
