import numpy as np
import cv2
import lab_thresh as thresholding

#img = cv2.imread('rsz_arena.jpg')

n=int(5)                        # no of grids 


#print(row," ",col)
             # height of one row             
             # width of one column

def detect(img,mask,shape):

    '''
    This function will return an nxn matrix containing '1' for shape of selected color, '0' otherwise.
    '''
    row,col = mask.shape
    divRow = int(row/n)
    divCol = int(col/n)

    imgMat = np.zeros([n,n])    
    _, contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i=1
    for cnt in contours:
        #print(cv2.contourArea(cnt))
        approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt, True), True)     # approximating the contours found 
        M = cv2.moments(cnt)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
        cv2.putText(img,str(i),(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 0, 0),2)
        i=i+1;
        if len(approx)==3 and shape=="TRIANGLE":
            print("TRIANGLE : ",cX," ",cY)
            r = int(cY/divRow)                          # to find position of the particular shape in nxn grid
            c = int(cX/divCol)
            imgMat[r,c]=1
            
        elif len(approx)==4 and shape=="SQUARE":
            print("SQUARE : ",cX," ",cY)
            r = int(cY/divRow)
            c = int(cX/divCol)
            imgMat[r,c]=1
        elif len(approx)>4 and shape=="CIRCLE":
            print("CIRCLE : ",cX," ",cY)
            r = int(cY/divRow)
            c = int(cX/divCol)
            imgMat[r,c]=1
    cv2.imshow('contours', img)
    return imgMat












