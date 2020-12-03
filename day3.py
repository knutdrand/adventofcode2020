from itertools import count
from math import prod

test_input = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
""".split("\n")

def read_tree_grid(lines):
    return([[char=="#" for char in line.strip()] for line in lines])

def count_trees(grid, row_step, col_step):
    nrow, ncol = (len(grid), len(grid[0]))
    positions = ((row_step*i, col_step*i % ncol) for i in range(nrow//row_step))
    return sum(grid[i][j] for i, j in positions)

def solution_1(lines):
    grid = read_tree_grid(lines)
    return count_trees(grid, 1, 3)

def solution_2(lines):
    grid = read_tree_grid(lines)
    slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    tree_counts = (count_trees(grid, r, c)
                   for r, c in slopes)
    return prod(tree_counts)
    

assert solution_1(test_input) == 7
print(solution_1(open("input/day3.txt")))
assert solution_2(test_input) == 336
print(solution_2(open("input/day3.txt")))
