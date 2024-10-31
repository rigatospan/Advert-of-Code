# dat = open('d15_23.txt').read().split(',')
# values = []
# for word in dat:  
#     s = 0
#     for c in word:
#         s= (17*(s+ord(c))) % 256
#     values.append(s)
# print(sum(values))

def hash_word(word:str):
    hash = 0
    for char in word:
        hash = (17*(hash+ord(char))) % 256
    
    return hash    
        
file = 'd15_23.txt'
data = open(file).read().split(',')

result = 0
for word in data:
    result+=hash_word(word)
    
print(result)