grid = [list(line) for line in open('d14_23.txt').read().splitlines()]

def move(grid):
    grid_left=[]
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
        grid_left.append(new_col)
    return grid_left

def cycle(grid):
    grid_n = [list(a) for a in zip(*grid)]
    g_n_move = move(grid_n)    
    g_w = [list(line) for line in zip(*g_n_move)]
    g_w_move = move(g_w)
    g_s = [list(reversed(list(line))) for line in zip(*g_w_move)]
    g_s_move = [list(a) for a in zip(*[list(reversed(line)) for line in move(g_s)])]
    g_e = [list(reversed(line)) for line in g_s_move]
    g_e_move = [list(reversed(line)) for line in move(g_e)]
    
    return g_e_move

c = 1000000000
cycles = []
for i in range(c):
    grid = cycle(grid)
    if grid in cycles:
        i1 = cycles.index(grid)
        break
    cycles.append(grid)

final_pos = i1+(c-i1-1)%(i-i1)
final_grid = cycles[final_pos]
s = sum([len(final_grid)-i  for i,line in enumerate(final_grid) for a in line  if a=='O'])
print(s)