import numpy as np
import queue
import adjacency as ad

adjMat = ad.adj
vis = np.zeros(82) 
parent = np.zeros(82,int)

n = int(9)

def bfs(node,imgMat):
    q = queue.Queue(82)
    vis[node]=1
    q.put(node)
    while q.empty()==0:
        front = q.get()

        r = int(front/n)            # find the position in grid for the corresponding node
        c = int(front%n)
        c = c-1
        if c==-1:
            r = r-1
            c=n-1
        if(imgMat[r][c]==1):        # if shape found, break out of this loop i.e. PATH FOUND !! 
            dest = front            
            break

        for i in range(1,82):
            if adjMat[front,i]==1:
                if vis[i]==0:
                    vis[i]=1
                    q.put(i)
                    parent[i]=front # store parent of current node

    return dest                     # return destination i.e. end point of the path
