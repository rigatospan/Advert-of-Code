races = [(51926890,222203111261225)]
p=1
for t,d in races:
    w=0
    for time_hold in range(t+1):
        dis = (t-time_hold)*time_hold
        if dis > d:
            w+=1
    p*=w
print(p)