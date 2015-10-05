#! /usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from imfunc import *

# Picture stitching

# read in all the images.
img = []

for i in range(1,21):
    img.append(mpimg.imread("img" + str(i) + ".jpg"))

f = open('data-comma.csv')

#print "point 19, good comparison = " + str(compare(img[0],img[1],[107,147],[24,23]))
#print "point 50, bad comparison = " + str(compare(img[0],img[1],[109,181],[24,23]))
#print "point 50, good comparison = " + str(compare(img[0],img[1],[109,181],[24,57]))

T = leastTrans([24,23],[24,57],[39,55],[109,147],[109,181],[124,179]) # pulled directly from the points
print T

big = stitch_transform(img[0],img[1],T)
show(big,'big')


