from itertools import count
from operator import itemgetter

test_input = """\
939
7,13,x,x,59,x,31,19\
""".split("\n")

def parse_input(lines):
    lines = iter(lines)
    earliest_time = int(next(lines))
    buses = [(i, int(p)) for i, p in enumerate(next(lines).split(",")) if p != "x"]
    return earliest_time, buses

def solution_1(lines):
    t, buses = parse_input(lines)
    buses = (b[1] for b in buses)
    wait_time, bus = min((bus-(t % bus), bus) for bus in buses)
    return wait_time*bus

def solution_2(lines):
    _, buses = parse_input(lines)
    cur_value, cur_step = (0, 1)
    for offset, step in buses:
        while (cur_value+offset) % step:
            cur_value += cur_step
        cur_step *= step
    return cur_value


assert solution_1(test_input) == 295
assert solution_2(test_input) == 1068781

examples = [("17,x,13,19",  3417),
            ("67,7,59,61", 754018),
            ("67,x,7,59,61", 779210),
            ("67,7,x,59,61", 1261476),
            ("1789,37,47,1889", 1202161486)]

for example, answer in examples:
    assert solution_2(("0", example)) == answer

print(solution_1(open("input/day13.txt")))
print(solution_2(open("input/day13.txt")))
