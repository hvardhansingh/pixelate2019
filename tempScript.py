import numpy as np
import cv2
import threshold as th
import detectShape as ds
import adjacency as adj
import BFS
import incContrast as con
import bot
from getBot import getBot 
from getImg import getImg
from node2centroid import n2c

#cap = cv2.VideoCapture(0)
#ret,img = cap.read()
#r = cv2.selectROI('img',img,False)

if __name__ == "__main__":

        
    
    
    im = cv2.imread('arena1.jpg')
    r = cv2.selectROI('img',im,False)                 
    img = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    c = n2c(20,img)
    print(c)
    
    
    #mat = th.start(img)

    #botclr1 = th.start(img)
    #botclr2 = th.start(img)

    #p,a = getBot(img,botclr1,botclr2)
    #print(p,a)
    
    #mask = th.roi(img,mat)
    #imgMat = ds.detect(img,mask,"TRIANGLE")
    #print(imgMat)
    #h,s,v = cv2.split(img)
    #ret,thresh1 = cv2.threshold(h,200,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #cv2.imshow('h',h)
    #botx,boty,ang = bot.botpos(img, botclr1, botclr2)

    #print(botx,boty,ang)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    '''
    imgMat = ds.detect(mask,"CIRCLE")         # boolean nxn matrix containing '1' in place of triangles of the selected color, '0' otherwise
    print(imgMat)
    start = int(23)                             # Starting point. During final run, this would be the current position of the bot. 
    dest = BFS.bfs(start,imgMat)                # End point of PATH obtained by BFS
    print(dest)
    
    while True:                                 # Print path. NOTE : The path will be printed in reverse order i.e. first destination then source.
        node = BFS.parent[dest]
        print(node)
        if node == start:
            break
        dest = node

img = cv2.imread('arena.jpeg')
mat1 = start(img)
mat2 = start(img)
mat3 = start(img)
mat4 = start(img)
mat5 = start(img)
mat6 = start(img)
mat7 = start(img)
mat8 = start(img)

mask1 = roi(img,mat1)
mask2 = roi(img,mat2)
mask3 = roi(img,mat3)
mask4 = roi(img,mat4)
mask5 = roi(img,mat5)
mask6 = roi(img,mat6)
mask7 = roi(img,mat7)
mask8 = roi(img,mat8)

mask = cv2.bitwise_or(mask1,mask2)
mask = cv2.bitwise_or(mask,mask3)
mask = cv2.bitwise_or(mask,mask4)
mask = cv2.bitwise_or(mask,mask5)
mask = cv2.bitwise_or(mask,mask6)
mask = cv2.bitwise_or(mask,mask7)
mask = cv2.bitwise_or(mask,mask8)
#mask = cv2.bitwise_xor(mask,mask4)

for i in range(3):
        mat = th.start(img)
        mask1 = th.roi(img,mat)
        mask = cv2.bitwise_or(mask, mask1)
    


'''
