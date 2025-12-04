with open("input") as f:
    banks = [x.strip() for x in f.readlines()]

count = 0
for bank in banks:
    print(bank)
    max_1 = max(int(c) for c in bank[:-1])
    max_1_index = bank[:-1].index(str(max_1))

    max_2 = max(int(c) for c in bank[max_1_index+1:])

    count += int(str(max_1) + str(max_2))

print(count)