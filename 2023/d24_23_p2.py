dat = [ [tuple(map(int,a.split(','))) for a in line.split('@')] for line in open('d24_23.txt').read().splitlines()]
print(dat[:3])
