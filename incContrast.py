import cv2

def increase(img):
    #img = cv2.imread('arena.jpeg', 1)
    #cv2.imshow("img",img)
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    cv2.imshow("lab",lab)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2,2))
    cl = clahe.apply(l)
    ca = clahe.apply(a)
    cb = clahe.apply(b)
    limg = cv2.merge((cl,ca,cb))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final
