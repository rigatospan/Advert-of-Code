data_file = 'd01_24.txt'
data = [line.split() for line in open(data_file).read().splitlines()]

l = []
m = []
for (a, b) in data:
    l.append(int(a))
    m.append(int(b))

l.sort()
m.sort()

res = sum( [abs(a-b) for a, b in zip(l, m)] )

print(f'result is {res}')