import numpy as np
import sys
sys.path.insert(0,'..')
from advent_lib import *

# Gets the ids from the input data
def extract_ids():
    # Animation stuff   ----------------------
    arrays = []
    grid = np.zeros((8, 128))
    # ----------------------------------------
    data = read_lines("input.txt", f=str)
    res = []
    for s in data:
        row = sum([int(c=="B") << 6-i for i, c in enumerate(s[:7])])
        col = sum([int(c=="R") << 2-i for i, c in enumerate(s[7:])])
        res.append(row * 8 + col)

    # Animation stuff   -------------------------------------
        grid[col, row] = 1
        arrays.append(grid.copy())
    
    # Set "my" seat to orange and duplicate last frame some times
    grid[5, 81] = 2
    for _ in range(250):
        arrays.append(grid.copy())
    # -------------------------------------------------------


    res.sort()
    return res, arrays

# Part 1 solution : 
def part_1():
    res, arrays = extract_ids()
    return max(res)

# Part 2 solution : 
def part_2():
    res, arrays = extract_ids()
    animate(arrays, cmap=["white", "orange", "green"], border_width=.1, aspect_ratio=1, save=False)
    for i, ID in enumerate(res[:-1]):
        if res[i] != res[i+1] - 1:
            return ID + 1

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
