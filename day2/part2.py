#open file
with open("input") as f:
    #parse ranges into array of tuples "1-2,45-50" -> [("1","2"), ("45","50")]
    id_ranges = [(y[0], y[1]) for y in (x.split("-") for x in f.read().strip().split(","))]

count = 0

#loop over all ranges
for id_range in id_ranges:
    #loop over every number in ranges
    for i in range(int(id_range[0]), int(id_range[1]) + 1):
        str_i = str(i) #convert number to str

        #loop over every size of pointer 123456 -> 1, 2, 3
        for j in range(1, (len(str_i)//2) + 1):
            # convert number into an array of all pointer size and compares if every element is equal["1", "2", "3", "4", "5", "6"] ["12", "34", "56"] ["123", "456"]
            if len(set(list(map(''.join, zip(*[iter(str_i)]*j))))) == 1 and len(str_i) % j == 0:
                count += i #if equal add id to count
                break

print(count)