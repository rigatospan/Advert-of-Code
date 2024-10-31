def mirror(matrix: list[list]):

    for i, row in enumerate(matrix[:-1]):
         
        is_valid_refl = False

        # find consecutive rows that have only one symbol different 
        if len(matrix[i]) - sum( [matrix[i][j] == matrix[i+1][j] for j in range(len(matrix[i])) ] ) == 1:

            # check if it is a perfectreflaction
            k = 1
            is_valid_refl = True
            while i-k>=0 and i+1+k<len(matrix):
                if matrix[i-k] != matrix[i+1+k]:
                    is_valid_refl = False
                    break
                k+=1

            if is_valid_refl:

                return i+1

        if row == matrix[i+1]:
            # check if it is a perfect reflaction
            k = 0
            smudge = 0
            while i-k>=0 and i+1+k<len(matrix):
                
                differencies = len(matrix[i]) - sum( [matrix[i-k][j] == matrix[i+k+1][j] for j in range(len(matrix[i])) ] )
                if differencies == 1: 
                    smudge += 1
                
                if differencies > 1:
                    smudge = 2
                    break

                k+=1

            if smudge == 1:
                return i+1
    
    return 0

b = [str(a).splitlines() for a in open('d13_23.txt').read().split('\n\n')]

result = 0 
for block in b:

    block_trans = [''.join(list(a)) for a in zip(*block)]

    rows = mirror(block)
    result+=100*rows

    if rows:
        continue

    cols = mirror(block_trans)

    result += cols

print(f'result is {result}')