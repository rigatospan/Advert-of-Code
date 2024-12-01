data_file = 'd01_24.txt'
data = [line.split() for line in open(data_file).read().splitlines()]

l1 = []
l2 = []
res = 0
for (a, b) in data:
    l1.append(int(a))
    l2.append(int(b))

for a in l1:
    res += a*l2.count(a)


print(f'result is {res}')