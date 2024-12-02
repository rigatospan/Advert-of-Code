file = 'd02_24.txt'
data = [list(map(int,line.split())) for line in open(file).read().splitlines()]

safe = 0
for line in data:
    is_safe = True

    sing = line[1] - line[0]

    for a, b in zip(line[:-1], line[1:]):
        n = abs(a-b)
        if n<1 or n>3 or sing*(b-a) < 0 :
            is_safe = False
            break

    if is_safe:
        safe+=1

print(safe)