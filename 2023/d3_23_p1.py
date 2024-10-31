dat = [list(line) for line in open('d3_23.txt').read().splitlines()]
a = len(dat)
i , s = 0 , 0
while i<a:
    j=0
    while j<a:
        k=1
        if dat[i][j].isdigit():  
            # find the start and end of the number      
            while j+k<a and dat[i][j+k].isdigit() :
                k+=1
            num= int(''.join(dat[i][j:j+k]))
           
            con =False # break the checking when finding one nghbr for one digit of the number
            # check for neighbours
            for c in range(j,j+k):
                for ni in range(i-1,i+2):
                    for nj in range(c-1, c+2):
                        if a>ni>=0 and a> nj >=0 and not(dat[ni][nj].isdigit() or dat[ni][nj]=='.'):
                            #print(num)
                            s+=num
                            con = True
                            break
                    if con == True: break
                if con == True: break                            
        j+=k
    i+=1
            
print(s)