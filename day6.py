from more_itertools import split_at

test_input = """\
abc

a
b
c

ab
ac

a
a
a
a

b\
""".split("\n")

def parse_groups(lines):
    return split_at(lines, lambda line: not line.strip())

def get_union(group):
    return {c for line in group for c in line.strip()}

def get_intersection(group):
    return set.intersection(*(set(line.strip()) for line in group))

def solution_1(lines):
    return sum(len(get_union(group)) for group in parse_groups(lines))

def solution_2(lines):
    return sum(len(get_intersection(group)) for group in parse_groups(lines))

assert solution_1(test_input) == 11, solution_1(test_input)
assert solution_2(test_input) == 6, solution_1(test_input)

print(solution_1(open("input/day6.txt")))
print(solution_2(open("input/day6.txt")))
