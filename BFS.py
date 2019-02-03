import numpy as np
import queue
import adjacency as ad

adjMat = ad.adj
vis = np.zeros(82) 
parent = np.zeros(82,int)
#parent = stack.Stack(82)
n = int(9)

def bfs(node,imgMat):
    q = queue.Queue(82)
    vis[node]=1
    q.put(node)
    while q.empty()==0:
        front = q.get()
        #print(front)
        r = int(front/n)
        c = int(front%n)
        c = c-1
        #print(r," ",c)
        if c==-1:
            r = r-1
            c=n-1
        if(imgMat[r][c]==1):
            dest = front
            break
        for i in range(1,82):
            if adjMat[front,i]==1:
                if vis[i]==0:
                    #print(i)
                    vis[i]=1
                    q.put(i)
                    parent[i]=front
    return dest
