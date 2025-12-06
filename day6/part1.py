from math import prod

with open("input") as f:
    lines = f.readlines()

    eqs = [tuple(int(v) if i < len(lines)-1 else v for i, v in enumerate(t)) for t in zip(*[y.split() for y in (" ".join(line.split()) for line in lines)])]

print(eqs)
count = 0
for eq in eqs:
    op = eq[-1]
    if op == "+":
        count += sum(eq[:-1])
    else:
        count += prod(eq[:-1])

print(count)