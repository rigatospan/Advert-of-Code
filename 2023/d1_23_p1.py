file = '2023/d1_23.txt'
dat = open(file).read().splitlines()
num = []
for line in dat:
    l = [c for c in line if c.isdigit()]
    num.append(int(l[0]+l[-1]))
print(sum(num))