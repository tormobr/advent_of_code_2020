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
        return [[f(s.strip()) for s in x.split(sep)] for x in open(filename)]

    return [[f(s.strip()) for s in x.split(sep)] for x in filename.split("\n")[:-1]]

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
def animate(arrays, filename="ani.gif", save=False, border_width=1, fps=60, greys=False):
    cmap1 = colors.ListedColormap(['darkgrey','white', 'black'])
    arrays = arrays
    fig, (ax) = plt.subplots()
    fig.tight_layout()
    ax.set_aspect('equal', adjustable='box')
    mat = ax.pcolormesh(arrays[0], edgecolor="lightgrey", cmap=cmap1 if greys else "plasma", linewidth=border_width)
    ani = animation.FuncAnimation(fig, lambda i: mat.set_array(arrays[i]), interval=10,frames=len(arrays)-1)
    plt.gca().invert_yaxis()
    ax.axis("off")
    plt.show()

    if save:
        cwd = os.getcwd()
        if "animations" not in os.listdir(cwd):
            os.mkdir("animations")
        ani.save(f"animations/{filename}", fps=fps, writer="ffmpeg", dpi=200)



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



