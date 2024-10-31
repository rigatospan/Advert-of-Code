dat = open('d2_23.txt').read().splitlines()
s= 0

for i, line in enumerate(dat):
    game = [[cube.strip().split() for cube in g.strip().split(',')] for g in line.split(':')[1].split(';')]
    d = {'red': [], 'blue': [], 'green': [] }
    for g in game:
        for cube in g:
            d[cube[1]].append(int(cube[0]))
    min_cubes = list(map(max, d.values()))
    p=1
    for e in min_cubes: p*=e
    s+=p
    
print(s)