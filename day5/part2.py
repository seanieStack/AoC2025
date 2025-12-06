with open("input") as f:
    parts = f.read().split("\n\n")

    ranges = [tuple(map(int, line.split("-"))) for line in parts[0].strip().split("\n")]

ranges = sorted(ranges)
merged = [ranges[0]]
for current in ranges[1:]:
    last = merged[-1]

    if current[0] <= last[1]:
        merged[-1] = (last[0], max(last[1], current[1]))
    else:
        merged.append(current)

count = 0
for r in merged:
    count += r[1] - r[0] + 1

print(count)
