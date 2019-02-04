import numpy as np
import cv2
import lab_thresh as th
import detectShape as ds
import adjacency as adj
import BFS

if __name__ == "__main__":

    img = cv2.imread('rsz_arena.jpg')
    mat = th.start(img)                         # mat containing min and max LAB values for thresholding
    mask = th.roi(img,mat)                      
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
    
