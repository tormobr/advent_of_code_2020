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


# Gets the final score based on cards and index
def get_winner_score(a):
    return sum(x * (i+1) for i, x in enumerate(a[::-1]))

# Part 1 solution : 
def part_1():
    data = open("input.txt").read().strip().split("\n\n")
    player_1, player_2 = [deque(int(c) for c in line.split("\n")[1:]) for line in data]

    while True:
        c1, c2 = player_1.popleft(), player_2.popleft()

        if c1 > c2:
            player_1.extend([c1, c2])
        elif c2 > c1:
            player_2.extend([c2, c1])
        else:
            assert False

        if len(player_1) == 0:
            return get_winner_score(list(player_2))
        elif len(player_2) == 0:
            return get_winner_score(list(player_1))

        

    return None

# Part 2 solution : 
def part_2():
    data = open("input.txt").read().strip().split("\n\n")
    player_1, player_2 = [deque(int(c) for c in line.split("\n")[1:]) for line in data]
 
    # Recursive function to play rounds and games with new rules
    def play(p1, p2, depth):
        SEEN = set()
        while True:
            if tuple(p1) in SEEN:
                return get_winner_score(list(p1)), 0
            if tuple(p2) in SEEN:
                return get_winner_score(list(p1)), 0

            SEEN |= set([tuple(p1), tuple(p2)])


            c1, c2 = p1.popleft(), p2.popleft()

            if len(p1) >= c1 and len(p2) >= c2:
                new_1, new_2 = deque(list(p1)[:c1]), deque(list(p2)[:c2])
                score, winner = play(new_1, new_2, depth+1)
                if winner == 0:
                    p1.extend([c1, c2])
                elif winner == 1:
                    p2.extend([c2, c1])
                continue


            if c1 > c2:
                p1.extend([c1, c2])
            elif c2 > c1:
                p2.extend([c2, c1])


            if len(p1) == 0:
                return get_winner_score(list(p2)), 1
            elif len(p2) == 0:
                return get_winner_score(list(p1)), 0

    return play(player_1, player_2, 0)[0]


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
