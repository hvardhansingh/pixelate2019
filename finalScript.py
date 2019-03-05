import numpy as np
import cv2
import serial
import threshold as th
import detectShape as ds
import adjacency as adj
import math
import bot

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    _,frame = cap.read()

    r = selectROI(frame)
    red = th.start(frame)
    yellow = th.start(frame)
    botclr1 = th.start(frame)
    botclr2 = th.start(frame)

    print("Usind the following table, input your choice :")
    print("    Red Triangle =>  'r t' ")
    print("    Yellow Triangle =>  'y t' ")
    print("    Red Square =>  'r s' ")
    print("    Yellow Square =>  'y s' ")
    print("    Red Circle =>  'r c' ")
    print("    Yellow Circle =>  'y c' ")

    color = dict({"r":red, "y":yellow})
    shape = dict({"s":"SQUARE", "t":"TRIANGLE", "c":"CIRCLE", "S":"SQUARE", "T":"TRIANGLE", "C":"CIRCLE" })
    while True:
        _,frame = cap.read()
        img = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        clr = str(input("What appeared on dice ? \n"))
        sh = str(input())
        mask = th.roi(img,color[clr])
        shapeMat = ds.detect(mask,shape[sh])

        botposx,botposy,ang = bot.botpos(img, botclr1, botclr2)
        
        

        
