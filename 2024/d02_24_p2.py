def check(line):
    ''' return true is the line is safe, false otherwise
    '''
    if len(line)<=1:
        return True
    
    # find if the line is ascending or descending
    sing = line[1] - line[0]

    for a, b in zip(line[:-1], line[1:]):
        n = abs(a-b)
        if n<1 or n>3 or sing*(b-a) < 0 :
            return False
    
    return True

file = 'd02_24.txt'
data = [list(map(int,line.split())) for line in open(file).read().splitlines()]

res = 0

for line in data:
    
    # check if the line is safe
    if check(line):
        res+=1
        continue
    
    # find if the line is ascending or descending even if it has a false number
    diff = [b-a>0 for a, b in zip(line[:5], line[1:6])]

    s = 1 if diff.count(True) > diff.count(False) else -1

    for i, (a, b) in enumerate(zip(line[:-1], line[1:])):
        n = abs(a-b)
        if n<1 or n>3 or s*(b-a) < 0 :
            if check(line[:i+1]+line[i+2:]) or check(line[:i]+line[i+1:]):
                res +=1
            break

print(res)