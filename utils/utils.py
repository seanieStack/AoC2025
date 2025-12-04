from collections import defaultdict

def print_map(puzzle_map):
    max_row = max(key[0] for key in puzzle_map.keys())
    max_col = max(key[1] for key in puzzle_map.keys())

    for i in range(max_row + 1):
        row = ""
        for j in range(max_col + 1):
            pos = (i, j)
            char = puzzle_map[pos]
            row += char
        print(row)
    print("\n")

def load_map():
    puzzle_map = defaultdict(lambda: "?")
    with open("input") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(list(line.strip())):
                puzzle_map[(i, j)] = char

    return puzzle_map