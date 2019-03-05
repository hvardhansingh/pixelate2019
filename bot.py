import cv2
import math
import threshold as th
import numpy as np

def botpos(img,botclr1,botclr2):
    
    bot1 = th.roi(img,botclr1)
    bot2 = th.roi(img,botclr2)
    _, c1, _ = cv2.findContours(bot1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    _, c2, _ = cv2.findContours(bot2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    b1x = 0.0
    b1y = 0.0
    b2x = 0.0
    b2y = 0.0
        
    for c in c1:
        area = cv2.contourArea(c)
        if area>600:
            M = cv2.moments(c)
            b1x = int(M["m10"]/M["m00"])
            b1y = int(M["m01"]/M["m00"])
            break
    for c in c2:
        area = cv2.contourArea(c)
        if area>600:
            M = cv2.moments(c)
            b2x = int(M["m10"]/M["m00"])
            b2y = int(M["m01"]/M["m00"])
            break
    print(b1x," ",b1y," ",b2x," ",b2y)
    botposx = (b1x+b2x)/2
    botposy = (b1y+b2y)/2
        
    ang = math.atan((b2y-b1y)/(b2x-b1x))

    return [botposx,botposy,ang]
