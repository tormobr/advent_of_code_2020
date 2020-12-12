from numba import njit
import numpy as np

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Changes input grid to integers instead of strings
# Done for making the animations
def create_int_grid(grid):
    int_grid = np.zeros(grid.shape)
    mapping = {"#": -1, "L": 1, ".": 0}
    for y, row in enumerate(grid):
        for x, elem in enumerate(row):
            int_grid[y, x] = mapping[elem]
    return int_grid

@njit()
def play(grid, max_dist=1, num_occ=4):
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    arrays = [] 
    H, W = grid.shape
    while True:
        new_grid = grid.copy()
        arrays.append(new_grid)
        for y, row in enumerate(grid):
            for x, elem in enumerate(row):
                # If current seat is not a seat, continue
                if grid[y, x] == 0:
                    continue

                tot = 0     # The total number of neighbors that are occupied
                for dx, dy in dirs:
                    for dist in range(1, max_dist+1):
                        new_x = x + dx*dist
                        new_y = y + dy*dist

                        # Test if array indexes are out of bounds
                        if not 0 <= new_x < W or not 0 <= new_y < H:
                            break
                        new_val = grid[new_y, new_x]
                        if new_val == -1:
                            tot += 1
                        if new_val != 0:
                            break

                # Set the new values with regards to the rules of seatchanging
                if grid[y, x] == 1 and tot == 0:
                    new_grid[y, x] = -1

                elif grid[y, x] == -1 and tot >= num_occ:
                    new_grid[y, x] = 1

        # If no changes in the last step
        if np.array_equal(grid, new_grid):
            # delay last frame in animation
            for _ in range(10):
                arrays.append(grid)

            return np.count_nonzero(grid == -1), arrays

        # Apply new changes to grid
        grid = new_grid

# Part 1 solution : 
def part_1():
    grid = np.array(read_lines_sep("input.txt", sep="", f=str))
    grid = create_int_grid(grid)
    res, arrays = play(grid, max_dist=1)
    #animate(arrays, filename="part1.mp4", save=True, cmap=["darkred", "white", "darkgreen"], interval=200)
    return res

# Part 2 solution : 
def part_2():
    grid = np.array(read_lines_sep("input.txt", sep="", f=str))
    grid = create_int_grid(grid)
    res, arrays = play(grid, max_dist=max(len(grid), len(grid[0])), num_occ=5)
    #animate(arrays, filename="part2.mp4", save=True, cmap=["darkred", "white", "darkgreen"], interval=200)
    return res


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
