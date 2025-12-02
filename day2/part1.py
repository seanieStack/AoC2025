with open("input") as f:
    id_ranges = [(y[0], y[1]) for y in (x.split("-") for x in f.read().strip().split(","))]

count = 0
for id_range in id_ranges:
    for i in range(int(id_range[0]), int(id_range[1]) + 1):
        str_i = str(i)
        if str_i[:len(str_i)//2 + len(str_i)%2] == str_i[len(str_i)//2 + len(str_i)%2:]:
            count += i


print(count)
