def common_point(x1,y1,vx1, vy1, x2 , y2 , vx2, vy2):
    if vy1*vx2 - vx1* vy2 == 0:
        return None
    else:
        yc = (vy1*vy2*x1 - vy1*vy2*x2 - vx1*vy2*y1 + vx2*vy1*y2)/(vx2*vy1 - vx1*vy2)
        xc = (vx2*vy1*x1 - vx1*vy2*x2 - vx1*vx2*y1 + vx1*vx2*y2)/(vx2*vy1 - vx1*vy2)
        if (xc-x1)*vx1< 0 or (xc-x2)*vx2<0:
            return None
        
        return xc,yc 
    
dat = [ [tuple(map(int,a.split(',')[:-1])) for a in line.split('@')] for line in open('d24_23.txt').read().splitlines()]
s , f= 200000000000000 , 400000000000000
total=0

for i,p1 in enumerate(dat):
    x1 , y1  = p1[0]
    vx1, vy1 = p1[1]
    for p2 in dat[i+1:]:
        x2 , y2 = p2[0]
        vx2, vy2 = p2[1]
        cm = common_point(x1,y1,vx1, vy1, x2 , y2 , vx2, vy2)
        if cm == None:
            continue
        elif s<= cm[0] <= f and s<= cm[1] <=f:
            total+=1
    
print(total)