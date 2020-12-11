from copy import deepcopy
from numba import njit
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

def create_int_grid(grid):
    int_grid = np.zeros(grid.shape)
    mapping = {"#": -1, "L": 1, ".": 0}
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            int_grid[y, x] = mapping[elem]
    return int_grid

# Part 1 solution : 
def part_1(grid, max_dist=100000):


    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    arrays = [] 
    while True:
        new_grid = grid.copy()
        anim_arr = np.zeros(new_grid.shape)
        arrays.append(new_grid.copy())
        for y, row in enumerate(grid):
            for x, elem in enumerate(row):
                if grid[y, x] == 0:
                    continue
                tot = 0
                for dx, dy in dirs:
                    for dist in range(1, max_dist):
                        new_x = x + dx*dist
                        new_y = y + dy*dist
                        if new_x < 0 or new_x > len(grid[0])-1:
                            break
                        if new_y < 0 or new_y > len(grid) -1:
                            break
                        new_val = grid[new_y, new_x]
                        if new_val == -1:
                            tot += 1
                            break
                        elif new_val == 1:
                            break
                if grid[y, x] == 1:
                    if tot == 0:
                        new_grid[y, x] = -1

                elif grid[y, x] == -1:
                    if tot >= 5:
                        new_grid[y, x] = 1

        # If no changes in the last step
        if np.array_equal(grid, new_grid):
            # delay last frame in animation
            for _ in range(10):
                arrays.append(grid)

            return np.count_nonzero(grid == -1), arrays
        grid = new_grid

    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    grid = np.array(read_lines_sep("input.txt", sep="", f=str))
    grid = create_int_grid(grid)
    ret, arrays = part_1(grid)
    animate(arrays, save=False, cmap=["darkred", "white", "darkgreen"], interval=300)
    pretty_print(ret, part_2())
