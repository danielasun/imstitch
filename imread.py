#! /usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
from imfunc import *

# Picture stitching

# read in all the images.
img = []

for i in range(1,21):
    img.append(mpimg.imread("img" + str(i) + ".jpg"))

# read in all the coordinates.
f = open('data.txt')
CoordDict = [{'x':[],'y':[]} for i in range(20)]
# get a single line
for i in range(20): # there's 20 images
    data = list(f.readline()) # every three lines we throw away.

    for dim in ['x','y']:
        data = list(f.readline())
        tmp = []
        for char in data: # for every character in data
            if char == ' ':
                CoordDict[i][dim].append(int(''.join(tmp)))
                tmp = []
                continue
            elif char == '\n':
                CoordDict[i][dim].append(int(''.join(tmp)))
                tmp = []
                break
            else:
                tmp.append(char)

CoordList = [list() for i in range(20)]
for j in range(len(CoordDict)): # which coordinate we're on
    for k in range(len(CoordDict[j]['x'])):
        CoordList[j].append((CoordDict[j]['x'][k], CoordDict[j]['y'][k]))

# combine images and coordinates together into a picture
PicList = [Picture(img[i],CoordList[i]) for i in range(20)]

print PicList[0].cor

# initialize the big list
bigPic = PicList[0]

# small list is initialized
PicList.remove(PicList[0])
assert(len(PicList) == 19)

# Assume there is a unique best candidate picture to match and that all pictures overlap with at least 3 or more points.

# while there are still pictures to match:
while len(PicList) > 0: #TODO: make this while loop end!
    # each other picture calculates its best 3 vectors using the summed norms approach.
    # The sum of the three norms becomes a measure of how well the pictures match with the base picture.
    for p in PicList:
        # calculate the three best vectors
        p.topNorms = []
        p.normToCoord = dict()
        p.normToBigCor = dict()

        for coord in p.cor:
            lowestNorm = sys.maxint
            bestBigCoord = None  # a tuple is in the bigPic that matched best with this coord
            for bigCor in bigPic.cor:
                norm = compare(bigPic,p,bigCor,coord)
                if norm < lowestNorm: # this is the best coordinate right now!
                    lowestNorm = norm
                    bestCoord = bigCor

            p.topNorms.append(lowestNorm)
            p.normToCoord[lowestNorm] = coord
            p.normToBigCor[lowestNorm] = bestBigCoord

            if len(p.topNorms) > 3: # remove the highest one
                key = max(p.topNorms)
                del p.normToCoord[key]
                del p.normToBigCor[key]
                p.topNorms.remove(key)



# The lowest picture wins and gets stitched to the big picture.






# while there's still coordinates to match in the big picture:

    # for each coordinate in the big picture

        # for each other picture in the picList
            lowest = sys.maxint
            coordgroup = []
            # for each coordinate in the picture
                # compare the coordinates
                # if it is the lower than the maximum entry in the 3 coord group, then this coordinate is a candidate for the best match.
                # save its value
                # add the lowest coordinate to the group of matching candidates
                # if the group already has 3 candidates:
                    # replace the largest one with the new one
            # if you get a group of 3
                # find the least squares transform
                # if the determinant of the rotation matrix transform is 1, then it is a viable picture to be added.
                # stitch the picture into the big picture
                # add the small Pictures' coordinates into bigPic's coordinate list
                # delete the small Picture from the PicList




# while the number of points in the






#T = leastTrans([24,23],[24,57],[39,55],[109,147],[109,181],[124,179]) # pulled directly from the points

#big = stitch_transform(img[0],img[1],T)
#show(big,'big')


