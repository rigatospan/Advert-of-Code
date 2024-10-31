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
supported = {i:0 for i in range(len(settled_bricks))}

for i, brick in enumerate(settled_bricks):
    for j, another_brick in enumerate(settled_bricks):
        if overlap(brick, another_brick):
            # check if the brick supports another brick
            if brick[1][2]+1 == another_brick[0][2]:
                supporting[i].append(j)
            # check if the brick is supported by another brick
            if brick[0][2]-1 == another_brick[1][2]:
                supported[i]+=1 

# find the number of bricks that can be individually removed
# a brick can be removed if it doesn't support any other brick
# or if all the bricks that it supports are supported by at least two bricks
result = 0

for i in supporting:
    # check if brick i supports any other brick
    if supporting[i]:
        # if yes, check if the other bricks are supported by at least two bricks
        if all([supported[s]>1 for s in supporting[i]]):
            result+=1
    # if not it can be removed
    else:
        result+=1

print(result)