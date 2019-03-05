import numpy as np
import cv2
from getImg import getImg
from distance import distance
import Video

def goto(endpoint,cap,r):
    step = 0.5
    errp = 50
    erra = 5

    while True:
        img = getImg(cap,r)
        p,a = getBot(img,botclr1,botclr2)
        d = distance(p,endpoint)

        if d<errp:
            break
        allign(endpoint)
        stepforward(step)

    

