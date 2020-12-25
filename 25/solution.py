import sys
sys.path.insert(0,'..')
from advent_lib import *

# Performs the transformation algorithm
def transform(s_num=7, p_key=None, limit=None):
    curr = 1
    loop_size = 1
    while True:
        curr *= s_num
        curr = curr % 20201227

        # If loop size is known and calculating encryption key
        if limit and loop_size == limit:
            return curr

        # If trying to find correct loopsize
        if p_key and curr == p_key:
            return loop_size
        loop_size += 1

# Part 1 solution : 
def part_1():
    card_key, door_key = read_lines("input.txt", f=int)
    c_l_size = transform(p_key=card_key)
    d_l_size = transform(p_key=door_key)

    c_enc_key = transform(s_num=door_key, limit=c_l_size)
    d_enc_key = transform(s_num=card_key, limit=d_l_size)
    assert c_enc_key == d_enc_key
    return c_enc_key


if __name__ == "__main__":
    pretty_print(part_1(), "Merry Christmas!")
