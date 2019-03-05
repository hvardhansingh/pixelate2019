from node2centroid import n2c

def followPath(path,cap,r,botclr1,botclr2):
    
    for p in path:
        c = n2c(p)
        goto(c,cap,r,botclr1,botclr2)
        
