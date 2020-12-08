test_input = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6\
""".split("\n")
def run_code(codes):
    accumulator = 0
    position = 0
    visited = {len(codes)}
    while True:
        visited.add(position)
        operation, n = codes[position]
        assert operation in {"acc", "jmp", "nop"}, code
        if operation == "acc":
            accumulator += n
            position += 1
        elif operation == "jmp":
            position += n
        else:
            position += 1
        if position in visited:
            return accumulator

def parse_codes(lines):
    parts = (line.strip().split() for line in lines)
    return [(operation, int(n)) for operation, n in parts]


def create_graph(codes):
    adj_list = defaultdict(list)
    reverse_adj_list = defaultdict(list)
    for position, (operation, n) in enumerate(codes):
        if operation in ("acc", "nop"):
            n = 1
        adj_list[position].append(position+n)
        reverse_adj_list[position+n].append(position)
    return adj_list, reverse_adj_list

def get_visited(adj_list, start_position):
    stack = [start_position]
    visited = set()
    while stack:
        position = stack.pop()
        if position not in visited:
            visited.add(position)
            stack.extend(adj_list[position])
    return visited

def solution_2(lines):
    codes = parse_codes(lines)
    adj_list, rev_adj_lsit = create_graph(codes)
    forward_visited = get_visited(adj_list, 0)
    reverse_visited = get_visited(rev_adj_lsit, len(codes))
    for position in forward_visited:
        operation, n = codes[position]
        if operation == "jmp" and position + 1 in reverse_visited:
            codes[position] = ("nop", n)
            break
        if operation == "nop" and position + n in reverse_visited:
            codes[position] = ("jmp", n)
            break
    return run_code(codes)
        
def solution_1(lines):
    return run_code(parse_codes(lines))

assert solution_1(test_input) == 5
print(solution_1(open("input/day8.txt")))
assert solution_2(test_input) == 8
print(solution_2(open("input/day8.txt")))
