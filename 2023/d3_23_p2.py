dat = [list(line) for line in open('d3_23.txt').read().splitlines()]
a = len(dat)
i , s = 0 , 0
while i<a:
    j=0
    while j<a:
        if dat[i][j] == '*': # find the positions of *
            nums_nbrhs = []
            for di in range(i-1, i+2): # find numbers neighbours of * 
                dj = j-1
                while dj < j+2:
                    kplus , kmin = 1 , 0
                    if a>di>=0 and a> dj >=0 and dat[di][dj].isdigit():
                        while dj+kplus< a and dat[di][dj+kplus].isdigit():
                            kplus += 1
                        while dj-kmin>=0 and dat[di][dj-kmin-1].isdigit():
                            kmin +=1
                        num = ''.join(dat[di][dj-kmin:dj+kplus])
                        nums_nbrhs.append(num)
                    dj += kplus 
            if len(nums_nbrhs) == 2: # add the multiple of nums only if they are 2
                s += int(nums_nbrhs[0])*int(nums_nbrhs[1])
        j+=1
    i+=1
print(s)