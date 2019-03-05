import numpy as np
import cv2
import threshold as th

def getBot(img,botclr1,botclr2):
        

    img1 = th.roi(img,botclr1)
    img2 = th.roi(img,botclr2)

    c1x=0.0
    c1y=0.0
    c2x=0.0
    c2y=0.0
    
    _, contours, _ = cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>200:
            M = cv2.moments(cnt)
            c1x = (M["m10"]/M["m00"])
            c1y = (M["m01"]/M["m00"])

    _, contours, _ = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>200:
            M = cv2.moments(cnt)
            c2x = (M["m10"]/M["m00"])
            c2y = (M["m01"]/M["m00"])

    c1 = np.array([c1x,c1y])
    c2 = np.array([c2x,c2y])

    p = (c1+c2)/2
    a = (c1-c2)

    return [p,a]
