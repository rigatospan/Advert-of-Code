from collections import OrderedDict

def hash_word(word:str):
    hash = 0
    for char in word:
        hash = (17*(hash+ord(char))) % 256
    
    return hash    
 
file = 'd15_23.txt'
data = open(file).read().split(',')

# use OrderDict for the labels-focal_length pairs of each box 
# to keep the order of inserting and updating the labels intacked
# box_number: OrderDict{label: focal_length}
boxes = {n: OrderedDict() for n in range(256)}
for word in data:
    if word[-1] == '-':
        w, operation, focal_length = word[:-1], word[-1], None
    else:
        w, operation, focal_length = word[:-2], word[-2], int(word[-1])
    
    box_number = hash_word(w)
   
    # remove from the box box_number the lens w
    if operation == '-':
        if w in boxes[box_number]:
            del boxes[box_number][w]
        
        continue
    
    # replace or add to the box the label and focal length
    # using an ordered dictionary would do that in place
    boxes[box_number][w] = focal_length

result = 0
for i in boxes:
    for j, label in enumerate(boxes[i], start=1):
        result += (i+1)*j*boxes[i][label]
        
print(result)