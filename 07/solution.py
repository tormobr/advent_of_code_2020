from collections import deque, defaultdict
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Parses input and returns a dict representation of graph
def gen_graph():
    data = read_string("input.txt")
    subs = {", ": ",", "\.": "", "bags": "bag", r"(\d)\s": r"\1:"}
    for k, v in subs.items():
        data = re.sub(k, v, data)
    D = defaultdict(dict)
    data = [line.split(" contain ") for line in data.split("\n")][:-1]
    for key, values in data:
        if values == "no other bag":
            continue
        v_list = values.split(",")
        sub_dict = {}
        for v in v_list:
            num, tag = v.split(":")
            sub_dict[tag] = int(num)
        D[key] = sub_dict

    return D

# Part 1 solution : 
def part_1():
    D = gen_graph()
    q = deque([(k, k) for k in D.keys()])
    total = 0
    TARGET = "shiny gold bag"
    SEEN = set()

    while q:
        k, start_node = q.popleft()
        # If parent bag already has been accounted for
        if start_node in SEEN:
            continue

        # if the gold bag is in current bags children
        if TARGET in D[k].keys():
            total += 1 
            SEEN.add(start_node)

        # Append all children of current bag
        for child in D[k]:
            q.appendleft((child, start_node))
    return total

# Part 2 solution : 
def part_2():
    D = gen_graph()
    START = "shiny gold bag"
    q = deque([(START, 1)])
    total = 0

    while q:
        k, multiplier = q.popleft()
        # Get the children and their values of current bag
        for child_key, child_value in D[k].items():
            new_mul = multiplier * child_value
            total += new_mul
            q.appendleft((child_key, new_mul))
    return total


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
