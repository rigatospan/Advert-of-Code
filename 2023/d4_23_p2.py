dat = [[num.strip().split() for num in line.split(':')[1].split('|')] for line in open('d4_23.txt').read().splitlines()]
d= {i+1: 1 for i in range(len(dat))}
for i,card in enumerate(dat):
    s = sum([1 for n in card[1] if n in card[0]])
    for n in range(d[i+1]):
        for j in range(1,s+1):
            d[i+j+1]+=1
print( sum(d.values()))