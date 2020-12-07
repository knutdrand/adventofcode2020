from collections import defaultdict

from more_itertools import chunked

test_input = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.\
""".split("\n")

test_input_2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.\
""".split("\n")

def parse_rule_line(line):
    parts = line.strip().split()
    color = tuple(parts[:2])
    contained = [(int(t[0]), (t[1], t[2])) for t in chunked(parts[4:], 4)] if parts[4] != "no" else []
    return color, contained

def parse_rule_file(lines):
    graph = defaultdict(list)
    for (color, contained) in (parse_rule_line(line) for line in lines):
        for n, contained_color in contained:
            graph[contained_color].append(color)
    return graph

def parse_rule_file_2(lines):
    return dict(parse_rule_line(line) for line in lines)

def solution_1(lines):
    valid = set()
    stack = [("shiny", "gold")]
    graph = parse_rule_file(lines)
    while stack:
        color = stack.pop()
        valid.add(color)
        stack.extend(graph[color])
    return len(valid)-1

def solution_2(lines):
    graph = parse_rule_file_2(lines)
    memo = {}
    def rec(color):
        if color not in memo:
            memo[color] = 1 + sum(n*rec(c) for n, c in graph[color])
        return memo[color]
    return rec(("shiny", "gold"))-1

assert solution_1(test_input) == 4, solution_1(test_input)
assert solution_2(test_input) == 32, solution_2(test_input)
assert solution_2(test_input_2) == 126, solution_2(test_input_2)
print(solution_1(open("input/day7.txt")))
print(solution_2(open("input/day7.txt")))
