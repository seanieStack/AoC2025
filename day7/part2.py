from collections import defaultdict
from utils.utils import load_map, print_map

puzzle_map = load_map("input")

width  = max(key[0] for key in puzzle_map.keys())
height = max(key[1] for key in puzzle_map.keys())

current_positions = defaultdict(int)
current_level = 0
for i in range(width):
    if puzzle_map[(0, i)] == "S":
        starting_pos = i
        break

current_positions[starting_pos] = 1

while current_level <= height:
    next_positions = defaultdict(int)

    for position, count in current_positions.items():

        if puzzle_map[(current_level + 1, position)] == "^":
            next_positions[position - 1] += count
            next_positions[position + 1] += count
        else:
            next_positions[position] += count

        puzzle_map[(current_level, position)] = "|"

    current_positions = next_positions
    current_level += 1

print_map(puzzle_map)

print(sum(current_positions.values()))
