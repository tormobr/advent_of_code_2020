from copy import deepcopy
import math
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
    grid = read_lines_sep("input.txt", sep="", f=str)


    dirs = [(1,0), (0,1), (1,1), (-1,0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
    its = 0
     
    while True:
        its += 1
        new_grid = deepcopy(grid)
        for y, row in enumerate(grid):
            for x, elem in enumerate(row):
                if grid[y][x] == ".":
                    continue
                tot = 0
                for dx, dy in dirs:
                    for dist in range(1, max(len(grid), len(grid[0]))):
                        new_x = x + dx*dist
                        new_y = y + dy*dist
                        if new_x < 0 or new_x > len(grid[0])-1:
                            break
                        if new_y < 0 or new_y > len(grid) -1:
                            break
                        if grid[new_y][new_x] == "#":
                            tot += 1
                            break
                        elif grid[new_y][new_x] in ["L"]:
                            break
                if grid[y][x] == "L":
                    if tot == 0:
                        new_grid[y][x] = "#"

                elif grid[y][x] == "#":
                    if tot >= 5:
                        new_grid[y][x] = "L"

        #for hax in new_grid:
            #print("".join(hax))
        #print("\n------\n")
        #time.sleep(10)

        if grid == new_grid:
            ret = 0
            for hax in grid:
                for elem in hax:
                    if elem == "#":
                        ret += 1
            return ret, its
        grid = new_grid

    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
