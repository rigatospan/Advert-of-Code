def overlap(brick1, brick2):
    # [a,b] overlaps with [c,d] if max(a,c)<=min(b,d)
    overlap_x = max(brick1[0][0], brick2[0][0]) <= min(brick1[1][0], brick2[1][0])
    overlap_y = max(brick1[0][1], brick2[0][1]) <= min(brick1[1][1], brick2[1][1])
    
    return overlap_x and overlap_y
    

bricks = [ [list(map(int,a.split(','))) for a in line.split('~')] for line in open('d22_23.txt').read().splitlines()]
# sort the bricks in ascending height
bricks.sort(key= lambda x: x[0][-1])

# keep a list with the positions of the bricks when they settled
settled_bricks = []

for brick in bricks:
    final_brick_z = 1

    # find the settled brick with the heighest z that overlapps with brick
    for settled_brick in settled_bricks[::-1]:
        if overlap(brick, settled_brick):
            brick_z = settled_brick[1][2]+1
            if brick_z>final_brick_z:
                final_brick_z = brick_z

    final_brick = [[brick[0][0], brick[0][1], final_brick_z], [brick[1][0], brick[1][1], brick[1][2]-brick[0][2] + final_brick_z ] ]
    settled_bricks.append(final_brick)

settled_bricks.sort(key= lambda x: x[0][-1])


# define two dictionaries for each brick: 
# one listing the bricks that it supports
supporting = {i:[] for i in range(len(settled_bricks))}
# and one that keeps the number of bricks that support that brick
supported = {i:[] for i in range(len(settled_bricks))}

for i, brick in enumerate(settled_bricks):
    for j, another_brick in enumerate(settled_bricks):
        if overlap(brick, another_brick):
            # check if the brick supports another brick
            if brick[1][2]+1 == another_brick[0][2]:
                supporting[i].append(j)
            # check if the brick is supported by another brick
            if brick[0][2]-1 == another_brick[1][2]:
                supported[i].append(j)


# for each brick find the bricks that would fall if that brick was removed
cause_to_fall = {i:[] for i in range(len(settled_bricks))}

for i in cause_to_fall:
    
    # brick directly supported by i will fall if they only supported by i
    cause_to_fall[i] = [s for s in supporting[i] if len(supported[s])==1 ]
    
    # check if the above bricks will fall
    for j in range(i+1, len(settled_bricks)):
        
        # check if the j brick has already fallen or it is not supported by any brick
        if j in cause_to_fall[i] or supported[j] == []:
            continue
        
        # brick j will fall if all the bricks that support it have fallen
        if all( [brick in cause_to_fall[i] for brick in supported[j] ] ):
            cause_to_fall[i].append(j)

# sum the number of bricks that would fall if each brick would be removed
print(sum([len(val) for val in cause_to_fall.values()]))