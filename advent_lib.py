HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


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
def read_sep(filename, sep, f=str, use_file=True):
    if use_file:
        return [f(x.strip()) for x in open(filename).read().split(sep)]

    return [f(x.strip()) for x in filename.split(sep)]


# Reads each line and seperate items on line into 2D array
def read_lines_sep(filename, sep=None, f=str, use_file=True):
    if use_file:
        return [[f(s.strip()) for s in x.split(sep)] for x in open(filename)]

    return [[f(s.strip()) for s in x.split(sep)] for x in filename.split("\n")[:-1]]


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



