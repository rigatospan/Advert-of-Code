dat = [[int(a) for a in line.split(' ')] for line in open('d9_23.txt').read().splitlines()]
s=0
for line in dat:
    first_n = []
    while line != [0]*len(line) :
        first_n.append(line[0])
        line = [ line[i+1] - line[i] for i in range(len(line)-1)]
    dif = 0 
    for n in reversed(first_n):
        ext_n = n - dif
        dif = ext_n
    s+=ext_n
print(s)