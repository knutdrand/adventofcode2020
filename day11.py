from itertools import chain
test_input="""\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL\
""".split("\n")

def parse_floor(lines):
    floor = [list(line.strip()) for line in lines]
    padded  = [["."]*(len(floor[0])+2)]+ [["."] + row + [0] for row in floor] + [["."]* (len(floor[0])+2)]
    assert all(len(row) == len(padded[0]) for row in padded)
    return padded

directions = list(chain(((-1, k) for k in (-1, 0, 1)),
                        ((1, k) for k in (-1, 0, 1)),
                        ((0, k) for k in (-1, 1))))

def neighbours(i, j, _):
    return ((i+di, j+dj) for di, dj in directions)

def seen_neighbours(i, j, floor):
    for di, dj in directions:
        ni, nj = i+di, j+dj
        while (0 <= ni < len(floor)) and (0 <= nj < len(floor[0])):
            if floor[ni][nj] != ".":
                yield (ni, nj)
                break
            ni += di
            nj += dj
        else:
            yield (i+di, j+dj)

def simulate(floor, neighbour_func=neighbours, threshold=4):
    new_floor = [list(row) for row in floor]
    for i, row in enumerate(floor[1:-1], 1):
        for j, cell in enumerate(row[1:-1], 1):
            occupied_neighbors = sum(floor[k][l]=="#" for k, l in neighbour_func(i, j, floor))
            if cell == "#" and occupied_neighbors >= threshold:
                new_floor[i][j] = "L"
            elif cell == "L" and occupied_neighbors == 0:
                new_floor[i][j] = "#"
    
    return new_floor

def solution_1(lines):
    floor = parse_floor(lines)
    new_floor = simulate(floor)
    while new_floor != floor:
        floor, new_floor = (new_floor, simulate(new_floor))

    return sum(cell=="#" for row in floor for cell in row)

def solution_2(lines):
    floor = parse_floor(lines)
    new_floor = simulate(floor)
    while new_floor != floor:
        floor, new_floor = (new_floor, simulate(new_floor, seen_neighbours, 5))
    return sum(cell=="#" for row in floor for cell in row)

assert solution_1(test_input) == 37
assert solution_2(test_input) == 26
print(solution_1(open("input/day11.txt")))
print(solution_2(open("input/day11.txt")))

