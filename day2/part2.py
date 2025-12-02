with open("input") as f:
    id_ranges = [(y[0], y[1]) for y in (x.split("-") for x in f.read().strip().split(","))]

count = 0
for id_range in id_ranges:
    for i in range(int(id_range[0]), int(id_range[1]) + 1):
        str_i = str(i)
        for j in range(1, (len(str_i)//2) + 1):
            if len(set(list(map(''.join, zip(*[iter(str_i)]*j))))) == 1 and len(str_i) % j == 0:
                count += i
                break

print(count)