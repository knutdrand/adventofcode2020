from itertools import groupby
test_input = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
""".split("\n")


test_input2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1\
""".split("\n")
def parse_input(lines):
    groups = groupby(lines, lambda x: x.startswith("mask"))
    cur_mask = None
    for is_mask, group in groups:
        split_lines = (line.split(" = ") for line in group)
        if is_mask:
            cur_mask = next(split_lines)[1].strip()
        else:
            yield cur_mask, ((int(p[0][4:-1]), int(p[1])) for p in split_lines)

def get_masked_repr(mask, number):
    binary_repr = bin(number)[2:]
    binary_repr = "0"*(36-len(binary_repr))+binary_repr
    return [m if m != "X" else n for m, n in zip(mask, binary_repr)]

def get_masked_address(mask, address):
    binary_repr = bin(address)[2:]
    binary_repr = "0"*(36-len(binary_repr))+binary_repr
    stack = [[]]
    for m, a in zip(mask, binary_repr):
        if m == "0":
            for s in stack:
                s.append(a)
        elif m == "1":
            for s in stack:
                s.append("1")
        elif m == "X":
            stack = [s+["0"] for s in stack] + [s + ["1"] for s in stack]
    return stack


def solution_1(lines):
    all_mems = {}
    for mask, kv in parse_input(lines):
        for key, value in kv:
            all_mems[key] = get_masked_repr(mask, value)
    return sum(int("0b"+"".join(bin_repr), 2) for bin_repr in all_mems.values())

def solution_2(lines):
    all_mems = {}
    for mask, kv in parse_input(lines):
        for key, value in kv:
            for address in get_masked_address(mask, key):
                all_mems[int("0b"+"".join(address), 2)] = value
    return sum(all_mems.values())


assert solution_1(test_input) == 165
assert solution_2(test_input2) == 208
print(solution_1(open("input/day14.txt")))
print(solution_2(open("input/day14.txt")))
