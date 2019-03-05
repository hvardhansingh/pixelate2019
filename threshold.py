import numpy as np
import cv2
t = 25           #  correction term for min and max values

'''
mat is a 3x2 matrix containing min and max RGB values for thresholding.
'''
def start(crop_img):        
    mat = np.zeros([3,2])   
    lab = crop_img #cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    r = cv2.selectROI('img',crop_img,False)                 
    imCrop = lab[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    
    for i in range(3):                      #extract min and max values from roi
        mat[i][0] = imCrop[:,:,i].min()-t
        mat[i][1] = imCrop[:,:,i].max()+t
    mat = np.transpose(mat)
    return mat
'''
<< THRESHOLDING >>
'''
def roi(crop_img,mat):
    lab = crop_img                          #cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(lab,mat[0],mat[1])
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4,4))
    dilation = cv2.dilate(mask, kernel, iterations = 1)  
    mask = cv2.erode(dilation, kernel, iterations = 4)
    return mask



