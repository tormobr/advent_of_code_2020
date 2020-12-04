import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Extract the passwords into dicts from input file
def get_passwords():
    text = open("input.txt").read()
    text = re.sub(r"(.)\n", r"\1 ", text)
    lines = [[tuple(s.split(":")) for s in l.split()] for l in text.split("\n")]
    passwords = [{k: v for k, v in l} for l in lines]
    return passwords

# Finds all the valid passwords for part 1
def is_valid_1(p):
    return len(p) == 8 or len(p.keys()) == 7 and "cid" not in p.keys()

# Finds all the valid passwords for part 2
def is_valid_2(p):
    return (is_valid_1(p) and 
            is_valid_byr(p) and
            is_valid_iyr(p) and
            is_valid_eyr(p) and
            is_valid_hgt(p) and
            is_valid_hcl(p) and
            is_valid_ecl(p) and
            is_valid_pid(p) and
            is_valid_cid(p))


# ------------------- Functions to test validity --------------------
def is_valid_byr(p):
    return 1920 <= int(p["byr"]) <= 2002

def is_valid_iyr(p):
    return 2010 <= int(p["iyr"]) <= 2020

def is_valid_eyr(p):
    return 2020 <= int(p["eyr"]) <= 2030

def is_valid_hgt(p):
    if re.match(r"(^(1[5-8]\d|19[0-3])cm$|^(([5-6]\d|7[0-6])in)$)", p["hgt"]):
        return True
    return False

def is_valid_hcl(p):
    if re.match(r"^#[\d|a-f]{6}$", p["hcl"]):
        return True
    return False

def is_valid_ecl(p):
    return p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_valid_pid(p):
    if re.match("^\d{9}$", p["pid"]):
        return True
    return False

def is_valid_cid(p):
    return True

#-------------------------------------------------------------------------

     
def part_1():
    PP = get_passwords()
    return sum(is_valid_1(p) for p in PP)

def part_2():
    PP = get_passwords()
    return sum(is_valid_2(p) for p in PP)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
