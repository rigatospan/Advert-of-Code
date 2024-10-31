dat = [[num.strip().split() for num in line.split(':')[1].split('|')] for line in open('d4_23.txt').read().splitlines()]
ss=0
for card in dat:
    s=0
    for n in card[1]:
        if n in card[0]:
            if s==0:
                s=1
            else:
                s*=2
    ss+=s
print(ss)