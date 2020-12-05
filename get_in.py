import sys
from aocd.models import Puzzle

day = int(sys.argv[1])

puzzle = Puzzle(year=2020, day=day)

print(puzzle.input_data)
