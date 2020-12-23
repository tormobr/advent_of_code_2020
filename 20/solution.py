import math
from copy import deepcopy
import numpy as np
from operator import mul
from functools import reduce

import sys
sys.path.insert(0,'..')
from advent_lib import *

sys.setrecursionlimit(100000)

# Generates possible flips and rotations of tile
def flip_rot(grid, ID=None):
    ret = []
    for _ in range(4):
        grid = np.rot90(grid)
        if ID:
            ret.append((ID, deepcopy(grid)))
        else:
            ret.append(deepcopy(grid))
    grid = grid[::-1]
    for _ in range(4):
        grid = np.rot90(grid)
        if ID:
            ret.append((ID, deepcopy(grid)))
        else:
            ret.append(deepcopy(grid))
    return ret

# Removes the borders of tile
def strip_grid(grid):
    return grid[1:-1, 1:-1]

# Check if current layout is valid
def check_match(x, y, fill):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr = fill[y][x]
    grids = [[] for _ in range(4)]
    for i, (dy, dx) in enumerate(dirs):
        new_x = dx + x
        new_y = dy + y
        if new_x < 0 or new_x > len(fill)-1:
            continue
        if new_y < 0 or new_y > len(fill)-1:
            continue
        new_grid = fill[new_y][new_x]
        grids[i] = new_grid
    
    right, down, left, up = grids[0], grids[1], grids[2], grids[3]
    if len(up) > 0 and not np.all(curr[0] == up[-1]):
        return False
    if len(down) > 0 and not np.all(curr[-1] == down[0]):
        return False
    if len(left) > 0 and not np.all(curr[:,0] == left[:,-1]):
        return False
    if len(right) > 0 and not np.all(curr[:,-1] == right[:,0]):
        return False
    return True

# Stitches all tiles together to big picture
def stitch_grids(grid_list):
    grids = [[strip_grid(g) for g in row] for row in grid_list]
    hor = np.array([np.hstack([g for g in grids[i]]) for i in range(len(grids))])
    return np.vstack(hor)

# Constructs the image from tiles
def create_image():
    D = {}
    for tile in open("input.txt").read().split("\n\n"):
        lines = tile.strip().split("\n")
        ID = ints(lines[0])[0]
        D[ID] = np.array([[x.strip() for x in line] for line in lines[1:]])

    # Create data structures
    sq = int(math.sqrt(len(D.keys())))
    fill = [[[] for x in range (sq)] for row in range(sq)]
    fill_ID = [[None]*sq for row in range(sq)]

    # Generate possible rotations and flips of all grids
    possible = []
    for ID, grid in D.items():
        possible.extend(flip_rot(grid, ID))

    # Some vars
    SEEN = set()
    res_ids = []
    res_tiles = []

    # reset certain values on backtrack
    def back_track(x, y, ID):
        SEEN.remove(ID)
        fill[y][x] = []
        fill_ID[y][x] = None

    def rec(current, ID, x, y):
        if ID in SEEN or res_ids:
            return

        SEEN.add(ID)
        fill[y][x] = deepcopy(current)
        fill_ID[y][x] = ID
        if x == len(fill) -1 and y == len(fill)-1:
            res_ids.append(fill_ID.copy())
            res_tiles.append(fill.copy())
            return 

        if not check_match(x, y, fill):
            back_track(x, y, ID)
            return

        for new_ID, n in possible:
            if res_ids:
                return 

            if x == len(fill)-1:
                new_x = 0
                new_y = y+1
            else:
                new_x = x+1
                new_y =  y

            ret = rec(n, new_ID,  new_x, new_y)
        back_track(x, y, ID)

   

        
    # Call recursive functions starting at every possible tile variant
    for i, (ID, p) in enumerate(possible):
        SEEN = set([])
        ret = rec(p, ID, 0, 0)

    return res_tiles[0], res_ids[0]

def part_1():
    _, ids = create_image()
    return reduce(mul, [ids[0][0], ids[0][-1], ids[-1][0], ids[-1][-1]])

def part_2():
    tiles, _ = create_image()
    main_grid = stitch_grids(tiles)
    orients  = flip_rot(main_grid)
    for grid in orients:
        count = count_monsters(grid)

        # "#" in monster = 15
        if count > 0:
            res = np.count_nonzero(grid == "#")
            return res - (count * 15 )

def count_monsters(grid):
    m1 = "                  # "
    m2 = "#    ##    ##    ###"
    m3 = " #  #  #  #  #  #   "
    monster = [list(m1), list(m2), list(m3)]
    mh = 3
    mw = len(m1)
    
    H, W = grid.shape
    c = 0
    for y, row in enumerate(grid):
        if y >= (H - mh):
            break
        for x, elem in enumerate(grid):
            if x >= (W - mw):
                break

            pot_mon = grid[y:y+mh, x:x+mw]
            found = True
            for r1, r2 in zip(monster, pot_mon):
                for e1, e2 in zip(r1, r2):
                    if e1 == " ":
                        continue
                    if e1 != e2:
                        found = False
                        break
            if found:
                c += 1

    return c

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
