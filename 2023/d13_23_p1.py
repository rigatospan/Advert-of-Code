def mirror(matrix: list[list]):
    
    res = 0 
    is_valid_refl = False

    # find vertical reflection
    for i, row in enumerate(matrix[:-1]):
        if row == matrix[i+1]:
            # check if it is a perfectreflaction
            k = 0
            is_valid_refl = True
            while i-k>=0 and i+1+k<len(matrix):
                if matrix[i-k] != matrix[i+1+k]:
                    is_valid_refl = False
                    break
                k+=1

            if is_valid_refl:
                res += i+1
                return i+1
    
    return res

b = [str(a).splitlines() for a in open('d13_23.txt').read().split('\n\n')]

result = 0 
for block in b:

    block_trans = [''.join(list(a)) for a in zip(*block)]

    rows = mirror(block)
    cols = mirror(block_trans)
    result += cols+100*rows

print(f'result is {result}')