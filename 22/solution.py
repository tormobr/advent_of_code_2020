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


def get_winner_score(a):
    res = 0
    for i, x in enumerate(a[::-1]):
        res += (i+1) * x
    return res

# Part 1 solution : 
def part_1():
    data = open("input.txt").read().strip().split("\n\n")
    players = []
    for p in data:
        s = p.split("\n")
        players.append(deque([int(c) for c in s[1:]]))

    player_1 = players[0]
    player_2 = players[1]
    while True:
        #print("player 1: ", player_1)
        #print("player 2: ", player_2)
        c1 = player_1.popleft()
        c2 = player_2.popleft()
        if c1 > c2:
            player_1.append(c1)
            player_1.append(c2)
        elif c2 > c1:
            player_2.append(c2)
            player_2.append(c1)
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
    players = []
    for p in data:
        s = p.split("\n")
        players.append(deque([int(c) for c in s[1:]]))

    player_1 = players[0]
    player_2 = players[1]
    SEEN_2 = set()
    def play(p1, p2, depth):
        SEEN = set()
        while True:
            if tuple(p1) in SEEN:
                if depth == 0:
                    return get_winner_score(list(p1))
                return 0
            if tuple(p2) in SEEN:
                if depth == 0:
                    return get_winner_score(list(p1))
                return 0

            SEEN.add(tuple(p1))
            SEEN.add(tuple(p2))


            c1 = p1.popleft()
            c2 = p2.popleft()

            if len(p1) >= c1 and len(p2) >= c2:
                new_1 = deque(list(p1)[:c1])
                new_2 = deque(list(p2)[:c2])
                winner = play(new_1, new_2, depth+1)
                if winner == 0:
                    p1.extend([c1, c2])
                    #p1.append(c2)
                elif winner == 1:
                    p2.extend([c2, c1])
                continue


            if c1 > c2:
                p1.extend([c1, c2])
            elif c2 > c1:
                p2.extend([c2, c1])


            if len(p1) == 0:
                if depth == 0:
                    return get_winner_score(list(p2))
                return 1
            elif len(p2) == 0:
                if depth == 0:
                    return get_winner_score(list(p1))
                return 0

    return play(player_1, player_2, 0)
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
