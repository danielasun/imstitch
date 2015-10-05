f = open('data.txt')

coordlist = [{'x':[],'y':[]} for i in range(20)]

# get a single line
for i in range(20): # there's 20 images
    data = list(f.readline()) # every three lines we throw away.

    for dim in ['x','y']:
        data = list(f.readline())
        tmp = []
        for char in data: # for every character in data
            if char == ' ':
                coordlist[i][dim].append(int(''.join(tmp)))
                tmp = []
                continue
            elif char == '\n':
                coordlist[i][dim].append(int(''.join(tmp)))
                tmp = []
                break
            else:
                tmp.append(char)

print len(coordlist)
coords = [list() for i in range(20)]
for j in range(len(coordlist)): # which coordinate we're on
    for k in range(len(coordlist[j]['x'])):
        coords[j].append((coordlist[j]['x'][k], coordlist[j]['y'][k]))

print coords[3]