from math import prod

with open("input") as f:
    lines = f.readlines()

    lines = [line.rstrip('\n') for line in lines]
    operator_line = lines[-1]
    operator_positions = [i for i, char in enumerate(operator_line) if char.strip()]

    eqs = []
    for i, pos in enumerate(operator_positions):
        if i < len(operator_positions) - 1:
            end = operator_positions[i + 1]
        else:
            end = len(lines[0])

        column = tuple(line[pos:end] for line in lines)
        eqs.append(column)

formatted_eqs = []
for eq in eqs:
    x = ["".join(x) for x in list(zip(*eq[:-1]))]
    x = [int(x) for x in x if x.strip()]
    x.append(eq[-1].strip())

    formatted_eqs.append((tuple(x)))

count = 0
for eq in formatted_eqs:
    op = eq[-1]
    if op == "+":
        count += sum(eq[:-1])
    else:
        count += prod(eq[:-1])

print(count)