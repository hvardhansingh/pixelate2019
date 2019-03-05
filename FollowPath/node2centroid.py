import math
import numpy as np

n=5

def n2c(node,img):
    row,col,_ = img.shape
    print(row," ",col)
    dr = row/n
    dc = col/n
    r = int(node/n)            
    c = int(node%n)
    c = c-1
    if c==-1:
        r = r-1
        c = n-1

    print(r," ",c)
    
    cx = dc*c+(dc/2)
    cy = dr*r+(dr/2)

    c = np.array([cx,cy])

    return c
