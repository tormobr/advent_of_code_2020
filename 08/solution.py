import sys
sys.path.insert(0,'..')
from advent_lib import *

class solver:

    def __init__(self):
        self.acc = 0
        self.index = 0
        self.normal_ret = False
        self.input = self.read_input()
        self.num_op_codes = len(self.input)
        self.op_funcs = {
            "acc": self.op_acc,
            "jmp": self.op_jmp,
            "nop": self.op_nop
        }

    # Reads a input file and stores the data in array
    def read_input(self, filename="input.txt"):
        data = []
        with open(filename) as f:
            for line in f:
                op_code, val = line.split()
                data.append([op_code, int(val)])

        return data

    # Functions to execute each operation
    def op_acc(self, v):
        self.acc += v

    def op_jmp(self, v):
        self.index += v - 1

    def op_nop(self, v):
        pass

    # Main function that loops through all operations and executes them
    def execute_op_codes(self):
        # Reset the acc and the index
        self.acc = 0
        self.index = 0
        SEEN = set()
        while True:
            op_code, val = self.input[self.index]

            if self.index >= self.num_op_codes - 1:
                self.normal_term = True
                break
            if self.index in SEEN:
                self.normal_term = False
                break

            SEEN.add(self.index)

            self.op_funcs[op_code](val)
            self.index += 1

    # Solves part 1 of day 8
    def part_1(self):
        self.execute_op_codes()
        return self.acc


    # Solves part 2 of day 8
    def part_2(self):
        switches = {"nop": "jmp", "jmp": "nop"} # possible switches
        for key, value in switches.items():
            # Get the indexes of the current switch item
            replacements = [i for i, val in enumerate(self.input) if val[0] == key]
            
            # Switch one at a time and try to execute, and check normal termination
            for r in replacements:
                self.input[r][0] = value
                self.execute_op_codes()
                if self.normal_term:
                    return self.acc

                # Swith back if it didn't work out
                self.input[r][0] = key

if __name__ == "__main__":
    s = solver()
    pretty_print(s.part_1(), s.part_2())
