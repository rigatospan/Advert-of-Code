dat = open('d2_23.txt').read().splitlines()
d_limit = {'blue':14, 'red': 12, 'green':13}  
s= 0

for i, line in enumerate(dat):
    game = [[cube.strip().split() for cube in g.strip().split(',')] for g in line.split(':')[1].split(';')]
    for g in game:
        d = {c[1]:int(c[0]) for c in g}
        val = [d[cube]<= d_limit[cube] for cube in d.keys()]
        validity_game = True
        if False in val:
            validity_game = False
            break
    if validity_game == True: 
        s+=i +1
        
print(s)