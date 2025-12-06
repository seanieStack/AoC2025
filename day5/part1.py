with open("input") as f:
    parts = f.read().split("\n\n")

    ranges = [tuple(map(int, line.split("-"))) for line in parts[0].strip().split("\n")]
    ids = [int(x.strip()) for x in parts[1].split("\n")]


count = 0
valid_ids = set()
for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            count += 1
            break

print(count)