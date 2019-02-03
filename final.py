import numpy as np
import cv2
import lab_thresh as th
import detectShape as ds
import adjacency as adj
import BFS

if __name__ == "__main__":
    img = cv2.imread('rsz_arena.jpg')
    mat = th.start(img)
    mask = th.roi(img,mat)
    imgMat = ds.detect(mask,"TRIANGLE")
    print(imgMat)
    start = int(24) 
    dest = BFS.bfs(start,imgMat)
    print(dest)
    
    while True:
        node = BFS.parent[dest]
        print(node)
        if node == start:
            break
        dest = node
    
