grid = [list(line) for line in zip(*open('d14_23.txt').read().splitlines())]
grid_north=[]
for col in grid:
    new_col = []
    i = 0
    while i<len(col):
        if col[i]!= '.':
            new_col.append(col[i])
            i+=1
        else:
            j=0
            while i+j< len(col) and col[i+j]!= '#':
                j+=1
            n_O = col[i:i+j].count('O')
            new_col=new_col+['O']*n_O+['.']*(j-n_O)
            i+=j
    grid_north.append(new_col)
    
s = sum([len(col)-i  for col in grid_north for i,a in enumerate(col)  if a=='O'])
print(s)