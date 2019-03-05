import cv2
import numpy as np


def getImg(cap,r):
    ret,frame = cap.read()
    frame = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    return frame

