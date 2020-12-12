test_input = """\
F10
N3
F7
R90
F11\
""".split("\n")


def parse_intstructions(lines):
    return ((line[0], int(line[1:])) for line in lines)

#xy
directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
angles = {0: "E", 90: "S", 180: "W", 270: "N"} #Clockwise
angle_updates = {"R": lambda angle, d_angle:  (angle+d_angle) % 360,
                 "L": lambda angle, d_angle:  (angle-d_angle) % 360}

def solution_1(lines):
    instructions = parse_intstructions(lines)
    cur_pos = (0, 0)
    cur_angle = 0
    for char, n in instructions:
        if char in angle_updates:
            cur_angle = angle_updates[char](cur_angle, n)
            continue
        if char in directions:
            direction = directions[char]
        else:
            assert char == "F"
            direction = directions[angles[cur_angle]]
        cur_pos = (cur_pos[0] + direction[0]*n,
                   cur_pos[1] + direction[1]*n)
    return abs(cur_pos[0]) + abs(cur_pos[1])


rotations = {
    0: lambda pos: pos,
    90: lambda pos: (-pos[1], pos[0]),
    180: lambda pos: (-pos[0], -pos[1]),
    270: lambda pos: (pos[1], -pos[0])}
             

def solution_2(lines):
    instructions = parse_intstructions(lines)
    cur_pos = (0, 0)
    cur_waypoint = (10, 1)
    for char, n in instructions:
        if char == "F":
            cur_pos = (cur_pos[0] + cur_waypoint[0]*n,
                       cur_pos[1] + cur_waypoint[1]*n)
        elif char in directions:
            direction = directions[char]
            cur_waypoint = (cur_waypoint[0] + direction[0]*n,
                            cur_waypoint[1] + direction[1]*n)
        else:
            angle_dir = 1 if char == "L" else -1
            cur_waypoint = rotations[(angle_dir*n) % 360](cur_waypoint)
    return abs(cur_pos[0]) + abs(cur_pos[1])
    


assert solution_1(test_input) == 25
assert solution_2(test_input) == 286

print(solution_1(open("input/day12.txt")))
print(solution_2(open("input/day12.txt")))
