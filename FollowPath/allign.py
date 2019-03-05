import numpy as np
import cv2
from getImg import getImg
import math

def getangle(pt1,pt2):
    c1 = complex(pt1[0],pt1[1])
    c2 = complex(pt2[0],pt2[1])

    a = np.angle(c1/c2)
    a = (a*180)/3.14

    return a
    

def allign(endpoint,cap,r):

    err=1
    while True:
        img = getImg(cap,r)
        p,botVector = getBot(img)
        destVector = (endpoint-p)

        phi = getangle(destVector, botVector)

        if abs(phi)<err:
            break;

        turn(phi)
    
    
    
