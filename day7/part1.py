from utils.utils import load_map, print_map

puzzle_map = load_map("test")

width = max(key[0] for key in puzzle_map.keys())
height = max(key[1] for key in puzzle_map.keys())

current_positions = set()
current_level = 0
for i in range(width):
    if puzzle_map[(0, i)] == "S":
        starting_pos = i

current_positions.add(starting_pos)

split_count =0
while current_level <= height + 1:
    next_positions = set()

    for position in current_positions:
        if puzzle_map[(current_level+1, position)] == "^":
            split_count += 1
            next_positions.add(position-1)
            next_positions.add(position+1)
        else:
            next_positions.add(position)

        puzzle_map[(current_level, position)] = "|"

    current_positions = next_positions
    current_level += 1

print_map(puzzle_map)

print(split_count)