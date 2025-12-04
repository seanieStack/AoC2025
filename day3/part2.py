with open("input") as f:
    banks = [x.strip() for x in f.readlines()]

count = 0
for bank in banks:
    #keep 12 digits
    to_remove = len(bank) - 12
    stack = []

    #loop over every digit
    for d in bank:
        #if we can still remove a digit and the current digit is larger than what's on top of the stack, remove from stack
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1

        #add current digit to stack
        stack.append(d)

    #take the first 12 digits on the stack
    if to_remove > 0:
        stack = stack[:-to_remove]

    #convert stack to int and add to count
    count += int(''.join(stack[:12]))

print(count)