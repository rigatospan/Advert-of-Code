dat = [[int(a) for a in line.split(' ')] for line in open('d9_23.txt').read().splitlines()]
s=0
for line in dat:
    last_n = []
    while line != [0]*len(line) :
        last_n.append(line[-1])
        line = [ line[i+1] - line[i] for i in range(len(line)-1)]
    dif = 0 
    for n in reversed(last_n):
        ext_n = n +dif
        dif = ext_n
    s+=ext_n
print(s)