import time
import os
from matplotlib import pyplot as plt
from matplotlib import animation,colors
import numpy as np
import re

HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

WHITE_SQUARE = "\u25a0"

DIRECTIONS = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0)
}

SPIN_DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Reads each number on each line in file and return list
def read_lines(filename, f=int, use_file=True):
    if use_file:
        return [f(l.strip()) for l in open(filename)]

    return [f(l.strip()) for l in filename.split("\n")[:-1]]


# Read a file as string
def read_string(filename, use_file=True):
    if use_file:
        return open(filename).read()

    return filename


# Reads file and splits on seperator
def read_sep(filename, sep=None, f=str, use_file=True):
    if use_file:
        return [f(x.strip()) for x in open(filename).read().split(sep)]

    return [f(x.strip()) for x in filename.split(sep)]


# Reads each line and seperate items on line into 2D array
def read_lines_sep(filename, sep=None, f=str, use_file=True):
    if use_file:
        if sep == "":
            return [[f(c) for c in s.strip()] for s in open("input.txt")]
        return [[f(s.strip()) for s in x.split(sep)] for x in open(filename)]

    if sep == "":
        return [[f(c) for c in s.strip()] for s in filename]
    return [[f(s.strip()) for s in x.strip().split(sep)] for x in filename.split("\n")[:-1]]

# Finds all the integers in string
def ints(s):
    return re.findall(r"-?\d+", s)

# Prints array items
def print_arr(arr):
    for x in arr:
        print(x)


# Draw matrix in terminal
def draw_matrix(m, mapping={1: WHITE_SQUARE + " ", 0:"  "}):
    s = "" 
    for row in m:
        s += "\t"
        for item in row:
            if item not in mapping.keys():
                item = 0
            s += mapping[item]
        s += "\n"
    print(s)
    return s

# Shows image of matrix
def plot_matrix(m, cmap="plasma"):
    plt.imshow(m, cmap=cmap)
    plt.show()


# Creates an animation from a set of matrices from the constructor
# Used for grid layout that changes
def animate(arrays, filename="ani.mp4", save=False, border_width=.1, fps=60, cmap=["darkgray", "white", "black"], aspect_ratio=1, interval=10):
    #ax.figure(figsize=(20,10))
    cmap1 = colors.ListedColormap(cmap)
    arrays = arrays
    fig, (ax) = plt.subplots()
    fig.tight_layout()
    fig.set_size_inches(18.5, 10.5)
    ax.set_aspect(aspect_ratio, adjustable='box')
    plts = []
    for a in arrays:
        mat = ax.pcolormesh(a, edgecolor="lightgrey", cmap=cmap1, linewidth=border_width)
        plts.append([mat])
    ani = animation.ArtistAnimation(fig, plts, blit=True, interval=interval)
    plt.gca().invert_yaxis()
    ax.axis("off")
    plt.show()
    if save:
        cwd = os.getcwd()
        if "animations" not in os.listdir(cwd):
            os.mkdir("animations")
        ani.save(f"animations/{filename}")



# Pretty prints the results
def pretty_print(part_1, part_2):
    print(f"\n{WARNING}RESULTS:\n------------------------------------{ENDC}")
    print(f"{HEADER}Part 1: {OKGREEN} {part_1}{ENDC}")
    print(f"{HEADER}Part 2: {OKGREEN} {part_2}{ENDC}")
    print(f"{WARNING}------------------------------------\n{ENDC}")



if __name__ == "__main__":
    print(read_lines("test_input/1.txt", int))
    print(read_string("test_input/2.txt"))
    print(read_sep("test_input/3.txt", ",", int))
    print(read_lines_sep("test_input/4.txt", ",", str))



