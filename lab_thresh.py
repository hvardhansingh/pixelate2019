import numpy as np
import cv2
t = 20
#mat = np.zeros([3,2])

def start(crop_img):
    #global mat
    mat = np.zeros([3,2])
    lab = cv2.cvtColor(crop_img, cv2.COLOR_BGR2LAB)
    r = cv2.selectROI('img',crop_img,False)
    imCrop = lab[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    
    for i in range(3):
        mat[i][0] = imCrop[:,:,i].min()-t
        mat[i][1] = imCrop[:,:,i].max()+t
    mat = np.transpose(mat)
    return mat

def roi(crop_img,mat):
    lab = cv2.cvtColor(crop_img, cv2.COLOR_BGR2LAB)
    mask = cv2.inRange(lab,mat[0],mat[1])
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    mask = cv2.erode(dilation, kernel, iterations = 1)
    return mask
'''
img = cv2.imread('pcrop.jpg')
start(img)
thresh = roi(img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''