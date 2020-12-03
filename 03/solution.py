from collections import deque, defaultdict
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
    grid = [[c for c in s] for s in read_lines("input.txt",f=str)]
    dx = 3
    dy = 1
    x = 0
    y = 0

    trees = 0
    print(grid)
    while True:
        if y >= len(grid):
            break
        if grid[y][x] == "#":
            trees += 1
        x = (x + dx) % len(grid[0])
        y += dy
    return trees

# Part 2 solution : 
def part_2():
    grid = [c for c in read_lines("input.txt",f=str)]
    dx = 3
    dy = 1
    x = 0
    y = 0
    ds = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    prod = 1
    for dx, dy in ds:
        trees = 0
        x = 0
        y = 0
        while True:
            if y >= len(grid):
                break
            if grid[y][x] == "#":
                trees += 1
            x = (x + dx) % len(grid[0])
            y += dy
        prod *= trees
        print(trees)
    return prod


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
