from utils.utils import load_map, print_map

puzzle_map = load_map()

def get_surrounding_paper(cord):
    paper_count = 0

    neighbors = [
        (cord[0] - 1, cord[1]),  # left
        (cord[0] + 1, cord[1]),  # right
        (cord[0], cord[1] - 1),  # up
        (cord[0], cord[1] + 1),  # down
        (cord[0] - 1, cord[1] - 1),  # top-left
        (cord[0] + 1, cord[1] - 1),  # top-right
        (cord[0] - 1, cord[1] + 1),  # bottom-left
        (cord[0] + 1, cord[1] + 1),  # bottom-right
    ]

    for n in neighbors:
        if puzzle_map[n] == "@":
            paper_count += 1

    return paper_count < 4

removed = 0
can_be_removed = True
while can_be_removed:
    count = 0
    to_remove = []
    for cord, _ in list(puzzle_map.items()):
        if puzzle_map[cord] == "@" and get_surrounding_paper(cord):
            count += 1
            to_remove.append(cord)

    for cord in to_remove:
        puzzle_map[cord] = "."

    if count == 0:
        can_be_removed = False

    removed += count

print_map(puzzle_map)
print(removed)
