grid = [list(line) for line in open('d11_23.txt').read().splitlines()]
rows= [i for i,l in enumerate(grid) if l.count('.') == len(l)]
columns = [j for j, l in enumerate(list(zip(*grid))) if l.count('.') == len(l)]
galaxies = [(i,j) for i,l in enumerate(grid) for j, a in enumerate(l) if a == '#']
s, i= 0 , 0 
for i, g1 in enumerate(galaxies[i:-1]):
    for g2 in galaxies[i+1:]:
        i1 , i2, j1, j2 = min(g1[0],g2[0]) , max(g1[0],g2[0]) , min(g1[1],g2[1]) , max(g1[1],g2[1]) 
        d_i , d_j = i2-i1 , j2 - j1 
        extra_d_i=sum([1 for row in rows if i1 < row <  i2])
        extra_d_j=sum([1 for column in columns if j1 < column <  j2])
        s+=d_i+d_j+extra_d_i+extra_d_j
print(s)