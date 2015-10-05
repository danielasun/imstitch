f = open('data.txt')

coord = []

# get a single line
for i in range(60):
    data = list(f.readline())
    if i % 3 == 0:
        continue
    tmp = []

    for char in data: # for every character in data
        if char == ' ':
            continue
        elif char == '\n':
            int(str(tmp))
            coord.extend(tmp)
            tmp = []
            continue
        else
            


print coord