import matplotlib.pyplot as plt
import numpy as np


def stitch_basic(A,B,T):
    """
    stitches two matrix pictures A,B together using the rectilinear transformation T
    """
    # tentatively: DONE
    # convention for T is [x,y] instead of the usual [row,column]
    Aheight,Awidth,_ = A.shape
    Bheight,Bwidth,_ = B.shape

    height = max(T[1]+Bheight,Aheight)
    width = max(T[0]+Bwidth,Awidth)

    R = np.uint8(np.zeros((height,width,3)))  # T(0) is x, T(1) is y
    R[:Aheight,:Awidth,:] = A
    R[T[1]:T[1]+Bheight,T[0]:T[0]+Bwidth,:] = B
    return R # returns

def stitch_transform(A,B,T):
    """
    stitches two matrix pictures A,B together using the transformation matrix T
    """
    Aheight,Awidth,_ = A.shape
    Bheight,Bwidth,_ = B.shape

    height = int(max(T[1][2]+1+Bheight,Aheight)) # +1 because of array subscripting rules
    width = int(max(T[0][2]+1+Bwidth,Awidth))
    print height
    print width

    R = np.uint8(np.zeros((height,width,3)))  # T(0) is x, T(1) is y
    R[:Aheight,:Awidth,:] = A

    for r in range(B.shape[0]): # row --> y
        for c in range(B.shape[1]): # column --> x
            x = np.array([c,r,1])
            newG = np.dot(T,x)
            new_c = int(newG[0])
            new_r = int(newG[1])
            R[new_r][new_c][:] = B[r][c][:] # put the pixels in
    return R

class Picture:
    # class to hold pictures and coordinates together
    def __init__(self,img,coords):
        self.pic = img
        self.cor = coords


def show(A,tag = None):

    plt.imshow(A,interpolation='nearest')
    if tag != None:
        plt.title(str(tag))
    plt.show()


def compare(A,B,cA,cB):
    # image A, image B, coordinates cA and cB
    # compares a 5x5 area around them and computes the norm of the difference between the two vectors.
    ds = 5

    Amini = A[cA[1]-ds:cA[1]+ds,cA[0]-ds:cA[0]+ds,:]
    Bmini = B[cB[1]-ds:cB[1]+ds,cB[0]-ds:cB[0]+ds,:]
    # print Amini-Bmini

    Aavg = np.array([Amini[:,:,i].mean() for i in range(3)])
    Bavg = np.array([Bmini[:,:,i].mean() for i in range(3)])
    print Aavg - Bavg

    show(Amini)
    show(Bmini)
    show(Amini-Bmini)
    return np.linalg.norm(Amini-Bmini)

def leastTrans(a,b,c,a_sol,b_sol,c_sol):
    """
    a,b,c are the [x,y] coordinates of the candidate points in the local frame.
    a_sol, b_sol, c_sol are the coordinates of the candidate points in the world frame.
    x has the form [r11 r12 px r21 r22 py]'

    tentatively: DONE
    """

    sol = []
    sol.extend(a_sol)
    sol.extend(b_sol)
    sol.extend(c_sol)

    P = np.array(sol)
    M = np.array([[a[0],a[1],1,0,0,0],
                  [0,0,0,a[0],a[1],1],
                  [b[0],b[1],1,0,0,0],
                  [0,0,0,b[0],b[1],1],
                  [c[0],c[1],1,0,0,0],
                  [0,0,0,c[0],c[1],1]])

    Mplus = np.linalg.pinv(M)
    xsol = Mplus.dot(P)
    T = np.array([[xsol[0], xsol[1], xsol[2]],
                  [xsol[3], xsol[4], xsol[5]],
                  [0      , 0      , 1     ]])
    T.reshape(3,3)
    return T


